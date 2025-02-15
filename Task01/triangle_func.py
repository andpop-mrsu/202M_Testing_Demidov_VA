# triangle_func.py

class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
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


