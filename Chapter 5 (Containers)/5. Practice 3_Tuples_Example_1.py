# Chapter 5. Practice 3-1. Using Tuples

"""Кортеж (tuple) — это контейнер, хранящий объекты в определенном порядке.
В отличие от списков, кортежи неизменяемы, то есть их содержимое нельзя изменить.
Как только вы создали кортеж, значение какого-либо его элемента уже нельзя из-
менить, как нельзя добавлять и удалять элементы. Кортежи объявляются с по-
мощью круглых скобок. Элементы в кортеже должны быть разделены запятыми."""

"""Зачем использовать структуру данных, которая кажется менее гибкой, чем список?
Кортежи удобно использовать, когда вы имеете дело со значениями, которые никогда
не изменятся, и вы хотите быть уверенными, что их не изменят другие части вашей
программы. Примером данных, которые удобно хранить в кортеже, могут быть
географические координаты. Долготу и широту города следует сохранить в кортеже,
поскольку эти значения никогда не изменятся, и сохранение в кортеже будет
гарантировать, что другие части программы случайно их не изменят. Кортежи, в
отличие от списков, могут использоваться в качестве ключей в "словарях", о
которых пойдет речь в следующих практиках"""

# Для создания кортежей используют один из двух вариантов синтаксиса:

"""Первый вариант:"""

my_tuple = tuple("12")
print (my_tuple)

"""Второй вариант:"""

my_tuple = (12)
print (my_tuple)

"""Чтобы добавить в кортеж новые объекты, создайте его вторым способом, указав
через запятую каждый желаемый элемент."""

rndm_tuple = ("Back", 1981, True)
print(rndm_tuple)

"""Даже если кортеж содержит только один элемент, после этого элемента все
равно нужно поставить запятую. Таким образом Python отличает кортеж от чис-
ла в скобках, определяющих порядок выполнения операций."""

# Это кортеж (tuple)
print (("self_taught",))

# Это не кортеж (not tuple)
print ((9)+1)

"""Получить элементы кортежа можно тем же способом, что и элементы списка
указывая индекс элемента."""

books = ("45 tatoos of manager", "Top secrets of Project Management", "Basic Economy")
print (books[1])

"""Проверить, содержится ли элемент в кортеже, можно с помощью ключевого
слова in, а отсутствие с помощью - not in."""

books = ("45 tatoos of manager", "Top secrets of Project Management", "Basic Economy")
print ("45 tatoos of manager" in books)
print ("45 tatoos of manager" not in books)
print ("1984" in books)
print ("1984" not in books)


"""После создания кортежа в него нельзя добавлять новые элементы или изме-
нять существующие. При попытке изменить элемент в кортеже после его созда-
ния Python сгенерирует исключение."""

books = ("45 tatoos of manager", "The secrets of Project Management", "Basic Economy")
books[2] = "Economy"

#

