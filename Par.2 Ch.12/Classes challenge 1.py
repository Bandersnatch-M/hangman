# Определить класс Apple с четырьмя переменными экземпляра,
# представляющими четыре свойства яблока.
# 4 свойства - name, color, taste, origin. 

class Apple:
    def __init__(self, sn, c, t, o):
        self.sort_name = sn
        self.color = c
        self.taste = t
        self.origin = o
        print("The class of apple created")

apple_ant = Apple("Antonovka", "Greenish-yellow", "Granular sour-sweet", "Russia")
apple_fuji = Apple("Fuji", "Yellow-red", "Crispy-sweet", "Japan")
apple_gd = Apple("Golden Delicious", "Yellow", "Sweet", "USA")
apple_mac = Apple("McIntosh", "Whitish-yellow-pink", "juicy sweet and sour", "Canada")

print(apple_fuji.taste)


        
