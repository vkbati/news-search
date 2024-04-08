# news_search
This module prompts users to input a topic of interest and then searches the web for recent news articles related to that topic. It utilizes a 3rd party API for retrieving news content. The output includes:

a) A list of the top-15 matching news articles' titles, URLs, and publication dates from the last month, sorted by relevancy to the given topic.

b) A CSV file containing the full list of titles, URLs, and publication dates of matching articles from the last month.

c) An automatically generated summary of the top-15 article headlines, along with a list of named entities mentioned in those headlines, sorted by frequency.

## API
The model uses Newsapi API. One can get the API key from here: https://newsapi.org/register

## Usage
```python
>>> import news_search
>>> api_key = "YOUR API"
>>> news_search.query("bitcoin", api_key=api_key, lang="en")
```

One can also adjust the amount of news articles (defaults to `15`)
```python
>>> news_search.query("bitcoin", api_key=api_key, lang="en", max_news=1)
```

## Languages
The `news_search` module currently supports the following languages:

| Language   | Code |
|------------|------|
| English    | `en` |
| German     | `de` |
Use the `lang` parameter to specify the language (defaults to `en`):
```python
>>> import news_search
>>> news_search.query("bitcoin", api_key=api_key, lang="de", max_news=2)
```
## Requiremenets
transformers

torch

newsapi-python

spacy

spacy-model-en_core_web_sm

spacy-model-de_core_news_sm

## License
The `news_search` package is licensed under the MIT License.