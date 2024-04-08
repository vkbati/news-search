from datetime import datetime, timedelta
from newsapi import NewsApiClient


def search_news(topic: str, api_key: str, lang: str = "en", max_news: int = 15):
    # Your function implementation

    # Initialize News API client
    newsapi = NewsApiClient(api_key=api_key)


    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # Fetch news articles
    articles = newsapi.get_everything(q=topic,
                                      from_param=start_date.strftime('%Y-%m-%d'),
                                      to=end_date.strftime('%Y-%m-%d'),
                                      language=lang,
                                      sort_by='relevancy')

    # Extract relevant information from articles
    result = []
    for article in articles['articles'][:max_news]:
        result.append({
            'title': article['title'],
            'url': article['url'],
            'published_at': article['publishedAt']
        })

    return result, articles













    # with open("search_output.csv", 'w', newline='', encoding='utf-8') as csvfile:
    #     fieldnames = ['title', 'url', 'publishedAt']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #     writer.writeheader()
    #     for article in articles['articles']:
    #         writer.writerow({key: article[key] for key in fieldnames})
    #
    # headlines = [article['title'] for article in result_15]
    # summaries = []
    # for headline in headlines:
    #     summaries.append(summarizer.generate_summary(headline))
    #
    # # Extract named entities from headlines
    # nlp = spacy.load("en_core_web_sm")
    # named_entities = []
    # for headline in headlines:
    #     doc = nlp(headline)
    #     for ent in doc.ents:
    #         named_entities.append(ent.text)
    #
    # # Calculate frequency of named entities
    # entity_freq = Counter(named_entities)
    #
    # # Sort entities by frequency
    # sorted_entities = sorted(entity_freq.items(), key=lambda x: x[1], reverse=True)
    #
    # results = {'info': result_15, 'summary': summaries, "ner_freqs": sorted_entities}
    #
    #
    # return results