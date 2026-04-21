import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.llm_client import ask_llm
with open("prompts/base_input.txt", "r") as f:
    data = f.read()

prompt = f"""
Example:

Input:
Revenue increased 10%, costs stable.

Output:
Profitability improved due to revenue growth without cost increase.

Now analyze:

{data}
"""

response = ask_llm(prompt)

print("\nFEW SHOT OUTPUT:\n")
print(response)
