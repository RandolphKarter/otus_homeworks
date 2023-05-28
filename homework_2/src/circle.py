import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        self.name = 'Circle'
        self.radius = radius
        self.check_create_circle(radius)

    def get_area(self) -> int | float:
        return round(math.pi * (self.radius ** 2), 2)

    def get_perimeter(self) -> int | float:
        return round(2 * math.pi * self.radius, 2)

    @staticmethod
    def check_create_circle(radius: int | float):
        if not isinstance(radius, int | float):
            raise ValueError(f'Sides must be integer. Got: side_a {type(radius)}')

        if not radius > 0:
            raise ValueError(f'Sides must be greater than 0. Got: {radius}')
