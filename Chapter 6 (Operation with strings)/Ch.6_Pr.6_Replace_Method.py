# Chapter 6. Operations with strings.
# Practice 6. Replace Method. 

print("""
Использование метода replace!
Метод replace заменяет каждое вхождение строки другой строкой. Первый па-
раметр — строка, которую нужно заменить, второй — строка, которой нужно за-
менить вхождения.
""")
# Пример 
print("""Пример:
equ = "Все животные одинаковы"
equ = equ.replace("о", "@")
print(equ)
""")

equ = "Все животные одинаковы"
equ = equ.replace("о", "@")
print("Результат:")
print(equ)

