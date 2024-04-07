import unittest
from news_search.utils.ner import sort_ner


class TestSortNER(unittest.TestCase):
    def setUp(self):
        # Sample test data
        self.result_en = [
            {'title': 'Apple is launching new products'},
            {'title': 'Microsoft announces partnership with GitHub'},
            {'title': 'Amazon Web Services experiencing outage'}
        ]
        self.result_de = [
            {'title': 'Apple startet neue Produkte'},
            {'title': 'Microsoft kündigt Partnerschaft mit GitHub an'},
            {'title': 'Amazon Web Services mit Ausfall'}
        ]

    def test_sort_ner_en(self):
        # Call the function with English test data
        sorted_entities = sort_ner(self.result_en, "en")

        # Assert that the returned value is a list
        self.assertIsInstance(sorted_entities, list)

        # Assert that the length of the returned list is correct
        self.assertEqual(len(sorted_entities), 4)  # We have three unique named entities in the sample data

        # Add more assertions as needed to check the correctness of the sorting

    def test_sort_ner_de(self):
        # Call the function with German test data
        sorted_entities = sort_ner(self.result_de, "de")

        # Assert that the returned value is a list
        self.assertIsInstance(sorted_entities, list)

        # Assert that the length of the returned list is correct
        self.assertEqual(len(sorted_entities), 4)  # We have three unique named entities in the sample data

        # Add more assertions as needed to check the correctness of the sorting


if __name__ == '__main__':
    unittest.main()
