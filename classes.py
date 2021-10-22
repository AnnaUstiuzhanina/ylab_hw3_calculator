import abc
from math import sqrt, pi, tan
from decorators import round_decorator


class Shape:
    """
        Прототип фигуры
    """

    @classmethod
    def get_print_data(cls) -> dict:
        parent_data = {}
        if not cls is Shape:
            parent_data = cls.__bases__[0].get_print_data()
        
        if hasattr(cls, 'print_data'):
            result = {}
            result.update(cls.print_data)
            result.update(parent_data)
            return result
        
        return parent_data


class Shape_2D(Shape):
    """
        Прототип плоской фигуры
    """
    print_data = {
        'perimeter': 'Периметр',
        'area': 'Площадь',
    }

    @abc.abstractmethod
    def perimeter(self) -> float:
        """Периметр фигуры."""
        pass

    @abc.abstractmethod
    def area(self) -> float:
        """Площадь фигуры."""
        pass


class Rectangle(Shape_2D):
    """Прямоугольник."""

    title = 'Прямоугольник'
    params = {
        'a': 'сторона A',
        'b': 'сторона B',
    }
    print_data = {
        'diag': 'Диагональ',
    }

    def __init__(self, a, b):
        super().__init__()
        self.__a, self.__b = a, b

    @round_decorator(2)
    def perimeter(self) -> float:
        """Периметр прямоугольника."""
        return (self.__a + self.__b) * 2

    @round_decorator(2)
    def area(self):
        """Площадь прямоугольника."""
        return self.__a * self.__b
    
    @round_decorator(2)
    def diag(self):
        """Диагональ прямоугольника."""
        return sqrt(pow(self.__a, 2) + pow(self.__b, 2))


class Square(Rectangle):
    """Квадрат."""

    title = 'Квадрат'
    params = {
        'a': 'сторона A',
    }

    def __init__(self, a):
        super().__init__(a, a)


class Triangle(Shape_2D):
    """Треугольник."""

    title = 'Треугольник'
    params = {
        'a': 'сторона A',
        'b': 'сторона B',
        'c': 'сторона C',
    }
    print_data = {
        'rad': 'Радиус вписанной окружности',
    }

    def __init__(self, a, b, c):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c

    @round_decorator(2)
    def perimeter(self) -> float:
        """Периметр треугольника."""
        return self.__a + self.__b + self.__c
    
    @round_decorator(2)
    def area(self) -> float:
        """Площадь треугольника."""
        p = self.perimeter() / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
    
    @round_decorator(2)
    def rad(self) -> float:
        """Радиус вписанной окружности."""
        p = self.perimeter()
        return sqrt(((p - self.__a) * (p - self.__b) * (p - self.__c)) / p)


class Rhombus(Shape_2D):
    """Ромб"""

    title = 'Ромб'
    params = {
        'd1': 'Диагональ 1',
        'd2': 'Диагональ 2',
    }

    def __init__(self, d1, d2):
        super().__init__()
        self.__d1 = d1
        self.__d2 = d2

    @round_decorator(2)
    def perimeter(self) -> float:
        """Периметр ромба."""
        return sqrt(self.__d1 ** 2 + self.__d2 ** 2) * 2
    
    @round_decorator(2)
    def area(self) -> float:
        """Площадь ромба."""
        return (self.__d1 * self.__d2) / 2


class Trapezoid(Shape_2D):
    """Трапеция"""

    title = 'Трапеция'
    params = {
        'a': 'Сторона A (нижняя)',
        'b': 'Сторона B (верхняя)',
        'c': 'Сторона C',
        'd': 'Сторона D',
        'h': 'Высота H',
    }
    print_data = {
        'diags': 'Диагонали',
    }

    def __init__(self, a, b, c, d, h):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__h = h

    @round_decorator(2)
    def perimeter(self) -> float:
        """Периметр трапеции."""
        return self.__a + self.__b + self.__c + self.__d
    
    @round_decorator(2)
    def area(self) -> float:
        """Площадь трапеции."""
        return (self.__a + self.__b) / 2 * self.__h
    
    @round_decorator(2)
    def get_d1(self) -> float:
        """Первая диагональ."""
        try:
            return sqrt(pow(self.__d, 2) + self.__a * self.__b - self.__a * (pow(self.__d, 2) - pow(self.__c, 2)) / (self.__a - self.__b))
        except ValueError:
            return 0
    
    @round_decorator(2)
    def get_d2(self) -> float:
        """Вторая диагональ."""
        try:
            return sqrt(pow(self.__c, 2) + self.__a * self.__b - self.__a * (pow(self.__c, 2) - pow(self.__d, 2)) / (self.__a - self.__b))
        except ValueError:
            return 0
    
    def diags(self) -> tuple:
        """Диагонали трапеции."""
        return (self.get_d1(), self.get_d2())


