import torch
from models.model_loader import load_model
from agent.prompts import build_prompt

class Agent:
    def __init__(self, model_name="google/flan-t5-small"):
        self.tokenizer, self.model = load_model(model_name)

    def respond(self, user_input: str) -> str:
        prompt = build_prompt(user_input)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # return self.tokenizer.decode(outputs[0], skip_special_tokens=True)