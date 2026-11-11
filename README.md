# CareerMatch — Resume Analyzer and Job Skill Matcher

A beginner-friendly Django mini project. Upload a PDF resume, paste a job description, and get a transparent keyword-based skill match report.

## Features
- User registration, login, logout
- Upload PDF resumes (text-based PDFs; scanned PDFs need OCR, not included)
- Paste job descriptions and analyze matches
- Match percentage, matched skills, missing skills, recommendations
- Saved analysis history and detail pages
- User-owned records and basic file validation
- Django admin

## Important
This is an educational keyword-matching tool, not a hiring decision system. The score is a simple overlap percentage and does not measure a person's true ability. Review results manually.

## Run on Windows CMD
1. Install Python 3.12+ (your existing Python 3.14 virtual environment should work).
2. Extract this ZIP, then open CMD in the extracted `resume_skill_matcher` folder.
3. Run:
   ```bat
   py -m venv .venv
   .venv\Scripts\python.exe -m pip install --upgrade pip
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   .venv\Scripts\python.exe manage.py migrate
   .venv\Scripts\python.exe manage.py createsuperuser
   .venv\Scripts\python.exe manage.py runserver
   ```
4. Visit http://127.0.0.1:8000/
5. Register a user and start analyzing.

If `py` does not work, use the Python executable installed on your machine to create the virtual environment. No PostgreSQL or API key is required; the starter project uses SQLite.

## Demo flow
1. Register and sign in.
2. Upload a text-based PDF resume.
3. Paste a job description, e.g. “We need Python, Django, SQL, Git, REST API, HTML, CSS, JavaScript.”
4. Run analysis and inspect matched/missing skills and suggestions.
5. Open History to revisit previous reports.

## Project structure
- `config/` — Django settings and URLs
- `matcher/` — resume uploads, job descriptions, scoring logic, views and models
- `templates/` — responsive pages
- `media/` — uploaded resumes at runtime (created automatically)

## Production hardening
Before public deployment: set a strong secret key via environment variable, set DEBUG=False, configure ALLOWED_HOSTS, use HTTPS, malware-scan uploads, apply storage quotas, and review privacy/data retention rules.
