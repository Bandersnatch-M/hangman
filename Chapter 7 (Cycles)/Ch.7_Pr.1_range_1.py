# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.5.
# Использование for для перемещения данных между изменяемыми итерируемыми объектами.

print("""
Можно использовать встроенную функцию range, чтобы создать последователь-
ность целых чисел и цикл for , чтобы выполнить ее перебор. Функция range
принимает два параметра: число, с которого последовательность начинается, и
число, на котором она заканчивается. Последовательность целых чисел, возвра-
щаемая функцией range, включает в себя первый параметр (число, с которого
нужно начать), но не включает второй (число, на котором нужно закончить).
Ниже приведен пример использования функции range для создания последова-
тельности чисел и их перебора:

for i in range(1,11):
    print(i)
""")
print("Результат:")
for i in range(1,11):
    print(i)
