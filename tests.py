import unittest
from triangle import triangle_area, triangle_perimeter

class TriangleTestCase(unittest.TestCase):
    # Позитивные тесты
    def test_equilateral_area(self):
        # Площадь равностороннего треугольника со сторонами 3
        res = triangle_area(3, 3, 3)
        self.assertAlmostEqual(res, 3.89711, places=5)

    def test_equilateral_perimeter(self):
        # Периметр равностороннего треугольника со сторонами 3
        res = triangle_perimeter(3, 3, 3)
        self.assertEqual(res, 9)

    def test_isosceles_area(self):
        # Площадь равнобедренного треугольника со сторонами 3, 3, 2
        res = triangle_area(3, 3, 2)
        self.assertAlmostEqual(res, 2.82843, places=5)

    def test_isosceles_perimeter(self):
        # Периметр равнобедренного треугольника со сторонами 3, 3, 2
        res = triangle_perimeter(3, 3, 2)
        self.assertEqual(res, 8)

    # Негативные тесты
    def test_negative_side_raises(self):
        # Ошибка при отрицательной стороне (a < 0) должна вызывать ValueError
        with self.assertRaises(ValueError):
            triangle_area(-1, 2, 3)

    def test_zero_side_raises(self):
        # Ошибка при нулевой стороне (a == 0) должна вызывать ValueError
        with self.assertRaises(ValueError):
            triangle_perimeter(0, 2, 3)

    def test_triangle_inequality_raises(self):
        # Нарушение неравенства треугольника (1 + 2 <= 99) — ValueError
        with self.assertRaises(ValueError):
            triangle_area(1, 2, 99)

    def test_type_error_raises(self):
        # Неверный тип аргумента (строка вместо числа) — TypeError
        with self.assertRaises(TypeError):
            triangle_perimeter("3", 4, 5)