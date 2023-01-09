# Magic method - __repr__
class Lion():
       
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
        
lion = Lion("Spike")
print(lion)



