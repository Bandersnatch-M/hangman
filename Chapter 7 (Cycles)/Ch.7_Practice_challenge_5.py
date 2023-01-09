# Chapter 7. Cycles
# Practice challenge 5

print("""Умножьте все числа в списке [8, 19, 148, 4] на все числа в списке [9,
1, 33, 83] и поместите результаты в третий список.
""")

print("Результат:")
list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
list_mult = []
for i in list_1:
    for j in list_2:
        list_mult.append(i*j)
print(list_mult)
for n in list_mult:
      print(n)

