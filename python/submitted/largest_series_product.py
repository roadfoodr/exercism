import numpy as np

def rolling_window(a, window):
    # from https://rigtorp.se/2011/01/01/rolling-statistics-numpy.html
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def largest_product(series, size):
    """
    Given a string of digits, calculate the largest product for any contiguous
    substring of digits of length n.
    """
    if size > len(series):
        raise ValueError("Size must not be larger than series length.")
    if size < 0:
        raise ValueError("Size must not be less than 0.")

    try:
        series_array = np.fromiter(series, dtype='int64')
    except ValueError:
        raise ValueError("All characters in series must be digits.")
    
    return np.max(np.prod(rolling_window(series_array, size), axis=1))