def find_anagrams(word, candidates):
    '''
    Given a word and a list of candidate words, return a list of those
    unique candidates which are anagrams of the word.
    '''
    lower_word = word.lower()
    base_letters = sorted(lower_word)
    
    # comparing length as an opportunity for early termination
    return [c for c in set(candidates)
            if len(c) == len(word) 
            and c.lower() != lower_word
            and sorted(c.lower()) == base_letters
            ]