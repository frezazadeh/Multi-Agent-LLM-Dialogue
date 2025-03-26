import time
from enum import Enum
from openai import OpenAI
import anthropic

class AI(Enum):
    OPEN_AI = "OPEN AI"
    CLAUDE = "CLAUDE"
    OLLAMA = "OLLAMA"

class ChatSystem:
    def __init__(self, processor, system_string="", model="", type=AI.OPEN_AI):
        """
        Initialize the ChatSystem with a system message, model, and empty message history.
        """
        self.processor = processor
        self.system = system_string
        self.model = model
        self.messages = []
        self.type = type

    def call(self, message):
        # Append the new message to our history
        self.messages.append(message)
        toSend = self.messages.copy()
        try:
            if self.type == AI.CLAUDE:
                response = self.processor.messages.create(
                    model=self.model,
                    system=self.system,
                    messages=self.messages,
                    max_tokens=500
                )
                return response.content[0].text
            else:
                toSend.insert(0, {"role": "system", "content": self.system})
                completion = self.processor.chat.completions.create(
                    model=self.model,
                    messages=toSend
                )
                return completion.choices[0].message.content
        except Exception as e:
            print(f"Error in {self.type.value} call: {e}")
            return f"Error in {self.type.value} call: {e}"

def generate_chat_prompt(role, content):
    return {"role": role, "content": content}
