"""В классе Square определите метод change_size, позволяющий передавать
ему число, которое увеличивает или уменьшает (если оно отрицательное)
каждую сторону объекта Square на соответствующее значение."""

# Shape
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        perimeter = (self.width + self.length)*2
        return perimeter
    def what_am_i(self):
            if self.width == self.length:
                print("I am a shape of square")
            else:
                print("I am a shape of rectangle")

i_am_shape = Shape(5,5)
print(i_am_shape.what_am_i())


