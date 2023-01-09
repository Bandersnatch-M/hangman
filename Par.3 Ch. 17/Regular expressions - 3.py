"""import re - вызов встроенной библиотеки (модуля) re (regular expressions).
В модуле имеется метод - findall.

Чтобы определить шаблон для поиска совпадений с несколькими символами,
поместите эти символы внутрь квадратных скобок в регулярном выражении.
Если вы укажете значение [abc], регулярное выражение будет искать совпадения
с a, b или c.
В Python это делается так:
"""

import re
string = "Two too"
m = re.findall("t[wo]o", string, re.IGNORECASE)
print(m)

"""С помощью символа \d можно искать совпадения цифр."""

import re
line = "123?34 hello?"
m = re.findall("\d", line, re.IGNORECASE)
print(m)
