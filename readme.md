# LLaMA Local Chat

Hey there! 👋 Welcome to my LLaMA Local Chat project. This is a nifty little Python script that lets you chat with a locally-hosted LLaMA language model using Ollama. It's perfect for when you want to experiment with AI chatbots without relying on cloud services.

## What's this all about?

This project creates a simple command-line interface for chatting with an AI. It uses the LLaMA model (specifically llama3.1) through Ollama, which means you're running everything on your own machine. Pretty cool, right?

## Prerequisites

Before you dive in, make sure you've got these installed:
- Python 3.7 or higher
- Ollama (with the llama3.1 model)

## Setting Up

1. Clone this repo to your local machine.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Make sure Ollama is up and running:
   ```
   ollama serve
   ```
4. In a separate terminal, pull the llama3.1 model if you haven't already:
   ```
   ollama pull llama3.1
   ```

## Let's Chat!

To start chatting:
1. Open your terminal
2. Navigate to the project directory
3. Run:
   ```
   python asset.py
   ```
4. Start chatting with your AI assitant!

## How it works

The script sets up a conversation loop where you can input messages, and the AI responds. It maintains context, so the AI can refer back to earlier parts of the conversation. Neat, huh?

## Troubleshooting

Running into issues? Here are some quick fixes:
- Make sure Ollama is running (`ollama serve`)
- Check if llama3.1 is available (`ollama list`)
- If you see any error messages, they should guide you on what to do next

## Contributing

Found a bug? Have an idea for an improvement? Feel free to open an issue or submit a pull request. I'm always happy to collaborate!

Happy chatting! 🤖💬
