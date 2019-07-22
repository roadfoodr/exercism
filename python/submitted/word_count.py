import re
from collections import Counter

def count_words(sentence):
    '''
    Given a phrase, count the occurrences of each word in that phrase.
    Surrounding quotes should not be considered part of a word, but
    apostrophes for contractions or possessives should be.
    '''
    words = re.sub('[^a-z0-9\']', ' ', sentence.lower()).split()
    words = [
            w[1:-1] if w.startswith("'") and w.endswith("'") else w
            for w in words
            ]
    
    return Counter(words)
