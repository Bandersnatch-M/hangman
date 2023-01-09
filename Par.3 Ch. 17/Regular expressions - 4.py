"""import re - вызов встроенной библиотеки (модуля) re (regular expressions).
В модуле имеется метод - findall.
Повторения.

Символ звездочки (*) добавляет в регулярные выражения повторение. При его
помощи «предшествующий элемент будет найден ноль или более раз». К при-
меру, используя звездочку, можно найти совпадения с "to", за которым следует лю-
бое количество букв "o".

В регулярных выражениях точка соответствует любому символу. Если вы ука-
жете звездочку после точки, будет выполняться поиск совпадения с любым сим-
волом ноль или более раз. Можно использовать точку со звездочкой для поиска
всего, что находится в промежутке между двумя символами."""

import re
t = "__one__ __two__ __three__"
found = re.findall("__.*__", t)
print(found)

"""Регулярное выражение __.*__ находит все символы между двумя двойными
подчеркиваниями , включая сами подчеркивания. Символ звездочки является жад-
ным — это значит, что он попытается найти столько текста, сколько сможет."""

"""Однако, не всегда нужно искать шаблоны жадным образом. Чтобы сделать регуляр-
ное выражение нежадным , можно указать после звездочки вопросительный
знак. Нежадное регулярное выражение ищет наименьшее возможное количе-
ство совпадений. В Python для этого можно использовать знак вопроса.
"""

import re
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

"""В регулярных выражениях вы можете экранировать символы (игнорировать их
значение, просто находя совпадения) так же, как вы делали в случае со строками
в Python, указывая обратный слеш \ перед регулярным выражением."""

import re
t = "one two three $"
found = re.findall("\\$", t, re.IGNORECASE)
print(found)