from string import ascii_uppercase as abc
from string import digits
from random import choices as choices

class Robot(object):

    def __init__(self):
        self.name = ''
        self.names = set()
        self.reset()
        return

    def reset(self):
        while True:
            self.name = ''.join(choices(abc, k=2) + choices(digits,k=3))
            if self.name not in self.names:
                break
        self.names.add(self.name)
        return
