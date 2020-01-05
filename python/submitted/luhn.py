import numpy as np

class Luhn:
    '''
    Given a string, provide a method to determine whether it represents a 
    number that is valid per the Luhn formula.  Strings containing characters 
    other than digits and whitespace are invalid.
    '''
    def __init__(self, card_num):
        self.card_num = card_num
        
    def valid(self):
        card_digits = ''.join(self.card_num.split())
        
        if not card_digits.isnumeric():
            return False
        elif len(card_digits) < 2:
            return False
        else:
            card_digits = np.array(list(card_digits), dtype='int32')
            # Step 1: double every second digit, starting from the right
            card_digits[-2::-2] = card_digits[-2::-2] * 2
            # Step 2: subtract 9 from any numbers that are now greater than 9
            card_digits[card_digits > 9] = card_digits[card_digits > 9] - 9
            return bool((np.sum(card_digits) % 10) == 0)
