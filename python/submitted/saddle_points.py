import numpy as np

def saddle_points(matrix):
    '''
    Given a 2-d matrix, return a list of dicts of coordinates of all saddle
    points in the matrix.  A saddle point (for this exercise) is a point that 
    is greater than or equal to every element in its row and less than or equal
    to every element in its column.
    '''
    if not matrix:
        return [dict()]
    if len({len(row) for row in matrix}) != 1:
        raise ValueError('All rows of matrix must be the same length.')

    results = []
    matrix = np.asarray(matrix)
    numrows, numcols = matrix.shape
    
    row_maxes = np.repeat(
            np.amax(matrix, axis=1, keepdims=True),
            numcols,
            axis=1)
    
    col_mins = np.repeat(
            np.amin(matrix, axis=0, keepdims=True),
            numrows,
            axis=0)
    
    coords = np.where(row_maxes == col_mins)
    for coord in zip(coords[0], coords[1]):
        results.append({'row': coord[0] + 1, 'column': coord[1] + 1})

    return results if results else [dict()]
