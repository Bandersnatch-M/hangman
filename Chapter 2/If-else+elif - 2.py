Tea = "_Чай" 
Sugar = "_с сахаром"
Milk = "_с молоком"
if Tea == "Чай" and Sugar == "с сахаром" and Milk == "с молоком":
    print(Tea, Sugar, "и", Milk)
elif Tea == "Чай" and Sugar == "с сахаром" and Milk != "с молоком":
    print(Tea, Sugar)
elif Tea == "Чай" and Sugar != "с сахаром" and Milk == "с молоком":
    print(Tea, Milk)
elif Tea == "Чай" and Sugar != "с сахаром" and Milk != "с молоком":
    print(Tea,"без сахара и без молока")
else:
    print("Где мой чай?")
