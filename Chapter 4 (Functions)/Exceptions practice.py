# Практика. Работа с исключениями.

def Dev():
    print ("Давайте разделим A на B.")
    try:
        a = input ("Введите A (число цифрами): ")
        b = input ("Введите B (число цифрами): ")
        a = int(a)
        b = int(b)
        result = a / b
        print ("Получилось:", result)
    except ZeroDivisionError:
        print ("К сожалению по правилам на ноль делить нельзя!")
    except ValueError:
        print ("Будьте внимательны, значение можно указывать только числами!")
Dev()
