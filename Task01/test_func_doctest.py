if __name__ == "__main__":
    import doctest
    import triangle_func_doctest

    # Запуск тестов из docstring функции get_triangle_type
    doctest.testmod(triangle_func_doctest, verbose=True)