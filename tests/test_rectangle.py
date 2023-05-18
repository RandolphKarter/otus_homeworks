import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, expected_area, expected_perimeter',
                         [
                             (10, 2, 20, 24),
                             (15, 8, 120, 46),
                             (7, 5, 35, 24),
                             (3.2, 7.46575, 23.89, 21.33),
                             (5.43, 8.544, 46.39, 27.95),
                         ])
def test_positive_creation(side_a, side_b, expected_area, expected_perimeter):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.get_area() == expected_area, 'Expected correct perimeter'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b',
                         [
                             (5, 0),
                             (-6, 10),
                             (12, 12),
                             (6, '7'),
                             (6, (6, 5)),
                             (6, [3, 5, 2]),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'sides are equal',
                             'one side is string',
                             'one side is tuple',
                             'one side is list',
                         ])
def test_negative_creation(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize('side_a1, side_b1, side_a2, side_b2, expected_sum',
                         [
                             (12.56, 25.2, 6, 12, 388.51),
                             (6, 5.2, 3.3, 12, 70.8),
                             (12, 14, 8, 5, 208),
                             (4.523532, 6.4234, 8.5324234, 5.5435345, 76.36),
                             (534, 5353, 3452, 52442, 183888286),
                         ])
def test_rectangle_areas_sum(side_a1, side_b1, side_a2, side_b2, expected_sum):
    rectangle_1 = Rectangle(side_a1, side_b1)
    rectangle_2 = Rectangle(side_a2, side_b2)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'sums not equal'


@pytest.mark.parametrize('other_class',
                         [
                             63,
                             5.2,
                             [6, 5, 4],
                             'test'
                         ],
                         ids=[
                             'integer',
                             'float',
                             'list',
                             'str'
                         ])
def test_rectangle_areas_sum_negative(other_class):
    triangle_1 = Rectangle(6, 12)
    with pytest.raises(ValueError):
        triangle_1.add_area(other_class)
