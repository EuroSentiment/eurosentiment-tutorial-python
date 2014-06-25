# encoding: utf-8
from unicodedata import normalize

def flatten(text):
    if not isinstance(text, unicode):
        text = text.decode('utf-8', errors="ignore")
    return normalize("NFKD", text).encode("ascii", errors="ignore").lower()

def matches_count(text, words):
    text_words = flatten(text).split()
    matches = {word:text_words.count(flatten(word)) for word in words}
    return matches
