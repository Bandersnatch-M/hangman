# Chapter 6. Operations with strings.
# Practice 5. strip Method. 

print("""
Использование метода strip!
Метод strip используется для удаления пробельных символов в начале и конце
строки.
""")
# Пример 
print("""Пример:
z = "    Зеленоград       "
v = "   Супер!     "
print("Было:")
print(z,v)
z = z.strip()
v = v.strip()
print("Стало после использования метода strip:")
print(z,v)
""")

z = "    Зеленоград       "
v = "   Супер!     "
print("Было:")
print(z,v)
z = z.strip()
v = v.strip()
print("Стало после использования метода strip:")
print(z,v)

