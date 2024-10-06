from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)

# CORS nur für spezifische Domain (GitHub Pages) erlauben
CORS(app, resources={r"/api/*": {"origins": "https://gawelskitools.github.io"}})

# Setze den OpenAI API-Schlüssel als Umgebungsvariable in Heroku
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        # Response für Preflight OPTIONS Anfrage
        return jsonify({"message": "CORS preflight passed"}), 200
    
    data = request.json
    prompt = data.get("prompt")

    # An ChatGPT API senden
    response = openai.Completion.create(
        engine="text-davinci-003",  # oder ein anderes Modell
        prompt=prompt,
        max_tokens=100
    )

    reply = response.choices[0].text.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
