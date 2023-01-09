"""В классе Square определите метод change_size, позволяющий передавать
ему число, которое увеличивает или уменьшает (если оно отрицательное)
каждую сторону объекта Square на соответствующее значение."""



# Square
class Square():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (self.width + self.length)*2


# Rectangle

class Rectangle(Square):
    pass
   
perimeter = Rectangle(5,6)
print(perimeter.calculate_perimeter())


