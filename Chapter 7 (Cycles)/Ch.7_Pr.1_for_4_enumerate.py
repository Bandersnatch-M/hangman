# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.3.
# Использование for для изменения элементов списков, кортежей и словарей.
# Синтаксис "enumerate"!

# Использование синтаксиса "enumerate"!
print("""
Поскольку получение доступа к каждому элементу в итерируемом объекте и
его индексу — распространенная задача, у Python для этого есть специальный
синтаксис "enumerate".
Ниже пример его использования:

tv = ["Breaking Bad",
      "Secret Files",
      "Fargo"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
        
print(tv)
""")
print("Result:")
tv = ["Breaking Bad",
      "Secret Files",
      "Fargo"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
        
print(tv)
    
print("""
Вместо перебора списка tv вы передали список tv в enumerate и выполни-
ли перебор результата, что позволило ввести новую переменную i, отслеживаю-
щую текущий индекс.""")

