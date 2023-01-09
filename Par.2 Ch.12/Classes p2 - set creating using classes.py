# Creation of the class "Orange".
# Method "__init__", first parameter of the method is "self".

# Next parametrs for object creation - is weight (w) and color (c).


# Code for class "Orange" creation
class Orange:
# Body (object) of class, where def __init__(self) is the method of object creation.
# Parameters followed after "self" - chrachters of the class. 
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Class Orange created!")
# New objects of the class creating
or1 = Orange(4, "Blonde orange")
or2 = Orange(8, "Dark orange")
or2 = Orange(14, "Yellow orange")

# Adding "mold" characteristic
