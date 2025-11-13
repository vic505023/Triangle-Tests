# Вычисляет площадь треугольника по формуле Герона
def triangle_area(a, b, c):
    # Проверка валидности входных данных
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError("Стороны должны быть числами")
        if x <= 0:
            raise ValueError("Стороны должны быть > 0")
    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Нарушено неравенство треугольника")

    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Вычисляет периметр треугольника
def triangle_perimeter(a, b, c):
    # Проверка валидности входных данных
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError("Стороны должны быть числами")
        if x <= 0:
            raise ValueError("Стороны должны быть > 0")
    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Нарушено неравенство треугольника")

    return a + b + c