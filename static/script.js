document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');

    function addMessage(content, className) {
        const message = document.createElement('div');
        message.className = `message ${className}`;
        message.textContent = content;
        chatBox.appendChild(message);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    window.sendMessage = function() {
        const message = userInput.value.trim();
        if (message) {
            addMessage(message, 'user-message');
            userInput.value = '';
            getResponse(message);
        }
    };

    function getResponse(message) {
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                addMessage(`Error: ${data.error}`, 'bot-message');
            } else {
                addMessage(data.response, 'bot-message');
            }
        })
        .catch(error => {
            addMessage(`Error: ${error.message}`, 'bot-message');
        });
    }

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});