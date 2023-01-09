# Определить класс Circle методом area, подсчитывающим и возвращающим площадь круга.
# Затем создайте объект Circle, вызовите в нем метод area и выведите результат.
# Воспользуйтесь функцией pi из модуля math.

class Circle:
    def __init__(self, d):
        self.diameter = d
        print("The class of Circle created")
    def area(self):
        import math
        pi = math.pi
        return pi*self.diameter**2/4
         
circle_square = Circle(4)
print(circle_square.area())


        
