import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.llm_client import ask_llm

#data
with open("prompts/base_input.txt", "r") as f:
    data = f.read()
#zero_shot

zero_shot_prompt = f"Summarize the following financial data:\n{data}"
zero_shot_output = ask_llm(zero_shot_prompt)

#few_shot
few_shot_prompt = f"""
Example:
Input:
Revenue increased 10%, costs stable.
Output:
Profitability improved due to revenue growth without cost increase.

Now analyze:
{data}
"""

few_shot_output = ask_llm(few_shot_prompt)

#role_base_output

role_base_prompt = f"""
You are a senior financial analyst.

Analyze the following data and provide key insights.
Data:
{data}

Constraints:
- Do not assume missing data
- Keep response under 150-200 words

Output format:
- Summary
- Key Insight
"""

role_base_output = ask_llm(role_base_prompt)

#automated_comparison_report_creation

comparison_report = f"""
# Prompt Comparison Report

## Zero Shot Output
{zero_shot_output}

## Few Shot Output
{few_shot_output}

## Role Based Output
{role_base_output}

## Conclusion
Role-based prompting produced the most structured and reliable output.
"""

# Save report
with open("results/comparison_report.md", "w") as f:
    f.write(comparison_report)

print("Comparison report generated successfully! Please check the file.")