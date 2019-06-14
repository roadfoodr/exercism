def slices(series, length):
    '''
    Given a string of characters, return a list of all the contiguous substrings
    of specified length in that string in the order that they appear.
    '''
    if not series:
        raise ValueError('Series must be of nonzero length.')
    if length < 1 or length > len(series):
        raise ValueError(f'Length must be greater than zero and less than or '
                         f'equal to the length of series.')
    
    last_start = len(series) - length + 1
    return [series[i : i+length] for i in range(last_start)]