# Chapter 9. Practice 3.
"""Примите элементы в списке списков:
[["Star Wars","Terminator","Artificial Intelegence"],
["The Fool","Matilda","Leviathan"],
["Man in black","I am Robot", "Evolution"]]
и запишите их в CSV-файл.
Данные каждого списка должны быть стройкой в файле, при этом каждый элемент списка
должен быть отделен запятой.
"""
# C:\Education\Python\Cory Althoff\the-self-taught-programmer-zaberov\Chapter 9 (files)\film_list.csv


# 1.Зададим список
filmlist = [["Star Wars","Terminator","Artificial Intelegence"],["The Fool","Matilda","Leviathan"],
["Man in black","I am Robot","Evolution"]]
print(filmlist)


# 2.Назначем переменной path_to_filmlist путь к файлу film_list.csv
import os
path_to_filmlist = os.path.join("C:","\Education","Python","Cory Althoff",
                        "the-self-taught-programmer-zaberov","Chapter 9 (files)","film_list.csv")
print("""
Путь к файлу:""",path_to_filmlist)

# 3. Вызываем функцию CSV: import csv
"""
1. С помощью функции with open(..., "w") as "..." создаем файл film_list_csv по адресу из
path_to_filmlist;
2. С помощью метода csv.writer("film_list_csv, delimiter=","") для переменной w принимаем файловый
объект ("film_list_csv") и разделитель (",").
3. С помощью метода w.writerow([]) последовательно прописываем элементы в виде строк из списка
в задании.
"""
import csv

with open (path_to_filmlist,"w") as film_list_csv:
    w = csv.writer(film_list_csv, delimiter=", ")
    w.writerow(filmlist[0])
    w.writerow(filmlist[1])
    w.writerow(filmlist[2])
        
with open (path_to_filmlist,"r") as film_list_csv:
    print("""
Результат:
""")
    print(film_list_csv.read())
