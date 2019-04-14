import re

class Phone(object):
    """
    Canonify a phone number supplied as a string.  Only the numeric digits
    are placed into self.number.  ValueError is raised if the resulting number 
    does not:
        - contain 10 digits
        - area code begins with a digit from 2-9
        - exchange code begins with a digit from 2-9
    """
    def __init__(self, phone_number):
        self.number = "".join(re.findall("\d+", phone_number))
        self.number = re.sub(r"^[0-1]+", "", self.number)
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.validate_number()
        return
    
    def validate_number(self):
        if len(self.number) != 10:
            raise ValueError("Phone number must have 10 numeric digits \
                             and area code may not begin with zero or one")      
        if self.exchange_code[0] in "01":
            raise ValueError("Exchange code may not begin with zero or one")
        return
        
    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"
