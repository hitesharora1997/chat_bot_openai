from flask import Flask, request, jsonify, send_from_directory
from chatbot.langchain_wrapper import ChatBot  # Adjust the import as necessary
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
chatbot = ChatBot(api_key=OPENAI_API_KEY)

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)