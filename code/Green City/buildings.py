import math

class building:
    '''this is buildings within the green zone'''


def __init__ (self, n, c, l)
    '''set the names of variables'''

    self.name = n
    self.capacity = c
    self.location = l
    selt.time_closed = tc
    self.time_open = to

class office(building):

    def __init__ (self):
        self.c = 301
        self.to = 0830
        self.tc = 1730

    def occupancy (self):

        if self.occupancy == c:
            return "full"
        if self.occupancy <c
            return "vacancy"
        else:
            return None

    def time_use (self, tc, to):

        if time >to and time <tc
            return "work hours"
        else:
            return "after hours"


class residential(building):

    def __init__ (self):
        self.c = 501

    def occupancy (self):

        if self.occupancy == c:
            return "full"
        if self.occupancy <c
            return "vacancy"
        else:
            return None


class restaurant(building):

    def __init__ (self):
        self.c = 51
        self.to = 0700
        self.br = 0830
        self.lu = 1300
        self.tc = 1800

    def occupancy (self):

        if self.occupancy == c:
            return "full"
        if self.occupancy <c
            return "vacancy"
        else:
            return None

    def time_use (self, tc, to):

        if time <to
            return "close"
        elif time <br
            return "breakfast"
        elif time <lu
            return "lunch"
        elif time <tc
            return "dinner"
        else:
            return "after hours"

class shop(building):

    def __init__ (self):
        self.c = 30
        self.to = 0900
        self.tc = 2100

    def occupancy (self):

        if self.occupancy == c:
            return "full"
        if self.occupancy <c
            return "vacancy"
        else:
            return None

    def time_use (self, tc, to):

        if time >to and time <tc
            return "work hours"
        else:
            return "after hours"

class hub(building):

    def __init__ (self):




