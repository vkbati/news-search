from transformers import BartForConditionalGeneration, BartTokenizer, pipeline, BertTokenizer, BertModel
from typing import List, Text


def generate_summary(text: str, lang: str) -> Text:
    '''
    :param text:
    :param lang:

    This function uses fine-tuned BART models for summarizing.
    '''

    if lang == "en":
        '''
        English
        '''
        # Define the summarization pipeline with BART model
        summarizer = pipeline("summarization", model="ubikpt/t5-small-finetuned-cnn")
        text2sum = "summarize: " + text
        words = text.split()
        max_length = len(words) + 2
        min_lenth = len(words) - 2
        summary = summarizer(text2sum, max_length=max_length, min_length=min_lenth)
        summary_text = summary[0]['summary_text']
    elif lang == "de":
        '''
        German
        '''


        words = text.split()
        max_length = len(words) + 2
        min_lenth = len(words) - 2
        summarizer = pipeline("summarization", model="Shahm/t5-small-german")
        text2sum = "summarize: " + text
        # Generate summary
        summary = summarizer(text2sum, max_length=max_length, min_length=min_lenth)
        summary_text = summary[0]['summary_text']


    return summary_text

def get_summary(result, lang: str):
    '''
    :param result:
    :param lang:
    :return:

    This function summarizes the headlines
    '''
    headlines = [article['title'] for article in result]
    summaries = []
    for headline in headlines:
        summaries.append(generate_summary(headline, lang))
    return summaries
