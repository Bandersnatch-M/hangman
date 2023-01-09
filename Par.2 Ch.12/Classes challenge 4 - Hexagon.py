# Определить класс Hexagone методом calculate_perimeter, который возвращает длинну периметра.
# Создать объект класса, который возвращает и выводит длинну периметра.

class Hexagone:
    def __init__(self, sl):
        self.side_length = sl
        print("The class of Hexagone created")
    def calculate_perimeter(self):
        return self.side_length*6

perimeter = Hexagone(8)
print(perimeter.calculate_perimeter())


        
