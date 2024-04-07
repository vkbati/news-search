from news_search.utils import generate_csv, ner, summarizer, search
from typing import List, Dict
def query(topic: str, api_key: str, lang: str = "en")-> List[Dict]:
    result, articles = search.search_news(topic, api_key=api_key, lang=lang)
    generate_csv.gen_csv(articles)
    summs = summarizer.get_summary(result, lang)
    sorted_ner = ner.sort_ner(result, lang)
    final_result = []
    final_result.append({'info': result, 'summary': summs, "ner_freqs": sorted_ner})

    return final_result