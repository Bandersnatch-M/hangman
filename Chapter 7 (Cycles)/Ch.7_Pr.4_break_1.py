# Chapter 7. Cycles
# Practice 4. "break" instruction. Ex.1.

print("""
Инструкция с ключевым словом break используется, чтобы прекратить цикл.

Например следующий цикл должен выполниться 10 раз:

for i in range(1,11):
    print(i)

Результат:""")
for i in range(1,11):
    print(i)    
print("""
однако, если добавить инструкцию break, то цикл выполнится лишь один раз.

Пример:
for i in range(1,11):
    print(i)
    break
""")

print("Результат:")
for i in range(1,11):
    print(i)
    break
print("""
Как только Python сталкивается с инструкцией break, цикл завершается.""")
