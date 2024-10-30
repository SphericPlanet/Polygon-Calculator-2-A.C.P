class Polygon:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

class Square(Polygon):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def calculate_area(self):
        return 0.5 * self.__base * self.__height

if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Square(6),
        Triangle(8, 4)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area:", shape.calculate_area())
