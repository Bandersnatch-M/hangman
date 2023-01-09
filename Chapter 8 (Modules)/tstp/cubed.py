# Chapter 8. Modules
# Practice challenge 2. working modul - cubed

"""
Создайте модуль cubed, содержащий функцию, которая принимает в каче-
стве параметра число, возводит это число в куб и возвращает его. Импорти-
руйте и вызовите функцию из другого модуля.
"""
while True:
    n = input("Enter the number: ")
    try:
        n = float(n)
        n = n**3
        print(n)
        break
    except(ValueError):
        print ("Текст вводить нельзя. Попробуйте еще раз.")



