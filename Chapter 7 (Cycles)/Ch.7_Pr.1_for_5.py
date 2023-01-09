# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.5.
# Использование for для перемещения данных между изменяемыми итерируемыми объектами.

print("""
Использование for для перемещения данных между изменяемыми
(изменение строчных букв на заглавные) итерируемыми объектами:

tv = ["Breaking Bad", "Secret Files", "Fargo"]
films = ["Interstellar", "Terminator", "Aliens"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in films:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
""")
print("Результат:")
tv = ["Breaking Bad", "Secret Files", "Fargo"]
films = ["Interstellar", "Terminator", "Aliens"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in films:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
