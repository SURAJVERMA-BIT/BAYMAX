# BAYMAX
<<<<<<< HEAD
# BAYMAX
=======
# Baymax AI Chatbot

Baymax AI is a personal healthcare companion chatbot(upgrade iin future for healthcare) inspired by Disney's **Big Hero 6**. It responds in a **calm, gentle tone**, focusing on user well-being with a simple and literal interpretation of messages. The chatbot also features **text-to-speech (TTS)** support to provide voice responses.

## Features
- Conversational AI powered by Google Gemini
- Voice output using TTS
- Simple and intuitive API
- Deployed using Flask

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Gemini API Key
- Flask
- Required dependencies (listed in `requirements.txt`)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/SURAJVERMA-BIT/BAYMAX.git
   cd BAYMAX
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
4. Run the application:
   ```sh
   python app.py
   ```

## API Endpoints
### 1. Chat Endpoint
- **Endpoint:** `/chat`
- **Method:** `POST`
- **Request Body:**
  ```json
  { "message": "Hello, Baymax!" }
  ```
- **Response:**
  ```json
  {
    "response": "Hello! I am Baymax, your personal healthcare companion.",
    "audio": "<base64-encoded-audio>"
  }
  ```

## Contribution Guidelines
- Feel free to **fork** the project and submit pull requests.
- Report issues and suggest improvements via GitHub **Issues**.
- Follow standard **PEP 8** coding guidelines.

## License
This project is licensed under the **MIT License**. Feel free to modify and use it as per your needs.

---
_If you have any questions, feel free to reach out! 🚀_

>>>>>>> 3d8afef (Initial commit - Added Baymax AI chatbot)
