def is_isogram(string):
    '''
    Determine if a word or phrase is an isogram (a word or phrase without a 
    repeating letter, irrespective of case).  Non-alphabetic characters are
    not considered.
    '''
    letters = ''.join(c for c in string if c.isalpha()).lower()
    return len(set(letters)) == len(letters)
