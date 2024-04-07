import unittest
import csv
from news_search.utils.generate_csv import gen_csv

class TestGenCSV(unittest.TestCase):
    def setUp(self):
        # Initialize some sample articles data for testing
        self.articles = {
            'articles': [
                {'title': 'Article 1', 'url': 'http://example.com/article1', 'publishedAt': '2024-04-01'},
                {'title': 'Article 2', 'url': 'http://example.com/article2', 'publishedAt': '2024-04-02'},
                {'title': 'Article 3', 'url': 'http://example.com/article3', 'publishedAt': '2024-04-03'}
            ]
        }

    def test_gen_csv(self):
        # Call the function with sample data
        gen_csv(self.articles)

        # Open the generated CSV file and read its contents
        with open("../search_output.csv", 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

            # Assert that the CSV file has the correct number of rows
            self.assertEqual(len(rows), len(self.articles['articles']))

            # Assert that each row in the CSV file matches the corresponding article data
            for idx, article in enumerate(self.articles['articles']):
                self.assertEqual(rows[idx]['title'], article['title'])
                self.assertEqual(rows[idx]['url'], article['url'])
                self.assertEqual(rows[idx]['publishedAt'], article['publishedAt'])

if __name__ == '__main__':
    unittest.main()
