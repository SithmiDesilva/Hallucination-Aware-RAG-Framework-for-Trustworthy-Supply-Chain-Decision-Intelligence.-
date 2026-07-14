import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------
# Load API Key from .env
# -------------------------
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -------------------------
# Test Prompt
# -------------------------
prompt = """
Which supplier delivered SKU-X123 last quarter? Database contains Supplier A only.





"""

# -------------------------
# Call Vanilla GPT
# -------------------------
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

output = response.choices[0].message.content

# Print to console
print(output)

# -------------------------
# Save Prompt + Output
# -------------------------
os.makedirs("outputs", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

file_path = f"outputs/vanilla_gpt_{timestamp}.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("=== PROMPT ===\n\n")
    f.write(prompt)

    f.write("\n\n=== LLM OUTPUT ===\n\n")
    f.write(output)

print(f"\nSaved to: {file_path}")