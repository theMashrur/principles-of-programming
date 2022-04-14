from math import sqrt

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, p):
        c = self.centre
        dist = sqrt((c[0]-p[0])**2 + (c[1]-p[1])**2)
        if dist < self.radius:
            return True
        return False