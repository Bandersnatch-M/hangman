# Chapter 7. Cycles
# Practice 4. "break" instruction. Ex.2.

print("""
Можно использовать цикл while и ключевое слово break для написания про-
граммы, которая будет просить пользователя ввести данные, пока он не введет
букву Q, чтобы выйти.

Например:
qs = ["What is your name?",
      "What is your favorite colour?",
      "What are you doing?"]
n = 0
while True:
    print("Enter Q for escape")
    a = input(qs[n])
    if a == "Q":
        break
    n = (n + 1) % 3
    
Комментарий:
При каждом прохождении цикла данная программа задает пользователю один
из вопросов из списка qs.
n — переменная индекса. При каждом прохождении цикла вы присваиваете
n значение выражения (n + 1) % 3, что позволяет бесконечно проходить по
каждому вопросу в списке qs. При первом прохождении цикла n начинает с 0.
Затем n присваивается значение выражения (0 + 1) % 3, которое равно 1. По-
сле чего n присваивается значение (1 + 1) % 3, которое равно 2, ведь всегда,
когда первое число в выражении с оператором деления по модулю меньше вто-
рого, ответом является это первое число. Наконец, n присваивается значение
(2 + 1) % 3, равное 0, как и в начале.
""")
print("Результат:")
qs = ["What is your name? ",
      "What is your favorite colour? ",
      "What are you doing? "]
n = 0
while True:
    print("Enter Q for escape ")
    a = input(qs[n])
    if a == "Q":
        break
    n = (n + 1) % 3