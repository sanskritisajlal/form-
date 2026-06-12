# AI Music Analyser — Early Access Form

## What's in here

```
pitch-analyzer/
├── api/
│   └── index.py        ← Python FastAPI backend (writes to Google Sheets)
├── public/
│   └── index.html      ← The form (frontend)
├── requirements.txt
├── vercel.json
└── README.md
```

---

## Step 1 — Set up Google Service Account

1. Go to https://console.cloud.google.com
2. Create a new project (or use an existing one)
3. Enable **Google Sheets API** — search for it in the API Library
4. Go to **IAM & Admin → Service Accounts → Create Service Account**
   - Name it anything (e.g. `sheets-writer`)
   - Skip optional steps, click Done
5. Click the service account → **Keys tab → Add Key → JSON**
   - Download the JSON file — keep it safe, don't commit it anywhere

6. Open your Google Sheet:
   `https://docs.google.com/spreadsheets/d/1gYvSzVG15-WjdsbCtA05r2dWdGqvFfn3BEOm9Gy4qgU`
   - Click **Share**
   - Paste the service account email (looks like `name@project.iam.gserviceaccount.com`)
   - Give it **Editor** access

---

## Step 2 — Deploy to Vercel

1. Push this whole folder to a GitHub repo
2. Go to https://vercel.com → Import that repo
3. In **Environment Variables**, add one variable:
   - Key: `GOOGLE_SERVICE_ACCOUNT_JSON`
   - Value: paste the **entire contents** of the JSON file you downloaded
4. Deploy — Vercel handles everything else

---

## That's it

Every form submission will appear as a new row in your Sheet with:
- Timestamp
- Name
- Email
- Q1–Q4 answers

No maintenance needed. Free on Vercel's hobby plan.