class Shape_3D(Shape):
    """
        Прототип объемной фигуры фигуры
    """

    print_data = {
        'surface_area': 'Площадь поверхности',
        'volume': 'Объем',
    }

    @abc.abstractmethod
    def surface_area(self) -> float:
        """Площадь поверхности фигуры."""
        pass

    @abc.abstractmethod
    def volume(self) -> float:
        """Объем фигуры."""
        pass


class Sphere(Shape_3D):
    """Сфера"""

    title ='Сфера'
    params = {
        'r': 'Радиус',
    }
    print_data = {
        'diam': 'Диаметр',
    }

    def __init__(self, r):
        super().__init__()
        self.__r = r

    @round_decorator(2)
    def surface_area(self) -> float:
        """Площадь поверхности сферы."""
        return 4 * pi * self.__r ** 2
    
    @round_decorator(2)
    def volume(self) -> float:
        """Объем сферы."""
        return 4 * pi * self.__r ** 3 / 3
    
    @round_decorator(2)
    def diam(self) -> float:
        """Диаметр сферы."""
        return self.__r * 2


class Parallelepiped(Shape_3D):
    """Параллелепипед."""

    title = 'Параллелепипед'
    params = {
        'a': 'Сторона A',
        'b': 'Сторона B',
        'h': 'Высота'
    }
    print_data = {
        'diag': 'Диагональ',
    }

    def __init__(self, a, b, h):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__h = h

    @round_decorator(2)
    def surface_area(self):
        """Площадь поверхности параллелепипеда."""
        return 2 * (self.__a * self.__b + self.__a * self.__h + self.__b * self.__h)
    
    @round_decorator(2)
    def volume(self):
        """Объем параллелепипеда."""
        return self.__a * self.__b * self.__h
    
    @round_decorator(2)
    def diag(self):
        """Диагональ параллелепипеда."""
        return sqrt(pow(self.__a, 2) + pow(self.__b, 2) + pow(self.__h, 2))


class Cube(Parallelepiped):
    """Куб."""

    title ='Куб'
    params = {
        'a': 'Сторона A',
    }

    def __init__(self, a):
        super().__init__(a, a, a)


class Pyramid(Shape_3D):
    """Пирамида."""

    title ='Пирамида'
    params = {
        'a': 'Сторона',
        'h': 'Высота',
        'n': 'Количество сторон',
    }

    def __init__(self, a, h, n):
        super().__init__()
        self.__a = a
        self.__h = h
        self.__n = n

    @round_decorator(2)
    def surface_area(self) -> float:
        """Площадь поверхности пирамиды."""
        segment = self.__a / (2 * tan(180 / self.__n))
        return (self.__n * self.__a) * (segment + sqrt(pow(self.__h, 2) + pow(segment, 2))) / 2
    
    @round_decorator(2)
    def volume(self) -> float:
        """Объем пирамиды."""
        return (self.__n * self.__a ** 2 * self.__h) / (12 * tan(180 / self.__n))


class Cylinder(Shape_3D):
    """Цилиндр"""

    title = 'Цилиндр'
    params = {
        'r': 'Радиус',
        'h': 'Высота',
    }

    def __init__(self, r, h):
        super().__init__()
        self.__r, self.__h = r, h

    @round_decorator(2)
    def surface_area(self) -> float:
        """Площадь поверхности цилиндра."""
        return 2 * pi * self.__r * (self.__r + self.__h)
    
    @round_decorator(2)
    def volume(self) -> float:
        """Объем цилиндра."""
        return pi * self.__r ** 2 * self.__h


class Cone(Shape_3D):
    """Конус"""

    title = 'Конус'
    params = {
        'r': 'Радиус',
        'l': 'Длина стороны',
    }

    def __init__(self, r, l):
        super().__init__()
        self.__r, self.__l = r, l

    @round_decorator(2)
    def surface_height(self) -> float:
        """Высота конуса."""
        return sqrt(pow(self.__l, 2) - pow(self.__r, 2))

    @round_decorator(2)
    def surface_area(self) -> float:
        """Площадь поверхности конуса."""
        return pi * self.__r * (self.__r + self.__l)
    
    @round_decorator(2)
    def volume(self) -> float:
        """Объем конуса."""
        h = self.surface_height()
        return pi * self.__r ** 2 * h / 3
