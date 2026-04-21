import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.llm_client import ask_llm

with open("prompts/base_input.txt", "r") as f:
    data = f.read()

prompt = f"""
You are a senior financial analyst.

Analyze the following data and provide key insights.

Data:
{data}

Constraints:
- Do not assume missing data
- Keep response under 80 words

Output format:
- Summary
- Key Insight
"""

response = ask_llm(prompt)

print("\nROLE BASED OUTPUT:\n")
print(response)
