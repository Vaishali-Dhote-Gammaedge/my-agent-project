# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# import torch

# def load_model(model_name="google/flan-t5-small"):
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     # model = AutoModelForCausalLM.from_pretrained(
#     model = AutoModelForSeq2SeqLM.from_pretrained(
#         model_name,
#         torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
#         device_map="auto"
#     )
#     return tokenizer, model
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model(model_name="mistralai/Mistral-7B-Instruct-v0.2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    return tokenizer, model
