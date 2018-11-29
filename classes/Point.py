class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def sub(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def mul(self, other):
        return Point(self.x * other, self.y * other)
