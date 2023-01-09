# Chapter 9. Practice 2.
# Программа, которая задает пользователю вопрос и сохраняет ответ в файл.
# C:\Education\Python\Cory Althoff\the-self-taught-programmer-zaberov\Chapter 9 (files)\answer.txt

# Назначем переменной f_answer путь к файлу answer.txt
import os
f_answer = os.path.join("C:","\Education","Python","Cory Althoff",
                        "the-self-taught-programmer-zaberov","Chapter 9 (files)","answer.txt")
print("Путь к файлу:",f_answer)

# С помощью функции input задаём переменной answer значение ответа на указанный вопрос.
answer = input("Какой ваш любимый цвет?: ")
answer = str(answer)
# С помощью функции with open(..., "w") as "..." создаем файл по адресу в переменной f_answer
# С помощью метода "...".write("...") записываем в файл ("answer_txt") присвоенное значение answer
 
with open (f_answer,"w") as answer_txt:
    answer_txt.write(answer)
with open (f_answer,"r") as answer_txt:
    print(answer_txt.read())
