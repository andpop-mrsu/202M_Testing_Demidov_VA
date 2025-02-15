import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):
    """
    Тестирование функции get_triangle_type.
    """

    def test_equilateral_triangle(self):
        """Тест для равностороннего треугольника."""
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles_triangle(self):
        """Тест для равнобедренного треугольника."""
        self.assertEqual(get_triangle_type(4, 4, 6), "isosceles")
        self.assertEqual(get_triangle_type(5, 7, 7), "isosceles")

    def test_nonequilateral_triangle(self):
        """Тест для разностороннего треугольника."""
        self.assertEqual(get_triangle_type(5, 7, 9), "nonequilateral")

    def test_invalid_sides_zero_or_negative(self):
        """Тест на некорректные стороны (нули или отрицательные значения)."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 3, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 3, 3)

    def test_invalid_triangle_inequality(self):
        """Тест на нарушение неравенства треугольника."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 3, 7)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

if __name__ == "__main__":
    unittest.main()