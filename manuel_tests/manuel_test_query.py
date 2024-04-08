import news_search
api_key = "YOUR API"

eng_query = news_search.query("bitcoin", api_key=api_key, lang="en", max_news=1)
ger_query = news_search.query("apple", api_key=api_key, lang="de", max_news=2)
print(eng_query)
print(ger_query)

