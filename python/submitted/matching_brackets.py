def is_paired(input_string):
    '''
    Given a string containing brackets [], braces {}, parentheses (), or any 
    combination thereof, verify that any and all pairs are matched and nested 
    correctly.
    '''
    matches = {']':'[', '}':'{', ')':'('}
    lefts = matches.values()
    rights = matches.keys()
    stack = []
    
    for c in input_string:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack[-1] != matches[c]:
                return False
            else:
                stack.pop()
    
    return not stack
