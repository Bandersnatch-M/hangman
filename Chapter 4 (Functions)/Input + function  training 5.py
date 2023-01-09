# "Input" Function training

def your_age():
    age = input("Please, specify yor age: ")
    age = int(age)
    
if  age < 3:
    print ("You are an infant")
elif age < 12:
    print ("You are a child")
elif age < 18:
    print ("You are a teenager")
else:
    print ("You are an adult")
