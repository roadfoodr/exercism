def is_pangram(sentence):
    from string import ascii_lowercase as abc
    
    letset = {c for c in sentence.lower() if c.isalpha()}
    return (letset == set(abc))
