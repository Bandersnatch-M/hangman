"""import re - вызов встроенной библиотеки (модуля) re (regular expressions).
В модуле имеется метод - findall.

Можно создавать регулярные выражения со сложными шаблонами, доба-
вив в них особые символы, которые не используются для поиска совпадения, а
определяют правило. Например, для создания регулярного выражения, которое
ищет шаблон, только если он встречается в начале строки, можно использовать
символ каретки (^).
Ниже приведен пример использования символа каретки (^) в Python (вы
должны передать значение re.MULTILINE в качестве третьего параметра мето-
ду findall, чтобы искать совпадения во всех строках многострочного экрана).
"""

import re
zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
m = re.findall("^If", zen, re.MULTILINE)
print(m)

