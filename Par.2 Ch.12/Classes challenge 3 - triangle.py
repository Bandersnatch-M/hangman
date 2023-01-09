# Определить класс Triangle методом area, подсчитывающим и возвращающим площадь.

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("The class of Triangle created")
    def area(self):
        return self.base*self.height/2
  
triangle_square = Triangle(4.5,6.5)
print(triangle_square.area())


        
