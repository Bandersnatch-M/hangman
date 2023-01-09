# Chapter 7. Cycles
# Practice 5. Вложенный цикл. Ex.1

"""
Можно различными способами комбинировать циклы.
Например, можно поместить один цикл в другой, или создать цикл внутри
цикла внутри цикла. Нет никаких ограничений по количеству циклов, которые
можно помещать внутрь других циклов, хотя эти ограничения важны. Когда
цикл находится внутри другого цикла, второй цикл является вложенным в первый.
В этом случае цикл, содержащий внутри другой цикл, называется внешним, а
вложенный цикл — внутренним. Когда у вас есть вложенный цикл, внутренний цикл
выполняет перебор своего итерируемого объекта один раз за итерацию внешнего цикла.
"""

# Пример 1.
print("""
Пример 1:

for i in range(1,3):
      print(i)
      for letter in ["a", "b", "c"]:
          print(letter)
          
Вложенный цикл for будет перебирать список ["a", "b", "c"] столь-
ко раз, сколько раз выполняется внешний цикл — в нашем случае дважды.
Если сделать так, чтобы внешний цикл выполнялся три раза (for i in range(1,4)),
то и внутренний цикл также перебирал бы свой список трижды.
""")
print("Результат:")
for i in range(1,3):
      print(i)
      for letter in ["a", "b", "c"]:
          print(letter)

