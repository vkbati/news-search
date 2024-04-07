import news_search
api_key = "YOUR API"

eng_query = news_search.query("bitcoin", api_key=api_key, lang="en")
ger_query = news_search.query("bitcoin", api_key=api_key, lang="de")


