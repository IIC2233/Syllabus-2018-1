class MoveMarioEvent:
    def __init__(self, side):
        self.side = side

class MoveEvent:
    def __init__(self, x, y):
        self.x = x
        self.y = y