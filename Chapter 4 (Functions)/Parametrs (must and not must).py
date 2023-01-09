# Обязательные и необязательные параметры в функции. Практика

def f(x=2):
    return x**x
print (f())
print (f(5))

# Усложняем

def Summum(x, y=10):
    return x*x + y
result = Summum (5)
print(result)
