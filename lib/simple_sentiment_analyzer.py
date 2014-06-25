from positive_words_matcher import PositiveWordsMatcher
from negative_words_matcher import NegativeWordsMatcher

class SimpleSentimentAnalyzer:

    def __init__(self):
        self.positive_words_matcher = PositiveWordsMatcher()
        self.negative_words_matcher = NegativeWordsMatcher()

    def calculate_sentiment(self, text):
        positive_words = self.positive_words_matcher.positive_words(text)
        negative_words = self.negative_words_matcher.negative_words(text)
        positive_count = sum(positive_words.values())
        negative_count = sum(negative_words.values())
        total = positive_count + negative_count
        if total:
            return float(positive_count-negative_count) / total
        return 0.0

