from string import ascii_uppercase as abc
from string import digits
from random import choices as choices

class Robot(object):
    """
    A class for robots with unique names of the form 2 uppercase letters
    followed by 3 digits.  Names will be unique among instances of the class.
    """
    names = set()

    def __init__(self):
        self.name = ''
        self.reset()
        return

    def reset(self):
        """ Assign a new, unique name to this instance of the Robot class. """
        while True:
            self.name = ''.join(choices(abc, k=2) + choices(digits,k=3))
            if self.name not in self.names:
                break
        self.names.add(self.name)
        return
