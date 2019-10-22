import re

def abbreviate(phrase):
    """
    Convert a phrase to its acronym.  Punctuation characters other than 
    apostrophes are considered to be word separators.
    """
    words = re.sub('[^A-Z0-9\']', ' ', phrase.upper()).split()
    return ''.join((word[0] for word in words))