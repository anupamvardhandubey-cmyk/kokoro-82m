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
    <!DOCTYPE html>
<html>
<head>
    <style>
        body { background: #0b0e14; color: #fff; font-family: sans-serif; display: flex; justify-content: center; height: 100vh; margin: 0; }
        .container { width: 100%; max-width: 400px; padding: 20px; text-align: center; }
        .mode-btn { padding: 15px 30px; border-radius: 30px; border: none; cursor: pointer; background: #6c5ce7; color: white; margin: 10px; }
        #interface { margin-top: 50px; }
        .voice-toggle { margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Innerly</h1>
        <div class="voice-toggle">
            <select id="voiceSelect">
                <option value="female">Sweet Female Voice</option>
                <option value="male">Warm Male Voice</option>
            </select>
        </div>
        <button class="mode-btn" onclick="setMode('call')">📞 Calling Mode</button>
        <button class="mode-btn" onclick="setMode('chat')">💬 Chatting Mode</button>
        
        <div id="interface"></div>
    </div>

    <script>
        function setMode(mode) {
            const div = document.getElementById('interface');
            if (mode === 'call') {
                div.innerHTML = "<h2>Calling Innerly...</h2><div style='width:100px;height:100px;background:#e17055;border-radius:50%;margin:auto;'></div>";
            } else {
                div.innerHTML = "<textarea id='chatInput' style='width:90%; height:100px;'></textarea><br><button onclick='send()'>Send</button>";
            }
        }
    </script>
</body>
</html>
    
    
