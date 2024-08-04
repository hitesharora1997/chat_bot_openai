import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

class ChatBot:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key)
        self.conversation_history = []

    def get_response(self, message):
        window_knowledge = {
            "types of windows": "Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows.",
            "how windows are manufactured": "Window manufacturing involves cutting and assembling glass panes and frames, often using materials like vinyl, wood, or aluminum."
        }

        for key, value in window_knowledge.items():
            if key in message.lower():
                return value

        self.conversation_history.append(HumanMessage(content=message))
        
        try:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                *self.conversation_history
            ]
            response = self.llm(messages).content
        except Exception as e:
            response = f"An error occurred: {str(e)}"

        self.conversation_history.append(SystemMessage(content=response))

        return response