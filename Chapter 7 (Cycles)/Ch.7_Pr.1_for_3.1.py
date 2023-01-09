# Chapter 7. Cycles
# Practice 1. "for" cycles. Ex.3.
# Использование for для изменения элементов списков, кортежей и словарей.

# Изменение элемнтов сразу во всем списке


tv = ["Breaking Bad", "Secret Files", "Fargo", "Terminator", "Interstellar", "Jango Unchained"]
for show in tv[2:5]:
    show = show.upper()
    print(show)




