# # Simple reusable prompt templates

# SYSTEM_PROMPT = "You are a helpful AI assistant."

# def build_prompt(user_input: str) -> str:
#     return f"{SYSTEM_PROMPT}\nUser: {user_input}\nAgent:"
SYSTEM_PROMPT = """You are a smart AI assistant. 
- Always answer in full sentences.
- Be clear, detailed, and helpful.
- If the user asks about languages, reply whether you understand and can speak it.
"""

def build_prompt(user_input: str) -> str:
    return f"{SYSTEM_PROMPT}\nUser: {user_input}\nAssistant:"

