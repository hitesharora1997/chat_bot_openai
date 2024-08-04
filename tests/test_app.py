import os
import pytest
from flask import Flask
from dotenv import load_dotenv
from unittest.mock import patch
from app import app

load_dotenv()

@pytest.fixture
def client():
    return app.test_client()

def test_chat_no_message(client):
    response = client.post('/chat', json={})
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'No message provided'

@patch('app.chatbot.get_response', return_value="Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows.")
def test_chat_with_message(mock_get_response, client):
    response = client.post('/chat', json={'message': 'What types of windows exist?'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data
    assert data['response'] == "Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows."

@patch('app.chatbot.get_response', return_value="An error occurred: API error")
def test_chat_with_error(mock_get_response, client):
    response = client.post('/chat', json={'message': 'Tell me more about bay windows.'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'response' in data
    assert data['response'] == "An error occurred: API error"
