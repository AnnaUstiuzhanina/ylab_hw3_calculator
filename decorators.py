import functools


def round_decorator(decimal_places: int):
    """
        Декоратор для округления результата функции/метода.
        Аргументы:
            decimal_places - на сколько знаков округлять
    """
    def decorator_wrapper(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            result = funct(*args, **kwargs)
            return round(result, decimal_places)
        return wrapper
    return decorator_wrapper