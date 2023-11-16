class MyShape:
    def __init__(self, square_side, length, width, radius):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        return self.square_side ** 2

    def getRectangleArea(self):
        return self.length * self.width

    def getCircleArea(self):
        return 3.14 * self.radius ** 2


square = MyShape(5, 0, 0, 0)
rectangle = MyShape(0, 6, 4, 0)
circle = MyShape(0, 0, 0, 7)

print(f"正方形面積: {square.getSquareArea()}")
print(f"長方形面積: {rectangle.getRectangleArea()}")
print(f"圓面積: {circle.getCircleArea()}")
