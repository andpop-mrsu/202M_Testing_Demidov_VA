from triangle_func import get_triangle_type, IncorrectTriangleSides

try:
    print(get_triangle_type(3, 3, 3))  # equilateral
    print(get_triangle_type(4, 4, 6))  # isosceles
    print(get_triangle_type(5, 7, 9))  # nonequilateral
    print(get_triangle_type(1, 2, 3))  # IncorrectTriangleSides

except IncorrectTriangleSides as e:
    print(f"Ошибка: {e}")