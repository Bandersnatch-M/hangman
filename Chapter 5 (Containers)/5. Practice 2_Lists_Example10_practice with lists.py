# Chapter 5. Practice 2-10. Using the lists in practice


fruits = ["grape", "plum", "banana"]
print("""We have a list of fruits!
Try to guess is there your favorite fruit in the list!""")
guess = input("Please, put here your favorite fruit: ")

if guess in fruits:
    print ("Congratulations! We've got your favorite fruit!")
else:
    print ("Sorry! We haven't got your favorite fruit!")

"""Список fruits содержит различные строки, представляющие фрукты. При
помощи встроенной функции input программа предлагает пользователю указать
фрукт и сохраняет его ответ в переменной. Если этот ответ содержится в спи-
ске fruits, программа сообщает пользователю, что выбранный им фрукт
содержится в списке. В противном случае, программа сообщает, что фрукта в
списке нет."""
