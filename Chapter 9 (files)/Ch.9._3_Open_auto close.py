# Chapter 9. Saving in files.
# Open and auto close files (инструкция "with")
# C:\Education\Python\Cory Althoff\the-self-taught-programmer-zaberov\Chapter 9 (files)\stl.txt

"""Синтаксис для открытия файла с помощью инструкции with следующий:
with open("путь_к_файлу", режим) as "имя_переменной":
    "ваш_код".
Значение "путь_к_файлу" представляет путь к вашему файлу, затем
указывается режим, в котором нужно открыть файл, "имя_переменной",
которой назначен файловый объект, а значение "ваш_код" обозначает
код, у которого есть доступ к этой переменной.
"""

import os
path_stl_txt = os.path.join("C:","\Education","Python","Cory Althoff","the-self-taught-programmer-zaberov",
                  "Chapter 9 (files)","stl.txt")
print("Путь к файлу:",path_stl_txt)

with open(path_stl_txt, "w") as f:
    f.write("Hello from Python and welcome to the future!")
