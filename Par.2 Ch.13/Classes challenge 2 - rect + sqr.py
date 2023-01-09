"""В классе Square определите метод change_size, позволяющий передавать
ему число, которое увеличивает или уменьшает (если оно отрицательное)
каждую сторону объекта Square на соответствующее значение."""



# Rectangle

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (self.width + self.length)*2

# Square
class Square():
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        perimeter = self.side*4
        return perimeter
    def change_size(self, n):
        self.change = n
        perimeter = (self.side + self.change)*4
        return perimeter
        
        
           
square_perimeter = Square(5)
print(square_perimeter.calculate_perimeter())
print(square_perimeter.change_size(-6))

