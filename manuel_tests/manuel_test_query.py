import news_search
api_key = "a82492b6f44d45a685e1712f3e644552"

eng_query = news_search.query("bitcoin", api_key=api_key, lang="en", max_news=1)
ger_query = news_search.query("bitcoin", api_key=api_key, lang="de", max_news=2)
print(eng_query)
print(ger_query)

