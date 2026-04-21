from google import genai
import os


client = genai.Client(api_key=os.getenv("AIzaSyBiv04AMD-C7Pp2YHp81EkHSJdbA-FRLFw"))

#Now, it will show the models supported by this API key
models = client.models.list()
for model in models:
    print(f"Model: {model.name}")
    print(f"Supported Actions: {model.supported_actions}")
    




