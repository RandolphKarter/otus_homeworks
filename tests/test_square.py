import pytest

from src.square import Square


@pytest.mark.parametrize('side_a, expected_area, expected_perimeter',
                         [
                             (20, 400, 80),
                             (12.8, 163.84, 51.2),
                             (7.565, 57.23, 30.26),
                             (35, 1225, 140),
                             (21, 441, 84),
                         ])
def test_positive_creation(side_a, expected_area, expected_perimeter):
    rectangle = Square(side_a)
    assert rectangle.name == 'Square', 'Expected name is Square'
    assert rectangle.get_area() == expected_area, 'Expected correct perimeter'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct area'


@pytest.mark.parametrize('side_a',
                         [
                             0,
                             -2,
                             '6',
                             (6, 5),
                             [3, 5, 2],
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'one side is string',
                             'one side is tuple',
                             'one side is list',
                         ])
def test_negative_creation(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize('side_a1, side_a2, expected_sum',
                         [
                             (17.56, 13, 477.35),
                             (2.5, 12.53, 163.25),
                             (14.12, 6.66, 243.73),
                             (5, 9, 106),
                             (72, 18.44323, 5524.15),
                         ])
def test_rectangle_areas_sum(side_a1, side_a2, expected_sum):
    square_1 = Square(side_a1)
    square_2 = Square(side_a2)
    assert square_1.add_area(square_2) == expected_sum, f'sums not equal'


@pytest.mark.parametrize('other_class',
                         [
                             15,
                             3.322,
                             [7, 4],
                             'test'
                         ],
                         ids=[
                             'integer',
                             'float',
                             'list',
                             'str'
                         ])
def test_rectangle_areas_sum_negative(other_class):
    square_1 = Square(6)
    with pytest.raises(ValueError):
        square_1.add_area(other_class)
