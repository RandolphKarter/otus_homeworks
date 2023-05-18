from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        self.name = 'Rectangle'
        self.side_a = side_a
        self.side_b = side_b
        self.check_create_rectangle(side_a, side_b)

    def get_area(self) -> int | float:
        return round(self.side_a * self.side_b, 2)

    def get_perimeter(self) -> int | float:
        return round((self.side_a + self.side_b) * 2, 2)

    @staticmethod
    def check_create_rectangle(side_a: int | float, side_b: int | float):
        if not (isinstance(side_a, int | float) and isinstance(side_b, int | float)):
            raise ValueError(f'Sides must be integer. Got: side_a {type(side_a)}, side_b {type(side_b)}')

        if not (side_a > 0 and side_b > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {side_a}, {side_b}')

        if side_a == side_b:
            raise ValueError(f'sides must be different. Got: {side_a}, {side_b}')
