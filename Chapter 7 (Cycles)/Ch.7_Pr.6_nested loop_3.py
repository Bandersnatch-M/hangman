# Chapter 7. Cycles
# Practice 5. Вложенный цикл. Ex.3

# Пример 2.
"""
Можно вкладывать цикл for внутрь цикла while и наоборот.
"""

print("""
Пример 3:

while input('d or n?') != 'n':
    for i in range(1,6):
        print(i)

Программа будет выводить числа от 1 до 5, пока пользователь не введет n.
""")
print("Результат:")
while input('d or n? ') != 'n':
    for i in range(1,6):
        print(i)
