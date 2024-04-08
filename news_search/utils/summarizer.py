from transformers import BartForConditionalGeneration, BartTokenizer, pipeline, BertTokenizer, BertModel
from typing import List, Text
import torch

def generate_summary(text: str, lang: str) -> Text:

    if lang == "en":
        model_name = "sshleifer/distilbart-cnn-12-6"
        # Check if GPU is available and move model to GPU if it is
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name).to(device)

        # Define the summarization pipeline with BART model
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=0 if device == 'cuda' else -1)

        # Generate summary
        summary = summarizer(text, max_length=15, min_length=5)
        summary_text = summary[0]['summary_text']
    elif lang == "de":
        model_name = "Shahm/bart-german"
        # Check if GPU is available and move model to GPU if it is
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name).to(device)

        # Define the summarization pipeline with BART model
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=0 if device == 'cuda' else -1)

        # Generate summary
        summary = summarizer(text, max_length=15, min_length=5)
        summary_text = summary[0]['summary_text']


    return summary_text

def get_summary(result, lang: str):
    headlines = [article['title'] for article in result]
    summaries = []
    for headline in headlines:
        summaries.append(generate_summary(headline, lang))
    return summaries