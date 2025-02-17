# Пример корректного вызова внутренней функции вне внешней функции:
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # возвращаем значение внутренней функции
    return inner_function

# присваиваем переменной значение внешней функции (возвращённое значение внутреннй)
inner_func = test_function()
# теперь мы можем вызвать inner_function вне test_function используя
# синтаксис inner_func(), переменная используется как функция-ссылка на присвоенный объект
inner_func()

