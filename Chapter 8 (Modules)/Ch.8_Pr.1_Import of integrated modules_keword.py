# Chapter 8. Modules
# Practice 1. Import of integrated modules. Keyword

print("""Встроенный модуль keyword позволяет проверить, является ли строка клю-
чевым словом в Python.
Например:

import keyword

keyword.iskeyword("for")
keyword.iskeyword("football")
""")

print("Результат:")
import keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
