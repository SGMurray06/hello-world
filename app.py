import json

from flask import Flask, render_template, jsonify, request
import anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/suggest-apps", methods=["POST"])
def suggest_apps():
    data = request.get_json()
    euty_experience = (data.get("euty_experience") or "").strip()
    simon_experience = (data.get("simon_experience") or "").strip()

    if not euty_experience or not simon_experience:
        return jsonify({"error": "Both users must provide their experience."}), 400

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system="You are a helpful assistant. Always respond with valid JSON only. No markdown, no code fences, no extra text.",
            messages=[
                {
                    "role": "user",
                    "content": f"""Vibe coding means building software applications primarily through AI assistance -- you describe what you want in natural language and AI generates the code.

Here are two people who want to build a vibe coding project together:

Euty's experience:
{euty_experience}

Simon's experience:
{simon_experience}

Suggest exactly 3 practical vibe coding app ideas that leverage their combined skills and backgrounds. For each idea, provide a title and a brief description (2-3 sentences).

Respond as a JSON array of 3 objects, each with "title" and "description" keys.""",
                }
            ],
        )

        text = message.content[0].text.strip()
        # Strip markdown fences if the LLM adds them
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()

        suggestions = json.loads(text)
        return jsonify({"suggestions": suggestions})

    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse suggestions. Please try again."}), 500
    except anthropic.APIError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
