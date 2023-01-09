"""В классе Square определите метод change_size, позволяющий передавать
ему число, которое увеличивает или уменьшает (если оно отрицательное)
каждую сторону объекта Square на соответствующее значение."""

# Datasetxy
class Datasetxy():
    list_x = []
    list_y = []
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_x.append(self.x)
        self.list_y.append(self.y)

print("Hello! Please enter 10 variable for x and y.")       
n = 0
while n < 10:
    x = input("Please enter x: ")
    x = float(x)
    y = input("Please enter y: ")
    y = float(y)
    data = Datasetxy(x, y)
    n += 1
    print("Thank you!")

print("Great! All parameters has been collected to the dataset.")
print("Dataset for x:", Datasetxy.list_x)
print("Dataset for y:", Datasetxy.list_y)


