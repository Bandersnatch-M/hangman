# Chapter 5. Practice challenge 5. 
"""Создайте словарь, связывающий ваших любимых музыкантов со списком ва-
ших любимых песен, написанных ими."""

# Словарь, связывающий музыкантов со списком написанных ими песен, лучших по моему мнению.
music_dict = dict()
#0 Beatles
music_dict["The Beatles"] = ["Yesterday", "Hey Jude", "Yellow Submarine", "Let It Be", "Here Comes the Sun"]
#1 ABBA
music_dict["ABBA"] = ["Waterloo", "Mamma Mia", "People Need Love", "SOS", "Dancing Queen"]
#2 Queens
music_dict["Queens"] = ["Bohemian Rhapsody", "Bicycle Race", "Don't Stop Me Now", "We Are The Champions", "We Will Rock You"]
#3 Ray Charles
music_dict["Ray Charles"] = ["Georgia on My Mind", "Hit the Road Jack", "Them That Got", "Unchain My Heart", "Stick and Stones"]
#4 Depeche Mode
music_dict["Depeche Mode"] = ["Shake The Disease", "Everything Counts", "Master And Servant", "It Doesn't Matter", "Something To Do"]
#5 Jamiroquai 
music_dict["Jamiroquai"] = ["Too Young to Die", "Space Cowboy", "Virtual Insanity", "Cosmic Girl", "Deeper Underground"]

# Программа:

artist = input("Enter an artist or a band: ")
if artist in music_dict:
    music_dict = music_dict[artist]
    print("The best songs of",artist,"is:",music_dict)
else:
    print("There is no such artists or band in the dictionary or it' been entered wrong.")
