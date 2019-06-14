def square_of_sum(number):
    # https://en.wikipedia.org/wiki/Triangular_number
    return round((number * (number+1) / 2) ** 2)


def sum_of_squares(number):
    # https://en.wikipedia.org/wiki/Square_pyramidal_number
    return round((number**3 / 3) + (number**2 / 2) + (number / 6))


def difference_of_squares(number):
    '''
    Find the difference between the square of the sum and the sum of the 
    squares of the first N natural numbers.
    '''
    if number < 0:
        raise ValueError(f'number {number} may not be negative.')
        
    return square_of_sum(number) - sum_of_squares(number)
