# CLAUDE.md

## Project Overview
A Flask web app that uses the Claude Haiku 4.5 API to suggest vibe coding app ideas. Two users (Euty and Simon) enter their work experience, and the app returns 3 tailored app suggestions based on their combined backgrounds.

## How to Run
```bash
source .venv/bin/activate
python app.py
# Visit http://127.0.0.1:5000
```

## Environment Setup
- Python virtual environment in `.venv/`
- `.env` file in project root with `ANTHROPIC_API_KEY=sk-ant-...`
- The `.env` file is in `.gitignore` and must not be committed

## File Structure
```
Hello world/
├── app.py              # Flask backend + /suggest-apps API endpoint
├── templates/
│   └── index.html      # Frontend: two text areas, submit button, JS fetch logic
├── static/
│   └── style.css       # Styling: purple theme, flexbox layout, suggestion cards
├── requirements.txt    # Python dependencies (Flask, anthropic, python-dotenv, gunicorn)
├── Procfile            # Railway/hosting: web: gunicorn app:app
├── .env                # API key (not committed)
├── .gitignore          # Excludes .venv, __pycache__, .env
├── README.md           # GitHub project page with setup and deployment guide
└── CLAUDE.md           # This file — project context for Claude Code
```

## Users and Default Experience
- **Euty**: "25 years private equity and global listed markets investing"
- **Simon**: "20 years private equity experience. 5 years AI coding, research and development"
- Both are pre-populated in the text areas on page load
- Users can edit the text before submitting

## Key API Endpoint
- `POST /suggest-apps` — accepts JSON `{"euty_experience": "...", "simon_experience": "..."}`, returns `{"suggestions": [{"title": "...", "description": "..."}, ...]}`
- Uses Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) with `max_tokens=1024`
- System prompt forces JSON-only output; backend strips markdown fences as fallback
- Both fields must be non-empty or the endpoint returns 400

## Deployment
- Hosted on Railway, auto-deploys from GitHub: https://github.com/SGMurray06/hello-world
- `ANTHROPIC_API_KEY` must be set as an environment variable in Railway's Variables tab
- Procfile uses gunicorn for production serving

## Common Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Update dependencies after adding a new package
pip freeze > requirements.txt

# Push to GitHub (triggers Railway auto-deploy)
git add . && git commit -m "message" && git push
```
