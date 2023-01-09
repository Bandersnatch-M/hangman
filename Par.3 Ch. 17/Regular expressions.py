"""Hегулярные выражения в Python при помощи встроенной библиотеки re
(от англ. словосочетания regular expressions — регулярные выражения).
В модуле re есть метод findall. В качестве параметров в него передается
регулярное выражение, затем строка, и он возвращает список со всеми
элементами в строке, которые совпадают с шаблоном.
"""

import re
l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)
print(matches)

"""Чтобы не учитывать регистр в методе findall, передайте в него значение
re.IGNORECASE в качестве третьего параметра."""

import re
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)
