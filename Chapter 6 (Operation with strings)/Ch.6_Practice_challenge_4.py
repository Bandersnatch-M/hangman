# Chapter 6. Practice challenge 4.

print("""Вызовите метод, который превращает строку "Где это? Кто это?
Когда это?" в список ["Где это? Кто это? Когда это?"].
""")


phrase = "Где это? Кто это? Когда это?"
print("Строка:")
print(phrase)
print("""
Разбиваем строку на элементы:""")
a = phrase[:9]
print(a)
b = phrase[9:17]
print(b)
c = phrase[18:]
print(c)
phrase_list = list([a,b,c])
print("""
Создаем из элементов список:""")
print(phrase_list)
