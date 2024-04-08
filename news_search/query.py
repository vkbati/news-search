from news_search.utils import generate_csv, ner, summarizer, search
from typing import List, Dict
def query(topic: str, api_key: str, lang: str = "en", max_news: int = 15)-> List[Dict]:
    '''
    :param topic:
    :param api_key:
    :param lang:
    :param max_news:

    This is the main function which assembles necessary functions.
    '''
    result, articles = search.search_news(topic, api_key=api_key, lang=lang, max_news=max_news)
    generate_csv.gen_csv(articles, topic)
    summs = summarizer.get_summary(result, lang)
    sorted_ner = ner.sort_ner(result, lang)
    final_result = []
    final_result.append({'info': result, 'summary': summs, "ner_freqs": sorted_ner})

    return final_result