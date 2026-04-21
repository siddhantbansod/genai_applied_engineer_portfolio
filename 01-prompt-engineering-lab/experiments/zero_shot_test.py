import sys
import os

# Fix path first
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import after path setup

from utils.llm_client import ask_llm

with open("prompts/base_input.txt", "r") as f:
    data = f.read()

prompt = f"Summarize the following financial data:\n{data}"

response = ask_llm(prompt)

print("\nZERO SHOT OUTPUT:\n")
print(response)
