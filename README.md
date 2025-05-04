# Simple Chat App with LangChain and Claude

This repository contains a simple chat application built using LangChain and Anthropic's Claude model. The application allows you to have interactive conversations with an AI assistant.

## Features

- Direct interaction with Claude through a command-line interface
- Conversation memory storage
- Environment variable management using dotenv
- Two implementations:
  - Basic: Simple message exchange with Claude
  - Advanced: Maintains conversation history for context-aware responses

## Prerequisites

- Python 3.8 or higher
- Anthropic API key

## Setup

1. Clone this repository:
```bash
git clone git@github.com:khoatr1509/simple-chat-app.git
cd simple-chat-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -qU "langchain[anthropic]" python-dotenv
```

4. Create a `.env` file in the root directory and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Basic Version
Run the basic version to have a simple interaction with Claude:

```bash
python basic_chat.py
```

### Advanced Version with Memory
Run the advanced version to have a conversation with memory:

```bash
python chat_with_memory.py
```

In the advanced version, type 'exit' to end the conversation. The application will display the entire conversation history at the end.

## Project Structure

```
simple-chat-app/
├── .env                  # Environment variables (create this file)
├── README.md             # Project documentation
├── basic_chat.py         # Basic implementation
└── chat_with_memory.py   # Advanced implementation with memory
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
