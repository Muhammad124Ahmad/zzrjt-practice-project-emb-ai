import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
         result_1 = sentiment_analyzer('I love working with Python')
         self.assertEqual(result_1['label'], 'POSITIVE')
         result_2 = sentiment_analyzer('I hate working with Python')
         self.assertEqual(result_2['label'], 'NEGATIVE')        

unittest.main()         