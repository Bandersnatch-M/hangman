#
"""Напишите функцию, которая преобразовывает строку в тип данных float и
возвращает результат. Используйте обработку исключений, чтобы перехва-
тить возможные исключения."""

def f():
    try:
        x = input("Input your number: ")
        x = float(x)
        print ("Float number is: ",x)
    except ValueError:
        print ("Please pay your attantion, you can't print any text or use comas in numbers!")

f()
