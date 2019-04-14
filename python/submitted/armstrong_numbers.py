def is_armstrong(number):
    """
    True if the input is a number that is the sum of its own digits 
    each raised to the power of the number of digits.
    """
    numstring = str(number)
    pow = len(numstring)
    return number == sum(int(c)**pow for c in numstring)
