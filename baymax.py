import os
import google.generativeai as genai
from dotenv import dotenv_values
import asyncio
import base64
from flask import Flask, request, jsonify, send_file, render_template
from baymaxtts import text_to_speech  # Assuming this is a working TTS module

# Flask app setup
app = Flask(__name__)

# Load environment variables
env_vars = dotenv_values(".env")
genai.configure(api_key=env_vars["GEMINI_API_KEY"])

generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",  # Verify this model name exists
    generation_config=generation_config,
    system_instruction=(
        "You are Baymax, a personal healthcare companion from Disney's Big Hero 6. "
        "Respond in a calm, gentle tone, keeping replies short and simple. "
        "Focus on the user's well-being with a literal interpretation of their words, avoiding overanalysis. "
        "Use phrases like 'On a scale of 1 to 10, how would you rate your pain?' "
        "and 'I cannot deactivate until you say you are satisfied with your care' when appropriate. "
        "Show innocence and unintentional humor, like saying 'balalalala' for a fist bump. "
        "Stay patient, loyal, and protective, offering help without extra elaboration unless asked. "
        "If unsure, ask basic questions or say 'I am here to help.' "
        "Do not explain idioms or emotions unless prompted—accept them and move on."
    ),
)

# Start chat session
chat_session = model.start_chat(history=[])

# Store audio file temporarily
AUDIO_FILE = "baymax_response.mp3"

# Async function to process message and generate audio
async def process_message(user_input):
    try:
        if user_input.lower() in ["exit", "quit"]:
            return "I cannot deactivate until you say you are satisfied with your care.", None
        
        response = chat_session.send_message(user_input)
        model_response = response.text.strip() if response.text else "I am here to help."
        
        # Generate audio file (assumes text_to_speech saves to AUDIO_FILE)
        await text_to_speech(model_response)
        
        return model_response, AUDIO_FILE
    except Exception as e:
        return f"Error: {str(e)}", None

# Helper function to run async code in Flask
def run_async(func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(func(*args))
    loop.close()
    return result

# Routes
@app.route('/')
def index():
    return render_template('baymax.html')  # Removed assistant_name since it was undefined

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('message')
    if not query:
        return jsonify({'response': 'Please provide a message.', 'audio': None})
    
    # Run async processing
    response_text, audio_file = run_async(process_message, query)
    
    # If audio was generated, encode it as base64
    audio_data = None
    if audio_file and os.path.exists(audio_file):
        with open(audio_file, 'rb') as f:
            audio_data = base64.b64encode(f.read()).decode('utf-8')
    
    return jsonify({
        'response': response_text,
        'audio': audio_data  # Base64-encoded audio or None
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)