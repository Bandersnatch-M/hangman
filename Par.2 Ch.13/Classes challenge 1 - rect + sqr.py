



# Rectangle

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (self.width + self.length)*2

# Square
class Square():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        if self.width >= 0:
            if self.length >= 0:
                (self.width + self.length)*2
        else:
           print(0)
    def change_sides(self, n):
            self.width = w + n
            self.length = l + n
        
        
  
square_perimeter = Square(5,5)
rectangle_perimeter = Rectangle(5,6)
print(square_perimeter.calculate_perimeter())
print(rectangle_perimeter.calculate_perimeter())
print(square_perimeter.change_sides(10))

