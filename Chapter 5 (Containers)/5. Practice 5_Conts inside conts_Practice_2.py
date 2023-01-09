# Chapter 5. Practice 5-2. Контейнеры внутри контейнеров.
# Практика с кортежами, списками и словарями внутри друг друга. 

# Список внутри кортежа:

print("Кортежи внутри списка:")
"""Создаем список []"""

locations = [] 

"""Создаем кортежи (tuples)"""
Sveta_work = ("Улица Юности", "дом 5") 
Sveta_home = ("Микрорайон 14", "корпус 1412")

"""Используем метод [list].append(tuple)"""
locations.append(Sveta_work)
locations.append(Sveta_home)
print(locations)

# Кортежи внутри списка:

print("Списки внутри кортежа:")
"""Создаем списки"""
Sveta_work = ["Улица Юности", "дом 5"] 
Sveta_home = ["Микрорайон 14", "корпус 1412"]

"""Создаем кортеж из списков"""
locations = (Sveta_work, Sveta_home)
print(locations)


# Словарь внутри кортежа и списка:

adress ={"Адрес работы":
         "Улица Юности, дом 5",
         "Адрес дома":
         "Микрорайон 14, корпус 1412, квартира 52"}
adress_list = [adress]
print("Словарь внутри списка:")
print(adress_list)
adress_tuple = (adress,)
print("Словарь внутри кортежа:")
print(adress_tuple)
