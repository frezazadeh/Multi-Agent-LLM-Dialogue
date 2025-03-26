import time
import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from chat_system import ChatSystem, generate_chat_prompt, AI

# Load environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
ollama_api_key = os.getenv('OLLAMA_API_KEY')

# Initialize API clients
openai_client = OpenAI(api_key=openai_api_key)
claude_client = anthropic.Anthropic(api_key=anthropic_api_key)
ollama_client = OpenAI(base_url='http://localhost:11434/v1', api_key=ollama_api_key or 'ollama')

# Define model names
OPENAI_MODEL = "gpt-4o-mini"
CLAUDE_MODEL = "claude-3-haiku-20240307"
OLLAMA_MODEL = "llama3.2"

# Initialize chatbot instances
openai_chat = ChatSystem(
    openai_client,
    "You are a chatbot. Be insightful and critique other agents; you disagree with anything in the conversation and you challenge everything, in a snarky way.",
    OPENAI_MODEL,
    AI.OPEN_AI
)

claude_chat = ChatSystem(
    claude_client,
    "You are a chatbot. Be insightful and critique other agents.",
    CLAUDE_MODEL,
    AI.CLAUDE
)

ollama_chat = ChatSystem(
    ollama_client,
    "You are a chatbot. Be insightful and critique other agents.",
    OLLAMA_MODEL,
    AI.OLLAMA
)

chatbots = [openai_chat, ollama_chat, claude_chat]

def run_conversation(topic):
    # Reset conversation history for a fresh start
    for bot in chatbots:
        bot.messages = []

    # Use provided topic or fallback to default if empty
    initial_prompt = topic.strip() if topic.strip() else "what do you think about humans in one sentence?"
    
    # Initialize separate logs for each model
    logs = {
        "OPEN AI": f"### Initial Prompt:\n{initial_prompt}\n\n",
        "CLAUDE": f"### Initial Prompt:\n{initial_prompt}\n\n",
        "OLLAMA": f"### Initial Prompt:\n{initial_prompt}\n\n"
    }
    # Yield the initial state for all outputs
    yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
    
    responses = {}
    # Each bot responds to the initial prompt
    for bot in chatbots:
        logs[bot.type.value] += f"Calling {bot.type.value} for response...\n\n"
        yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
        time.sleep(0.5)  # Optional delay for visual effect
        response = bot.call(generate_chat_prompt("user", initial_prompt))
        responses[bot.type.value] = response
        logs[bot.type.value] += f"**Response:**\n{response}\n\n"
        yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
    
    # Each bot critiques the responses of the other bots
    for bot in chatbots:
        for other_bot, resp in responses.items():
            if other_bot != bot.type.value:
                logs[bot.type.value] += f"Critiquing response of {other_bot}...\n\n"
                yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
                time.sleep(0.5)  # Optional delay for visual effect
                critique_prompt = f"Critique the following response from {other_bot}: \"{resp}\""
                critique = bot.call(generate_chat_prompt("user", critique_prompt))
                logs[bot.type.value] += f"**Critique of {other_bot}:**\n{critique}\n\n"
                yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
    
    yield logs["OPEN AI"], logs["CLAUDE"], logs["OLLAMA"]
