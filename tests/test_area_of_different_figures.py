import pytest

from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


@pytest.mark.parametrize('side_a, side_b, side_c, '
                         'expected_sum_tr_cr, expected_sum_tr_sq, expected_sum_tr_rec, '
                         'expected_sum_cr_sq, expected_sum_cr_rec, expected_sum_sq_rec',
                         [
                             (
                                     4, 5, 7,
                                     60.07, 25.8, 29.8,
                                     66.27, 70.27, 36
                              ),
                             (
                                     5.2, 6.1, 7.8,
                                     100.79, 42.88, 47.56,
                                     111.99, 116.67, 58.76
                             ),
                         ])
def test_triangle_rectangle_areas_sum(side_a, side_b, side_c,
                                      expected_sum_tr_cr, expected_sum_tr_sq, expected_sum_tr_rec,
                                      expected_sum_cr_sq, expected_sum_cr_rec, expected_sum_sq_rec):
    triangle = Triangle(side_a, side_b, side_c)
    rectangle = Rectangle(side_a, side_b)
    square = Square(side_a)
    circle = Circle(side_a)
    assert triangle.add_area(circle) == expected_sum_tr_cr, \
        f'the sums of the areas of a triangle and a circle are not equal'
    assert triangle.add_area(square) == expected_sum_tr_sq, \
        f'the sums of the areas of a triangle and a square are not equal'
    assert triangle.add_area(rectangle) == expected_sum_tr_rec, \
        f'the sums of the areas of a triangle and a rectangle are not equal'
    assert circle.add_area(square) == expected_sum_cr_sq, \
        f'the sums of the areas of a circle and a square are not equal'
    assert circle.add_area(rectangle) == expected_sum_cr_rec, \
        f'the sums of the areas of a circle and a rectangle are not equal'
    assert square.add_area(rectangle) == expected_sum_sq_rec, \
        f'the sums of the areas of a square and a rectangle are not equal'
