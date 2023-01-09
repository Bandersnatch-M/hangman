# Chapter 5. Practice challenge 1. 
"""Создайте список кортежей, где каждый кортеж содержит долготу и широту
любого места, в котором вы жили или которое посещали."""

print("Список координат городов Европы, которые я посетил:")
leaving_list = []
#0 "London"
london = (51.507325, -0.127716)
#1 "Paris"
paris = (48.856615, 2.351503)
#2 "Edinburgh the capitol of Scotland"
edinburgh = (55.954007, -3.190219)
#3 "Bern the capitol of Switzerland"
bern = (46.947883, 7.440319)

leaving_list.append(london)
leaving_list.append(paris)
leaving_list.append(edinburgh)
leaving_list.append(bern)

print("London", leaving_list[0])
print("Paris", leaving_list[1])
print("Edinburgh", leaving_list[2])
print("Bern", leaving_list[3])
