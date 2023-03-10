# Chapter 7. Cycles
# Practice 5. "Continue" instruction. Ex.1

print("""
Вы можете использовать инструкцию continue, чтобы прервать текущую ите-
рацию цикла и продолжить со следующей итерации. Скажем, вам нужно вывести
все числа от 1 до 5, кроме числа 3. Вы можете это осуществить, используя цикл
for и инструкцию continue.""")
# Continue для конструкции for ... in ...
print("""
Пример:

for i in range(1,11):
      if 3 < i < 7:
          continue
      print(i)
""")
print("Результат:")
for i in range(1,11):
      if 3 < i < 7:
          continue
      print(i)
print("""
В этом цикле, когда переменная i принимает значение 3, выполняется ин-
струкция continue — тогда вместо того, чтобы полностью завершиться, как в
случае с ключевым словом break, цикл продолжает работать. Он переходит к
следующей итерации, пропуская код, который должен был выполниться. Когда
переменная i принимает значение 3, Python выполняет инструкцию continue,
а не выводит число 3.
Аналогичного результата можно достичь при помощи цикла while и ин-
струкции continue.""")
# Continue для конструкции while
print("""
Пример:

i = 1
while i < 11: 
      if 3 < i < 7:
          i = i + 1
          continue
      print(i)
      i = i + 1
""")
print("Результат:")
i = 1
while i < 11: 
      if 3 < i < 7:
          i = i + 1
          continue
      print(i)
      i = i + 1
