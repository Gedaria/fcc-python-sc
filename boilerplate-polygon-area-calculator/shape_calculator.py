class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "".join("*" * self.width + "\n" for _ in range(self.height))

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self, shape):
        # may be wrong, because it is indicated that
        # there should be no rotation
        # so, a 3x1 rectangle will not fit in a 1x4 rectangle
        inserted_shape = shape.height * shape.width
        my_shape = self.get_area()
        return my_shape // inserted_shape


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
