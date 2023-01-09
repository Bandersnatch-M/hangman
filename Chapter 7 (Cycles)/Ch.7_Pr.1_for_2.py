# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.2.
# Использование for для списков, кортежей и словарей

# Для списков
print("""
Пример использования цикла for для перебора элементов списка:

shows = ["Breaking Bad","Secret Files","Fargo"]
for show in shows:
     print(show)
""")
print("Result:")
shows = ["Breaking Bad","Secret Files","Fargo"]
for show in shows:
     print(show)
# Для кортежей
print("""
Пример использования цикла for для итерирования элементов кортежа:

sitcoms = ("The Big Bang Theory","Friends","Папины дочки")
for show in sitcoms:
     print(show)
""")
print("Result:")
sitcoms = ("The Big Bang Theory","Friends","Папины дочки")
for show in sitcoms:
     print(show)
# Для словарей
print("""
Пример использования цикла for для перебора ключей в словаре:

flat = {1: "Прихожая",
        2: "Гардеробная",
        3: "Прачечная",
        4: "Кухня",
        5: "Коридор",
        6: "Ванная",
        7: "Жилая комната №1",
        8: "Жилая комната №2",
        9: "Жилая комната №3"}

for number in flat:
     print(number)
""")
print("Result:")
flat = {1: "Прихожая",
        2: "Гардеробная",
        3: "Прачечная",
        4: "Кухня",
        5: "Коридор",
        6: "Ванная",
        7: "Жилая комната №1",
        8: "Жилая комната №2",
        9: "Жилая комната №3"}

for number in flat:
     print(number)
