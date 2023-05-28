from src.figure import Figure


class Square(Figure):
    def __init__(self, side_a: int | float):
        self.name = 'Square'
        self.side_a = side_a
        self.check_create_square(side_a)

    def get_area(self) -> int | float:
        return round(self.side_a * self.side_a, 2)

    def get_perimeter(self) -> int | float:
        return round(self.side_a * 4, 2)

    @staticmethod
    def check_create_square(side_a: int | float):
        if not isinstance(side_a, int | float):
            raise ValueError(f'Sides must be integer. Got: side_a {type(side_a)}')

        if not side_a > 0:
            raise ValueError(f'Sides must be greater than 0. Got: {side_a}')
