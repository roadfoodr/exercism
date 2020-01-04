MIN_PER_HR = 60
HR_PER_DAY = 24
MIN_PER_DAY = MIN_PER_HR * HR_PER_DAY

class Clock:
    '''
    Class that implements a 24-hour clock without dates.  Addition and
    subtraction of minutes are supported, with overflows/underflows "rolling 
    over" into the 24-hour timeframe of a day.
    '''
    
    def __init__(self, hour=0, minute=0):
        self.total_minutes = 0
        self.add_minutes(minute)
        self.add_minutes(MIN_PER_HR * hour)

    def add_minutes(self, minutes):
        self.total_minutes += minutes
        self.total_minutes %= MIN_PER_DAY
        return self

    def __repr__(self):
        hours, minutes = divmod(self.total_minutes, MIN_PER_HR)
        return f'{hours:02}:{minutes:02}'

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        new_clock = Clock(0, self.total_minutes)
        return new_clock.add_minutes(minutes) 

    def __sub__(self, minutes):
        return self + -minutes