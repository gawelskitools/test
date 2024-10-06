from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS für alle Routen aktivieren

# Setze den OpenAI API-Schlüssel als Umgebungsvariable in Heroku
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt")

    # An ChatGPT API senden
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    reply = response.choices[0].text.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
