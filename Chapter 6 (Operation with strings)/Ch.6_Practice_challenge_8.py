# Chapter 6. Practice challenge 8.

print("""Найдите в своей любимой книге диалог (с кавычками) и превратите его в строку.
""")

print("""Взят диалог из книги "Dune", Frank Herbert:
Dr. Yueh sighed.
"Would it disturb Paul if I looked in on him?" she asked.
"Not at all. I gave him a sedative."
"He's taking the changewell?" she asked.
"Except for getting a bit overtired. He's excited, but what fifteen-year-old wouldn't be under
these circumstances?" He crossed to the door, opened it. "He's in here"
Jessica followed, peered into a shadowy room.
""")

print("Для создания строки, помещаем весь диалог в кавыяки и присваиваем ему переменную string")
print("""Теперь с переменной string можно работать как со строкой,
например посчитать количество элементов с помощью функции len.""")
string = """
Dr. Yueh sighed.
"Would it disturb Paul if I looked in on him?" she asked.
"Not at all. I gave him a sedative."
"He's taking the changewell?" she asked.
"Except for getting a bit overtired. He's excited, but what fifteen-year-old wouldn't be under
these circumstances?" He crossed to the door, opened it. "He's in here"
Jessica followed, peered into a shadowy room.
"""
print("Длинна строки составляет:", len(string))
print("\nПервая фраза: ", string[:17])
print("\nВторая фраза: ", string[17:75])
