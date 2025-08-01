from huggingface_hub import InferenceClient
import json
from dotenv import load_dotenv
import os

load_dotenv()
client = InferenceClient(provider="hf-inference", api_key=os.getenv("HF_TOKEN"))

result = client.text_classification(
    "I like you. I love you",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)
json_result = json.dumps(result, indent=2)
print(json_result)
