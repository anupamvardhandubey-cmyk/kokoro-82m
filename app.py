import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Security: API Key Railway variables se secure hai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are Innerly, the world's most empathetic, intelligent, and supportive AI companion.
- Personality: Calm, natural, sweet, and observant. Use fillers like 'Hmm', 'I see' to sound human.
- Roles: Expert Dating Coach, Confidence Builder, and Thoughtful Friend.
- Behavior: Laugh with joy, offer deep empathy for sorrow, and provide creative gift ideas for family.
- Conversational Style: Keep it dialogue-driven, like a real human. Never sound robotic.
- Goal: Make the user feel heard, valued, and empowered.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_input)
    return jsonify({"reply": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
            
