import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
def test_triangle_creation():
    """Проверка создания треугольника с корректными сторонами."""
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5

def test_equilateral_triangle():
    """Проверка определения равностороннего треугольника."""
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == "equilateral"

def test_isosceles_triangle():
    """Проверка определения равнобедренного треугольника."""
    triangle = Triangle(4, 4, 6)
    assert triangle.triangle_type() == "isosceles"

def test_nonequilateral_triangle():
    """Проверка определения разностороннего треугольника."""
    triangle = Triangle(5, 7, 9)
    assert triangle.triangle_type() == "nonequilateral"

def test_perimeter():
    """Проверка расчета периметра треугольника."""
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12

# Негативные тесты
def test_invalid_sides_zero_or_negative():
    """Проверка обработки нулевых или отрицательных сторон."""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 3, 3)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 3, 3)

def test_invalid_triangle_inequality():
    """Проверка обработки нарушения неравенства треугольника."""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 3, 7)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)