import pytest

from src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, expected_area, expected_perimeter',
                         [
                             (6, 6, 6, 15.59, 18),
                             (7, 4, 6, 11.98, 17),
                             (5, 6, 8, 14.98, 19),
                             (10, 12.6436465, 8.4342, 42.09, 31.08),
                             (4.54, 6.2, 3.1, 6.73, 13.84),
                         ])
def test_positive_creation(side_a, side_b, side_c, expected_area, expected_perimeter):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == 'Triangle', 'Expected name is Triangle'
    assert triangle.get_area() == expected_area, 'Expected correct perimeter'
    assert triangle.get_perimeter() == expected_perimeter, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0, 3, 10),
                             (5, -2, 10),
                             (5, 5, 20),
                             (6, '6', 7),
                             (6, (6, 3), 8),
                             (3, [4, 3, 2], 5),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'can not create rectangle with these sides',
                             'one side is string',
                             'one side is tuple',
                             'one side is list',
                         ])
def test_negative_creation(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize('side_a1, side_b1, side_c1, side_a2, side_b2, side_c2, expected_sum',
                         [
                             (15, 11, 18, 7, 11, 9, 113.74),
                             (4.54, 6.2, 3.1, 2.41, 4.87, 2.52, 7.66),
                             (12, 16, 21, 8, 5, 7, 112.77),
                             (3.53534, 6.534534, 3.543634, 4.363, 6.5353, 7.534534, 18.62),
                             (46, 55.5, 61.3, 21.5, 43.32, 31.3, 1543.23),
                         ])
def test_triangles_areas_sum(side_a1, side_b1, side_c1, side_a2, side_b2, side_c2, expected_sum):
    triangle_1 = Triangle(side_a1, side_b1, side_c1)
    triangle_2 = Triangle(side_a2, side_b2, side_c2)
    assert triangle_1.add_area(triangle_2) == expected_sum, f'sums not equal'


@pytest.mark.parametrize('other_class',
                         [
                             10,
                             10.1,
                             [6, 5, 2],
                             'test'
                         ],
                         ids=[
                             'integer',
                             'float',
                             'list',
                             'str'
                         ])
def test_triangles_areas_sum_negative(other_class):
    triangle_1 = Triangle(6, 6, 6)
    with pytest.raises(ValueError):
        triangle_1.add_area(other_class)
