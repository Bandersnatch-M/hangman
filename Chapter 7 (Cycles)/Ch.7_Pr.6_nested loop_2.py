# Chapter 7. Cycles
# Practice 5. Вложенный цикл. Ex.2

# Пример 2.
"""
Можно использовать циклы for для прибавления каждого числа из одно-
го списка к каждому числу из другого списка.
"""

print("""
Пример 2:

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)

Первый цикл выполняет итерирование каждого целого числа в списке
list1. Для каждого элемента в этом списке второй цикл перебирает каждое це-
лое число в собственном итерируемом объекте, затем прибавляет его к числу из
list1 и добавляет результат в список added. Во втором цикле for использована пере-
менная j, поскольку имя i уже занято в первом цикле.
""")
print("Результат:")
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)