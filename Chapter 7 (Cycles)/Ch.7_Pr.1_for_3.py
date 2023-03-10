# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.3.
# Использование for для изменения элементов списков, кортежей и словарей.

# Изменение элемнтов сразу во всем списке
print("""
Изменение элемнтов сразу во всем списке при помощи for:

tv = ["Breaking Bad", "Secret Files", "Fargo"]
for show in tv:
    show = show.upper()
    print(show)
""")
tv = ["Breaking Bad", "Secret Files", "Fargo"]
for show in tv:
    show = show.upper()
    print(show)

# Изменение элемнтов в списке через итерации
print("""
При помощи цикла for можно изменять элементы в изменяемом итерируемом объекте,
например списке:

tv = ["Breaking Bad",
      "Secret Files",
      "Fargo"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
    
print(tv)
""")
print("Result:")
tv = ["Breaking Bad",
      "Secret Files",
      "Fargo"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
    
print(tv)
    
"""
В данном примере цикл for использовался для перебора списка tv. Вы отслеживаете
текущий элемент в списке с помощью переменной индекса (i) — переменной, хранящей
целое число, которое представляет индекс в итерируемом объекте. Значение
переменной индекса i начинается с 0 и увеличивается при каждом прохождении цикла.
Вы используете переменную индекса, чтобы получить текущий элемент списка, который
затем сохраняете в переменной new. После этого вы вызываете метод upper в переменной
new, сохраняете результат и используете свою переменную индекса, чтобы заменить этим
результатом текущий элемент в списке. Наконец, вы увеличиваете i, чтобы при
следующем прохождении цикла взять следующий элемент в списке."""



