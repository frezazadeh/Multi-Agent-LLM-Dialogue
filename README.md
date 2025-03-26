![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

# Multi-Chatbot Conversation

This project is an interactive multi-chatbot interface built with Gradio. It allows users to initiate a conversation topic and see how multiple AI models (currently **OPEN AI**, **CLAUDE**, and **OLLAMA**) respond and critique each other in real time. Each model’s output is displayed in its own separate box for clarity.

## Features

- **Interactive UI:** Built with Gradio to provide real-time updates and progress indicators.
- **Multi-Agent Dialogue:** Engage with multiple LLM models simultaneously.
- **Extensible Architecture:** Easily extend the project to integrate additional LLM models.
- **Modular Codebase:** The project is split into multiple files for better organization and maintainability.

## Configure Environment Variables

Create a .env file in the root directory with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
OLLAMA_API_KEY=your_ollama_api_key  # if required
