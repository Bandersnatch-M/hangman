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
# New object (or1) of the class creation 
or1 = Orange(10, "Dark orange")
# Printing the values of the variables - weight and color
print(or1.weight)
print(or1.color)
print(or1.self)

# Changing the values of the variables - weight and color
or1.weight = 100
or1.color = "Blond orange"
print(or1.weight)
print(or1.color)
print(or1)
