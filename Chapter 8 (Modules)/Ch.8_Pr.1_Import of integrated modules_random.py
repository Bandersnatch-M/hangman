# Chapter 8. Modules
# Practice 1. Import of integrated modules. Random

print("""random — еще один встроенный модуль. Вы можете использовать его функ-
цию randint для создания случайного числа: передайте функции два целых чис-
ла, и она вернет выбранное случайным образом целое число в промежутке меж-
ду ними, пример:

import random
random.randint(0,100)
""")

print("Результат:")
import random
print(random.randint(0,100))
