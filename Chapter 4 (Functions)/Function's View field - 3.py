# Практика с переменными. Область видимости.
# Глобальная и локальная область видимости.

x = 100

def f():
    global x
    x += 1
    print (x)

f()

