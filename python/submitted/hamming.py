def distance(strand_a, strand_b):
    '''
    Calculates the Hamming Distance (number of elements in same index 
    location, but with different values) between two iterators.
    '''
    if len(strand_a) != len(strand_b):
        raise ValueError("strand_a must have the same length as strand_b")
    
    return sum(1 for i,c in enumerate(strand_a) 
               if strand_a[i] != strand_b[i])
