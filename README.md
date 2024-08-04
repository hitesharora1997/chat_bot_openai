# window_chatbot

A web-based chatbot application specializing in window manufacturing, capable of answering questions about types of windows and their manufacturing processes.

## Features

- Provides information about various types of windows and their manufacturing processes.
- Maintains conversational context for follow-up questions.
- Uses LangChain for managing conversation history.
- Web-based interface using Flask for easy interaction.
- Docker support for containerization.
- Modular and testable code structure.

## Getting Started

### Prerequisites

- Python 3.6 or later
- `virtualenv` or `venv` for creating virtual environments
- Docker (for containerization)

### Project Structure

```plaintext
window_chatbot/
├── app.py
├── chatbot/
│   ├── __init__.py
│   ├── langchain_wrapper.py
├── .env
├── Dockerfile
├── requirements.txt
├── Makefile
├── tests/
├   ├── __init__.py
│   ├── test_langchain_wrapper.py
│   ├── test_app.py
```

## Example

### Usage
To use the chatbot, send a POST request to the /chat endpoint with a JSON payload containing the message.

### Input
```json
{
    "message": "What types of windows exist?"
}
```

### Output
```json
{
    "response": "Common types of windows include casement windows, double-hung windows, bay windows, and sliding windows."
}
```

Clone the repository:
   ```bash
   git clone git@github.com:hitesharora1997/bouquet_maker.git
   cd bouquet_maker
   ```
Create a virtual environment and install dependencies:
   ```bash
   make setup
   ```
Run the application:
   ```bash
   make run
   ```
To run the test:
   ```bash
   make test
   ```
Building Docker Image
   ```bash
   make docker
   ```
Running Docker Image
   ```bash
   make docker-run
   ```

Cleaning up the virtual environment and other generated files:
   ```bash
   make clean
   ```
Help
   ```bash
   make help
   ```

### Caveats and Limitations
Caveats and Limitations
- The current implementation processes flowers sequentially. Future versions could improve concurrency handling for higher performance.
- Error Handling: Basic error handling is implemented. More comprehensive error handling could be added for robustness.
- Testing Coverage: The tests cover major functionalities. Additional tests for edge cases and stress conditions could improve reliability.
- Code Maintainability: The code is structured for maintainability, with ongoing efforts to improve documentation and code clarity.
- Data Persistence: Currently, data is stored in memory during runtime and is not persisted after the application stops.