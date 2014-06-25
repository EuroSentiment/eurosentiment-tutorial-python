import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../conf"))

from configuration import *
from clients import ResourceClient, ServiceClient
from sparql_queries import *
from text_utils import matches_count

class NegativeWordsMatcher:

    def __init__(self):
        self.language_detector = ServiceClient(LANG_DETECTION_URL, TOKEN)
        self.resource_client = ResourceClient(RESOURCES_URL, TOKEN)

    def negative_words(self, text):
        lang_result = self.language_detector.request({"text": text})
        language = lang_result.get("dc:language", None)
        query = ELECTRONICS_NEGATIVE_ENTRIES % language
        input = {"query": query,
                 "format": "application/json"}
        resources_result = self.resource_client.request(input)
        sentiment_words = self.__extract_words_from_response(resources_result)
        return matches_count(text, sentiment_words)

    def __extract_words_from_response(self, resources_response):
        words = []
        for word in resources_response.get("results", {}).get("bindings", []):
            words.append(word.get("wordWithSentiment", {}).get("value", None))
        return words
