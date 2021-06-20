class Player:
    def __init__(self, name):
        self.name    = name.capitalize()
        self.initial = self.name[0]
        self.points  = []

    def add_point(self,n):
        self.points.append(n)