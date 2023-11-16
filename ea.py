class MyShape:
    def __init__(self, square_side, rectangle_length, rectangle_width, radius):
        self.square_side = square_side
        self.rectangle_length = rectangle_length
        self.rectangle_width = rectangle_width
        self.radius = radius

    def getSquareArea(self):
        return self.square_side ** 2

    def getRectangleArea(self):
        return self.rectangle_length * self.rectangle_width

    def getCircleArea(self):
        return 3.14 * self.radius ** 2

# Example usage
shape = MyShape(5, 10, 20, 7)
print(shape.getSquareArea()) # Output: 25
print(shape.getRectangleArea()) # Output: 200
print(shape.getCircleArea()) # Output: 1538.86