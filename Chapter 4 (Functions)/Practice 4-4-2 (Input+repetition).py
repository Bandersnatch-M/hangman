# Практика по исплользованию функции как средства для повторного запуска блоков с кодом. 


# На последующих строках блока кода для функции def необходимо делать отступ в 2 пробела!!!
# Если не сделать отсуп, программа выдает предупреждение!!!

def your_age():
  age = input("Put your age:")
  age = int(age)
  if age <= 2:
    print("Infant")
  elif age <= 6:
    print("Child")
  elif age <= 12:
    print("Pre-teen")
  elif age <= 18:
    print("Teenager")
  elif age <= 24:
    print("Young adult")
  elif age <= 49:
    print("Adult")
  elif age <= 64:
    print("Senior citizen")
  else:
    print("Elderly man")
# ----------------------------------
# После блока отступ не нужен    
your_age()
your_age()
your_age()
