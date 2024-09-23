# Пример вызова функции внутри функции:
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # вызываем inner_function внутри test_function

test_function()  # вызываем test_function