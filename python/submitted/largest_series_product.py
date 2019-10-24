import numpy as np

def largest_product(series, size):
    """
    Given a string of digits, calculate the largest product for any contiguous
    substring of digits of length n.
    """
    series_length = len(series)
    if size > series_length:
        raise ValueError("Size must not be larger than series length.")
    if size < 0:
        raise ValueError("Size must not be less than 0.")

    series_list = [int(c) for c in series if c.isdigit()]
    if len(series_list) < series_length:
        raise ValueError("All characters in series must be digits.")

    series_slices = np.array([
            series_list[i:i+size] 
            for i in range(series_length - size + 1)
            ])
    
    return np.max(np.prod(series_slices, axis=1))