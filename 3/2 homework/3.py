class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return f'Point(\'{self.name}\', {self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    def __le__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        else:
            return self.x <= other.x


class CheckMark:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return self.p1.name + self.p2.name + self.p3.name

    def __bool__(self):
        lst = [self.p1, self.p2, self.p3]
        f1 = (self.p3.get_y() - self.p1.get_y()) * (self.p2.get_x() - self.p1.get_x())
        f2 = (self.p2.get_y() - self.p1.get_y()) * (self.p3.get_x() - self.p1.get_x())
        f = len(set(map(lambda x: x.get_coords(), lst))) < 3 or len(set(map(lambda x: x.get_x(), lst))) == 1 or f1 == f2
        return not f

    def __eq__(self, other):
        x1 = self.p1 == other.p1 or self.p1 == other.p3
        x2 = self.p3 == other.p3 or self.p3 == other.p1
        return x1 and self.p2 == other.p2 and x2