# Chapter 6. Operations with strings.
# Practice 2. Format Method. 

print("""
Использование метода format!
Новую строку можно создать при помощи метода format, проверяющего вхож-
дения в строке фигурных скобок {} и заменяющего их переданными ему пара-
метрами.""")
# Пример 1
print("""
Пример 1:

"Уильям {}".format("Фолкнер")

/Метод format добавит в {} фамилию "Фолкнер" к имени "Уильям"./
""")
print("Результат:")
print("Уильям {}".format("Фолкнер"))

# Пример 2
print("""
Пример 2:
В качестве параметра можно также передавать переменную.""")

print("""Пример кода:

sername = "Фолкнер"
"Уильям {}".format(sername)

/Метод format добавит переменную sername в {}./
""")
sername = "Фолкнер"
print("Результат:")
print("Уильям {}".format(sername))

# Пример 3
print("""
Пример 3:
Вы можете использовать в строке фигурные скобки столько раз, сколько по-
желаете.""")

print("""Пример кода:

author = "Уильям" 
sername = "Фолкнер"
born = "1897"
"{} {} родился в {}".format(author, sername, born)

/Метод format добавит переменные author, sername и born в {}./
""")
author = "Уильям" 
sername = "Фолкнер"
born = "1897"
print("Результат:")
print("{} {} родился в {}г.".format(author, sername, born))

# Пример 4
print("""
Пример 4:
Метод format может пригодиться, если вы создаете строку из пользователь-
ского ввода.""")

print("""Пример кода:

noun1 = input("Введите существительное:") 
verb = input("Введите глагол:") 
adj = input("Введите прилагательное:")
noun2 = input("Введите существительное:")
result = "Билеберда обычно выглядит так: {} {} {} {}".format(noun1,verb,adj,noun2)
print("Результат:")
print(result)
/Метод format добавит введенные вами слова в {}./
""")
noun1 = input("Введите существительное:") 
verb = input("Введите глагол:") 
adj = input("Введите прилагательное:")
noun2 = input("Введите существительное:")
result = "Билеберда обычно выглядит так: {} {} {} {}".format(noun1,verb,adj,noun2)
print("Результат:")
print(result)