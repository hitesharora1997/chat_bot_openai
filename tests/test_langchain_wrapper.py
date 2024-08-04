import os
import pytest
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from unittest.mock import MagicMock, patch
from chatbot.langchain_wrapper import ChatBot

load_dotenv()

@pytest.fixture
def api_key():
    return os.getenv("OPENAI_API_KEY")

@pytest.fixture
def chatbot(api_key):
    return ChatBot(api_key=api_key)

def test_get_response_knowledge(chatbot):
    message = "What types of windows exist?"
    response = chatbot.get_response(message)
    assert response == "Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows."

@patch.object(ChatOpenAI, '__call__')
def test_get_response_manufacturing(mock_llm_call, chatbot):
    message = "How are windows manufactured?"
    mock_llm_call.return_value.content = "Window manufacturing involves cutting and assembling glass panes and frames, often using materials like vinyl, wood, or aluminum."
    
    response = chatbot.get_response(message)
    
    assert response == "Window manufacturing involves cutting and assembling glass panes and frames, often using materials like vinyl, wood, or aluminum."

@patch.object(ChatOpenAI, '__call__')
def test_get_response_conversation(mock_llm_call, chatbot):
    message = "Tell me more about bay windows."
    mock_llm_call.return_value.content = "Bay windows are typically made up of a center window and two angled side windows."
    
    response = chatbot.get_response(message)
    
    assert response == "Bay windows are typically made up of a center window and two angled side windows."
    assert len(chatbot.conversation_history) == 2
    assert isinstance(chatbot.conversation_history[0], HumanMessage)
    assert chatbot.conversation_history[0].content == message
    assert isinstance(chatbot.conversation_history[1], SystemMessage)
    assert chatbot.conversation_history[1].content == response

@patch.object(ChatOpenAI, '__call__', side_effect=Exception("API error"))
def test_get_response_api_error(mock_llm_call, chatbot):
    message = "Tell me more about bay windows."
    
    response = chatbot.get_response(message)
    
    assert response == "An error occurred: API error"
    assert len(chatbot.conversation_history) == 2
    assert isinstance(chatbot.conversation_history[0], HumanMessage)
    assert chatbot.conversation_history[0].content == message
    assert isinstance(chatbot.conversation_history[1], SystemMessage)
    assert chatbot.conversation_history[1].content == response
