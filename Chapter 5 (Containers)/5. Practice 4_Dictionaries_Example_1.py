# Chapter 5. Practice 4-1. Using Dictionaries

"""Словарь (dict) — еще один встроенный контейнер для хранения объектов. Он ис-
пользуется для связывания одного объекта, называемого ключом, с другим,
называемым значением. Такое связывание называется отображением. Резуль-
татом будет пара ключ-значение. Пары ключ-значение добавляются в словарь.
Затем вы можете найти в словаре ключ и получить соответствующее ему значе-
ние. Однако нельзя использовать значение для нахождения ключа.
Словари являются изменяемыми , так что в них можно добавлять новые пары
ключ-значение. В отличие от списков и кортежей, словари не хранят объекты в
определенном порядке. Их полезность заключается в связях между ключами и
значениями — существует множество ситуаций, в которых вам нужно будет со-
хранять данные попарно. Например, в словаре можно сохранить информацию
о ком-либо, связав ключ, представляющий рост, со значением роста человека,
ключ, представляющий цвет глаз, со значением цвета глаз человека, и ключ,
представляющий национальность, с соответствующим значением."""

# Словари объявляются с помощью фигурных скобок.
# Для создания словаря существует два варианта синтаксиса:

"""Первый вариант"""

my_dict1 = dict(one=1, two=2)
print(my_dict1)

"""Второй вариант"""

my_dict2 = {"1":"one", "2":"two"}
print(my_dict2)
