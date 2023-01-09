# Chapter 5. Practice 2-8. Checking elements in list.
"""Проверить, есть ли элемент в списке, можно с помощью ключевого слова in."""

fruits = ["grape", "plum", "banana"]
print("There is a list of fruits: ", fruits)
print("There is a banana in the list.", "banana" in fruits)
print("There is an apple in the list.", "apple" in fruits)

"""Для проверки отсутствия элемента в списке используйте ключевое слово not."""

print("There is no melon in the list.", "melon" not in fruits)
print("There is no plum in the list.", "plum" not in fruits)

