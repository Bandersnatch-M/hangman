# Chapter 9. Saving in files CSV
# C:\Education\Python\Cory Althoff\the-self-taught-programmer-zaberov\Chapter 9 (files)\st.txt

"""
CSV-файл можно открыть с помощью инструкции with, но внутри нее нужно ис-
пользовать модуль csv, чтобы конвертировать файловый объект в объект csv. У моду-
ля csv есть метод writer, который принимает файловый объект (f) и разделитель
(delimiter = ","): csv.writer(f,delimiter = ",")
Метод writer возвращает объект csv с помощью метода writerow. Метод writerow
принимает в качестве параметра список, и вы можете его использовать для записи в
CSV-файл. Каждый элемент в списке записывается — отделенный разделителем, ко-
торый вы передали методу writer — в строку в CSV-файле. Метод writerow создает
только одну строку, так что для создания двух строк его нужно вызвать дважды.
"""


import os
os = os.path.join("C:","\Education","Python","Cory Althoff","the-self-taught-programmer-zaberov",
                  "Chapter 9 (files)","st.csv")
print (os)

import csv
with open(os, "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
        print(row)

