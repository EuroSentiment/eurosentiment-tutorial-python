# encoding: utf-8
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#  The original code are licensed under the GNU Lesser General Public License.

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

