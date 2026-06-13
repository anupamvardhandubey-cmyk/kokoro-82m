import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# API Key setup (Railways Variables se hi uthayega)
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not model:
        return jsonify({"reply": "API Key nahi mili, Railway settings check karo!"})
    user_input = request.json.get("message")
    response = model.generate_content(user_input)
    return jsonify({"reply": response.text})

if __name__ == '__main__':
    app.run()
    
            
