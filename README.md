# Vibe Coding App Generator

A web app that suggests vibe coding project ideas based on two users' combined work experience. Powered by Claude AI.

## What It Does

Enter work experience for two users (Euty and Simon), click "Suggest App Ideas", and get 3 tailored app suggestions that leverage both users' backgrounds. Vibe coding means building apps with AI assistance — describe what you want and AI generates the code.

## Tech Stack

- **Backend**: Python / Flask
- **AI**: Claude Haiku 4.5 (Anthropic API)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Deployment**: Railway (auto-deploys from GitHub)

## Getting Started

### Prerequisites
- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

### Setup

```bash
# Clone the repo
git clone https://github.com/SGMurray06/hello-world.git
cd hello-world

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "ANTHROPIC_API_KEY=your-key-here" > .env

# Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Project Structure

```
├── app.py              # Flask backend + Claude API integration
├── templates/
│   └── index.html      # Frontend UI and JavaScript
├── static/
│   └── style.css       # Styling
├── requirements.txt    # Python dependencies
├── Procfile            # Production server config
├── .env                # API key (not committed)
└── .gitignore
```

## Deployment

This app is deployed on [Railway](https://railway.app/) and auto-deploys on every push to GitHub. To deploy your own:

1. Push to a GitHub repository
2. Connect the repo in Railway
3. Add `ANTHROPIC_API_KEY` in Railway's Variables tab
4. Railway auto-detects the Procfile and deploys

## Built With

Built using vibe coding with [Claude Code](https://claude.ai/code).
