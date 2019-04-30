def raindrops(number):
    '''
    Converts a number to a string, the contents of which depend on the number's 
    factors.  If the number contains none of the factors, the string version
    of the number is returned.
    '''
    subs = [(3,"Pling"), (5,"Plang"), (7,"Plong")]

    s = "".join([sub for fact,sub in subs if number % fact == 0])
    return s if s else str(number)