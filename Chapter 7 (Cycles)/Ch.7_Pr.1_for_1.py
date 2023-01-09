# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.1

print("Цикл for предназначен для перебора итерируемого объекта.")

"""Процесс перебора называется итерированием. Цикл for можно использовать, чтобы
определять инструкции, которые будут выполняться один раз для каждого элемента в
итерируемом объекте, и с помощью таких инструкций вы можете получать доступ
ко всем этим элементам и осуществлять операции с ними.
Например, с помощью цикла for, выполняющего перебор списка строк, и метода
upper можно сделать символы каждой строки прописными."""

print("""Определяется синтаксисом for "имя_переменной" in "имя_итерируемого_объекта":
инструкции, где "имя_переменной" – выбранное вами имя переменной, которая назначается
значению каждого элемента в итерируемом объекте, а инструкции — код, который
выполняется при каждом прохождении цикла.""")
print("""
Пример 1:)
name = "Ted"
for character in name:
    print(character)
""")
print("Результат:")
name = "Ted"
for character in name:
    print(character)
    
"""При каждом прохождении цикла переменная character назначается эле-
менту итерируемого объекта name. При первом прохождении выводится буква
T, поскольку переменная character назначена первому элементу объекта name.
При втором прохождении выводится буква e, ведь character назначена вто-
рому элементу name. Процесс продолжается до тех пор, пока каждый элемент в
итерируемом объекте не будет назначен переменной character."""

print("""
Пример 2:
a = 1000
for n in a:
    print(n)
""")
print("Результат:")
a = "1000"
for n in a:
    print(n)
