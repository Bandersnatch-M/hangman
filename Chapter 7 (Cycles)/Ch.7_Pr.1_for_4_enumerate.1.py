# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.3.
# Использование for для изменения элементов списков, кортежей и словарей.
# Синтаксис "enumerate"!

# Использование синтаксиса "enumerate"!

print("Result:")
tv = ["Breaking Bad", "Secret Files", "Fargo",
      "Terminator", "Interstellar", "Jango Unchained"]
i = 2
for i, show in enumerate(tv[2:3]):
    new = tv[i]
    new = new.upper()
    tv[i] = new
        
print(tv)
    
print("""
Вместо перебора списка tv вы передали список tv в enumerate и выполни-
ли перебор результата, что позволило ввести новую переменную i, отслеживаю-
щую текущий индекс.""")

