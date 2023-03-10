# Chapter 5. Practice 5-1. Контейнеры внутри контейнеров.
# Практика со списками внутри списков.

# Создаем список flat.
flat = []
print("Квартира состоит из трёх зон:")
# Создаем списки комнат по зонам (не жилая, мокрая, жилая)
nl_zone = ["Прихожая",
           "Гардеробная",
           "Коридор"]
print("Нежилая зона: ",nl_zone) 
w_zone = ["Кухня",
          "Прачечная",
          "Ванная"]
print("Мокрая зона: ",w_zone) 
l_zone = ["Жилая комната №1",
          "Жилая комната №2",
          "Жилая комната №3"]
print("Жилая зона: ",l_zone) 

# С помощью метода [список].append([список_n]) добавляем поочередно в список flat списки комнат
flat.append(nl_zone)
flat.append(w_zone)
flat.append(l_zone)

# Выводим на экран список зон с комнатами   
print("Список комнат в квартире по зонам: ",flat)

# Списки внутри списка flat имеют свои индексы:
""" nl_zone - индекс [0]
    w_zone - индекс [1]
    l_zone - индекс [2]
    Таким образом можно вывести на экран требуемый список из общего списка"""

nl_zone = flat[0]
w_zone = flat[1]
l_zone = flat[2]

# Если добавить новые элементы в список nl_zone, то при выводе получится такой результат:
print("Добавим в нежилую зону балконы:")
nl_zone = flat[0]
nl_zone.append("Балкон №1")
nl_zone.append("Балкон №2")
print("Таким образом в нежилую зону входят комнаты: ",nl_zone)
print("Список комнат в квартире по зонам теперь выглядит так: ",flat)

