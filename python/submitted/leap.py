def leap_year(year: int) -> bool:
    '''
    Given an integer, return whether it represents a leap year.
    '''

    if not isinstance(year, int):
        raise TypeError("The input value 'year' must be an integer.")
    
    if year % 4 != 0:
        return False
    if (year % 100) == 0 and (year % 400) != 0:
        return False
    return True
