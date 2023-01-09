# Horse and Rider

# Horse
class Horse():
    def __init__(self, name, color, owner):
        self.name = name
        self.color = color
        self.owner = owner

# Rider
class Rider():
     def __init__(self, name):
        self.name = name

Paul = Rider("Paul Wambley")
horse = Horse("Spike", "Brown", stan)
print(horse.owner.name)
