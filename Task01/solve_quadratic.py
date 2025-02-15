import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "Нет решений" if c != 0 else "Бесконечно много решений"
        else:
            x = -c / b
            return [x]
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return sorted([x1, x2])
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return "Нет вещественных корней"

print(solve_quadratic(1, -4, 4))