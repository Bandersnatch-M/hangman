# Chapter 7. Cycles
# Practice challenge 4

print("""Напишите программу с бесконечным циклом (с возможностью ввести букву
X, чтобы выйти) и списком чисел. При каждом переборе цикла предлагайте
пользователю отгадать число из списка и сообщайте, правильно ли он отга-
дал.
""")

print("Результат:")
list_n = [4,7,5,3,2,9,8,10,6,1]
n = 0
while True:
    a = input("Введите число (если нужно выйти нажмите Q): ")
    if a == "Q":
      break
    a = int(a)
    if a == list_n[n]:
        print("Поздравляю! Вы угадали число!\nИнтересно, угадаете ли следующее?")
    else:
        print("Извините. Вам не удалось угадать число.\nПопробуйте еще раз.")
    n = (n + 1) % 10

