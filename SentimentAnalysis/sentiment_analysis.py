from huggingface_hub import InferenceClient
import json
from dotenv import load_dotenv
import os
load_dotenv()

def sentiment_analyzer(text_to_analyse):

    MODEL="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    HF_TOKEN=os.getenv("HF_TOKEN")
    client = InferenceClient(provider="hf-inference", api_key=HF_TOKEN)

    #received result as py list
    result = client.text_classification(
       text_to_analyse,
        model=MODEL,
    )
    label=result[0].label
    score=result[0].score

    return ({"label": label,"score": score})

