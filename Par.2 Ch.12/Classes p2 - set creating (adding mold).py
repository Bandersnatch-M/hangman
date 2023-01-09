# Creation of the class "Orange".
# Method "__init__", first parameter of the method is "self".

# Next parametrs for object creation - is weight (w) and color (c).


# Code for class "Orange" creation
class Orange:
# Body (object) of class, where def __init__(self) is the method of object creation.
# Parameters followed after "self" - chrachters of the class.
# Adding "mold" characteristic using method (def rot(self, days, temp):) inside class
    def __init__(self, w, c):
        """weight in gramms"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Class Orange created!")
    def rot(self, days, temp):
        self.mold = days * temp
        """days - number of days from harvesting, temp - aver. store temperature"""
# New objects of the class creating
orange = Orange(6, "Blonde orange")
print(orange.mold)
orange.rot(15, 45)
print(orange.mold)


