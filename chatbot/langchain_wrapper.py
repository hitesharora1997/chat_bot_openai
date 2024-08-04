import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
        self.conversation_history = []

    def get_response(self, message):
        window_knowledge = {
            "types of windows": "Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows.",
            "how windows are manufactured": "Window manufacturing involves cutting and assembling glass panes and frames, often using materials like vinyl, wood, or aluminum."
        }

        for key, value in window_knowledge.items():
            if key in message.lower():
                return value

        self.conversation_history.append({"role": "user", "content": message})
        
        try:
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                *self.conversation_history
            ]
            response = self.client.chat.completions.create(
                model="mixtral-8x7b-instruct",
                messages=messages
            )
            response_content = response.choices[0].message.content
        except Exception as e:
            response_content = f"An error occurred: {str(e)}"

        self.conversation_history.append({"role": "assistant", "content": response_content})

        return response_content