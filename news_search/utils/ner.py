import spacy
from collections import Counter
from typing import List

def sort_ner(result, lang: str) -> List:
    '''
    :param result:
    :param lang:

    This function captures named entities and sorts them by their freq
    '''
    # Extract named entities from headlines
    headlines = [article['title'] for article in result]
    if lang == "en":
        nlp = spacy.load("en_core_web_sm")
    elif lang == "de":
        nlp = spacy.load("de_core_news_sm")
    named_entities = []
    for headline in headlines:
        doc = nlp(headline)
        for ent in doc.ents:
            named_entities.append(ent.text)

    # Calculate frequency of named entities
    entity_freq = Counter(named_entities)

    # Sort entities by frequency
    sorted_entities = sorted(entity_freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_entities