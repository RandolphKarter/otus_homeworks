import pytest

from src.circle import Circle


@pytest.mark.parametrize('radius, expected_area, expected_perimeter',
                         [
                             (66, 13684.78, 414.69),
                             (13.1, 539.13, 82.31),
                             (2.532, 20.14, 15.91),
                             (4, 50.27, 25.13),
                             (13, 530.93, 81.68)
                         ])
def test_positive_creation(radius, expected_area, expected_perimeter):
    rectangle = Circle(radius)
    assert rectangle.name == 'Circle', 'Expected name is Circle'
    assert rectangle.get_area() == expected_area, 'Expected correct perimeter'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct area'


@pytest.mark.parametrize('radius',
                         [
                             0,
                             -6,
                             '6',
                             (2, 71),
                             [4, 5.5, 1],
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'one side is string',
                             'one side is tuple',
                             'one side is list',
                         ])
def test_negative_creation(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize('radius_1, radius_2, expected_sum',
                         [
                             (21, 8.42, 1608.17),
                             (2.5, 12.53, 512.86),
                             (14.12, 6.66, 765.7),
                             (5, 9, 333.01),
                             (72, 18.44323, 17354.64),
                         ])
def test_rectangle_areas_sum(radius_1, radius_2, expected_sum):
    square_1 = Circle(radius_1)
    square_2 = Circle(radius_2)
    assert square_1.add_area(square_2) == expected_sum, f'sums not equal'


@pytest.mark.parametrize('other_class',
                         [2,
                          3.214,
                          [2, 5],
                          'test'
                          ],
                         ids=[
                             'integer',
                             'float',
                             'list',
                             'str'
                         ])
def test_rectangle_areas_sum_negative(other_class):
    square_1 = Circle(6)
    with pytest.raises(ValueError):
        square_1.add_area(other_class)
