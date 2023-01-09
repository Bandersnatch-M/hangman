# Chapter 9. Saving in files.
# Open and auto close files (инструкция "with") and read
# C:\Education\Python\Cory Althoff\the-self-taught-programmer-zaberov\Chapter 9 (files)\stl.txt

"""
Если вы хотите прочесть данные из файла , то передаете "r" в качестве второго
параметра в open. Затем вы вызываете метод read в своем файловом объекте,
что возвращает итерируемый объект со всеми строками файла.
"""

# Задаем переменной path_stl_txt путь к файлу stl.txt

import os
path_stl_txt = os.path.join("C:","\Education","Python","Cory Althoff","the-self-taught-programmer-zaberov",
                  "Chapter 9 (files)","stl.txt")
print("Путь к файлу:",path_stl_txt)

# Создаем файл stl.txt по указанному в переменной path_stl_txt пути и прописываем в него желаемый код:
#(f.write("код")

with open(path_stl_txt, "w") as f:
    f.write("Hello from Python and welcome to the future!")

# с помощью той же функции with open, инструкции r и метода "имя_объекта".read выводим
# в интерактивную оболочку IDLE содержимое файла stl.txt:

with open(path_stl_txt, "r") as f:
    print (f.read())

"""
Для того, чтобы можно было использовать содержимое, созданного в программе файла несколько раз,
не прибегая к новому открытию и закрытию его, достаточно внести содержимое файла в переменную или в контейнер.
"""

# Внесение содержимого файла в список:
# C помощью функции with open и инструкции r - читаем файл. С помощью метода "имя_списка".append()
# добавляем "имя_объекта".read() в список

file_list = list()

with open(path_stl_txt, "r") as f:
    file_list.append(f.read())
print (file_list)
    
