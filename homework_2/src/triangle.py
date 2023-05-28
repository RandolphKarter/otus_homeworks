import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        self.name = 'Triangle'
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.check_create_triangle(side_a, side_b, side_c)

    def get_area(self) -> int | float:
        half_per = self.get_perimeter() / 2
        area = math.sqrt(half_per * (half_per - self.side_a) * (half_per - self.side_b) * (half_per - self.side_c))
        return round(area, 2)

    def get_perimeter(self) -> int | float:
        return round(self.side_a + self.side_b + self.side_c, 2)

    @staticmethod
    def check_create_triangle(side_a: int | float, side_b: int | float, side_c: int | float):
        if not (isinstance(side_a, int | float) and
                isinstance(side_b, int | float) and
                isinstance(side_c, int | float)):
            raise ValueError(f'Sides must be integer. Got: side_a {type(side_a)}, '
                             f'side_b {type(side_b)}, side_c {type(side_c)}')

        if not (side_a > 0 and side_b > 0 and side_c > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {side_a}, {side_b}, {side_c}')

        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError(f'Unable to create triangle with sides: {side_a} {side_b} {side_c}')
