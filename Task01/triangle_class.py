class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass

class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Длины сторон должны быть положительными числами.")
        
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise IncorrectTriangleSides("Треугольник с такими сторонами невозможен.")
        
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        """
        Возвращает тип треугольника: "equilateral", "isosceles", "nonequilateral".
        """
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        """
        Возвращает периметр треугольника.
        """
        return self.a + self.b + self.c