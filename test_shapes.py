from classes import (
    Rectangle,
    Square,
    Triangle,
    Rhombus,
    Trapezoid,
    Sphere,
    Parallelepiped,
    Cube,
    Pyramid,
    Cylinder,
    Cone
)


def test_rectangle_perimeter():
    rectangle = Rectangle(20, 30)
    assert rectangle.perimeter() == 100

def test_rectangle_area():
    rectangle = Rectangle(20, 30)
    assert rectangle.area() == 600

def test_square_perimeter():
    square = Square(25)
    assert square.perimeter() == 100

def test_square_area():
    square = Square(25)
    assert square.area() == 625

def test_triangle_perimeter():
    triangle = Triangle(20, 30, 40)
    assert triangle.perimeter() == 90

def test_triangle_area():
    triangle = Triangle(20, 30, 40)
    assert triangle.area() == 290.47

def test_rhombus_perimeter():
    rhombus = Rhombus(20, 30)
    assert rhombus.perimeter() == 72.11

def test_rhombus_area():
    rhombus = Rhombus(20, 30)
    assert rhombus.area() == 300

def test_trapezoid_perimeter():
    trapezoid = Trapezoid(50, 30, 20, 10, 15)
    assert trapezoid.perimeter() == 110

def test_trapezoid_area():
    trapezoid = Trapezoid(50, 30, 20, 10, 15)
    assert trapezoid.area() == 600

def test_sphere_surface_area():
    sphere = Sphere(10)
    assert sphere.surface_area() == 1256.64

def test_sphere_volume():
    sphere = Sphere(10)
    assert sphere.volume() == 4188.79

def test_parallelepiped_surface_area():
    parallelepiped = Parallelepiped(20, 30, 10)
    assert parallelepiped.surface_area() ==  2200

def test_parallelepiped_volume():
    parallelepiped = Parallelepiped(20, 30, 10)
    assert parallelepiped.volume() == 6000

def test_cube_surface_area():
    cube = Cube(20)
    assert cube.surface_area() ==  2400

def test_cube_volume():
    cube = Cube(20)
    assert cube.volume() == 8000

def test_pyramid_surface_area():
    pyramid = Pyramid(30, 20, 5)
    assert pyramid.surface_area() == 1652.16

def test_pyramid_volume():
    pyramid = Pyramid(30, 20, 5)
    assert pyramid.volume() == 967.68

def test_cylinder_surface_area():
    cylinder = Cylinder(10, 20)
    assert cylinder.surface_area() == 1884.96

def test_cylinder_volume():
    cylinder = Cylinder(10, 20)
    assert cylinder.volume() == 6283.19

def test_cone_surface_area():
    cone = Cone(10, 20)
    assert cone.surface_area() ==  942.48

def test_cone_volume():
    cone = Cone(10, 20)
    assert cone.volume() ==  1813.75
