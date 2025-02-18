from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Chatbot responses
responses = [
    "Hey there! How can I help?",
    "That's interesting! Tell me more.",
    "I'm here to chat with you!",
    "What’s on your mind?",
    "Arham is always here for you!"
]

@app.route("/", methods=["GET"])
def home():
    return "Flask Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Get message from frontend (Netlify)
    user_message = data.get("message", "")

    bot_reply = random.choice(responses)  # Generate bot response

    return jsonify({"user": user_message, "bot": bot_reply})  # Send response

if __name__ == "__main__":
    app.run(debug=True)
