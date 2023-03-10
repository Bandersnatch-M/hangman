# Chapter 8. Modules
# Practice 1. Import of integrated modules. Pow

"""
Чтобы использовать модуль , его сначала нужно импортировать , то есть напи-
сать код, который сообщит Python, где искать модуль. Импортировать модуль
можно командой с синтаксисом import "имя_модуля". Замените значение "имя_модуля"
именем модуля, который вы импортируете. Как только вы выполнили
импорт модуля, вы можете использовать его переменные и функции.
"""

print("""Ниже показано, как импортируется модуль math:

import math

Как только вы импортировали модуль, можно использовать его код при по-
мощи синтаксиса "имя_модуля.код", указав "имя_модуля", который вы импор-
тировали, и код - желаемой функции или переменной из модуля.
Ниже приведен пример импорта и использования функции pow из модуля math,
принимающей два параметра, x и y, и возводящей x в степень y.

import math
math.pow(2,3)

""")

print("Результат:")
import math
print(math.pow(2,3))
