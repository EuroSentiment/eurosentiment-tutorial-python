# encoding: utf-8
from unicodedata import normalize

def flatten(text):
    return normalize("NFKD", text.decode('utf-8', errors="ignore")).encode("ascii", errors="ignore").lower()

def matches_count(text, words):
    text_words = flatten(text).split()
    print text_words
    matches = {word:text_words.count(flatten(word)) for word in words}
    return matches
