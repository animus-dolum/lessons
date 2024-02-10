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
        return self.name == other.name and self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.name == other.name:
            if self.x == other.x:
                return self.y < other.y
            else:
                return self.x < other.x
        else:
            return self.name < other.name

    def __le__(self, other):
        if self.name == other.name:
            if self.x == other.x:
                return self.y <= other.y
            else:
                return self.x <= other.x
        else:
            return self.name <= other.name
