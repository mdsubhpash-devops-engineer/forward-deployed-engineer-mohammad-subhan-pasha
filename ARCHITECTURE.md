# System Architecture - © 2026 Mohammad Subhan Pasha

## How FieldMitra Works

Field Officer (Mobile / Low Network)
        |
        v
Streamlit UI - FieldMitra Voice Ops
        |
        v
Recovery Tracker API (FastAPI) - /customers, /pending
        |
        v
SQLite Database - customers, loans
        |
        v
Ops Copilot (Gemini API) - Answers from real data
        |
        v
SQL Analytics - Village wise risk report

## Why This Design?
1. Officer has less time -> Voice + 1 Click UI
2. Low network -> Light API, no heavy frontend
3. Field data is messy -> SQLite first, easy to sync later
4. Manager needs answer fast -> SQL Analytics, not Excel

Author: Mohammad Subhan Pasha - Forward Deployed Engineer™
© 2026 All Rights Reserved.
