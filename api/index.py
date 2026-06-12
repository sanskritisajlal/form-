from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import gspread
from google.oauth2.service_account import Credentials
import os
import json
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

SPREADSHEET_ID = "1gYvSzVG15-WjdsbCtA05r2dWdGqvFfn3BEOm9Gy4qgU"

class FormData(BaseModel):
    name: str
    email: EmailStr
    q1: str
    q2: str
    q3: str
    q4: str

def get_sheet():
    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not creds_json:
        raise HTTPException(status_code=500, detail="Missing credentials")
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    return sheet

@app.post("/api/submit")
async def submit(data: FormData):
    sheet = get_sheet()
    headers = sheet.row_values(1)
    if not headers:
        sheet.append_row([
            "Timestamp", "Name", "Email",
            "Q1 - What do you wonder?",
            "Q2 - Improving?",
            "Q3 - Would you use timestamps?",
            "Q4 - Feedback wanted on"
        ])
    sheet.append_row([
        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        data.name,
        data.email,
        data.q1,
        data.q2,
        data.q3,
        data.q4,
    ])
    return {"ok": True}
