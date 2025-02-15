
class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
    Примеры использования:

    >>> get_triangle_type(3, 3, 3)
    'equilateral'

    >>> get_triangle_type(4, 4, 6)
    'isosceles'

    >>> get_triangle_type(5, 7, 9)
    'nonequilateral'

    >>> get_triangle_type(0, 3, 3)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Длины сторон должны быть положительными числами.

    >>> get_triangle_type(-1, 3, 3)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Длины сторон должны быть положительными числами.

    >>> get_triangle_type(3, 3, 7)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Треугольник с такими сторонами невозможен.

    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    triangle_func.IncorrectTriangleSides: Треугольник с такими сторонами невозможен.
    """
    # Проверка на положительность сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Длины сторон должны быть положительными числами.")
    
    # Проверка условия существования треугольника
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise IncorrectTriangleSides("Треугольник с такими сторонами невозможен.")
    
    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"

