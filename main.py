import argparse
from news_search.utils import generate_csv, search, ner, summarizer

API_KEY = None

def get_api_key():
    """Function to get API key either from global variable or user input."""
    global API_KEY
    if API_KEY is None:
        API_KEY = input("Enter your API key: ")
    return API_KEY

def main(topic: str, api_key: str, lang: str = "en", max_news: int = 15):
    '''
    :param lang:
    :param max_news:
    :param topic:
    :param api_key:

    This is the main function which assembles necessary functions.
    '''
    while True:
        api_key = get_api_key()
        topic = input("Enter a topic to search for news articles (press q to quit): ")
        if topic.lower() == 'q':
            print("Exiting the program.")
            return
        result, articles = search.search_news(topic, api_key=api_key, lang=lang, max_news=max_news)
        generate_csv.gen_csv(articles, topic)
        summs = summarizer.get_summary(result, lang)
        sorted_ner = ner.sort_ner(result, lang)
        final_result = []
        final_result.append({'info': result, 'summary': summs, "ner_freqs": sorted_ner})
        print(final_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--lang', type=str, default='en', help='language for news search')
    parser.add_argument('--max_news', type=int, default=15, help='maximum number of news articles to fetch')
    parser.add_argument('--topic', type=str, help='topic to search for news articles')
    parser.add_argument('--api_key', type=str, help='API key for accessing news API')
    args = parser.parse_args()

    main(args.topic, args.api_key, args.lang, args.max_news)

