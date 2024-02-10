class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return self.name + "({}, {})".format(self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def get_coords(self):
        return (self.x, self.y)
    

class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        super().__init__(name, x, y)
        self.rgb = rgb

    def get_color(self):
        return self.rgb

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, (255 - self.rgb[0], 255 - self.rgb[1], 255 - self.rgb[2]))
