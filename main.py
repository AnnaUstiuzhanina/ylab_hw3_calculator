from classes import (
    Parallelepiped,
    Rectangle,
    Square,
    Triangle,
    Rhombus,
    Trapezoid,
    Sphere,
    Cube,
    Pyramid,
    Cylinder,
    Cone,
)

ALLOW_SHAPES = {
    1: Rectangle,
    2: Square,
    3: Triangle,
    4: Rhombus,
    5: Trapezoid,
    6: Sphere,
    7: Parallelepiped,
    8: Cube,
    9: Pyramid,
    10: Cylinder,
    11: Cone,
}


def run() -> None:
    """Запуск вычислений."""
    print('Введите номер фигуры:')
    shapes_list_text = ''

    for num, shape_class in ALLOW_SHAPES.items():
        shapes_list_text += f'{num} - {shape_class.title}\n'
    
    shape_num = int(input(shapes_list_text))

    if shape_num not in ALLOW_SHAPES:
        print('Вы ввели неправильный номер фигуры')
        return
    
    shape_class = ALLOW_SHAPES[shape_num]
    params_list_text = 'Введите параметры через пробел:\n'

    for name, description in shape_class.params.items():
        params_list_text += f'{name} - {description}\n'
    
    params_text = input(params_list_text)
    params = [float(i) for i in params_text.split()]
    shape_instanse = shape_class(*params)

    for method_name, method_descr in shape_instanse.get_print_data().items():
        print(f'{method_descr}: {getattr(shape_instanse, method_name)()}')

def main() -> None:
    end_response = None

    while True:
        run()
        
        correct_input = False
        while not correct_input:
            end_response = input('Продолжить вычисления (или выйти)? Y / N \n')

            if end_response.upper() not in {'Y', 'N'}:
                print('Некорректный ввод')
            else:
                correct_input = True
        
        if end_response.upper() == 'N':
            break
        

if __name__ == '__main__':
    main()
