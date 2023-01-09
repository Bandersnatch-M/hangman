def hangman(word):
    wrong = 0 # кол-во не правильных предположений
    stages = ["",                   # Строки вывода виселицы (список)
              "________        ",
              "|       |       ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "] 

    rletters = list(word) # список букв в слове word
    board = ["__"]*len(word) # список строк "__" в слове word
    win = False
    print("Welcome for the execution!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter a letter: "
        guess = input(msg)
        if guess in rletters:
            letter_index = rletters.index(guess)
            board[letter_index] = guess
            rletters[letter_index] = '$'
        else:
            wrong += 1
        print(("  ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
              print ("You win! The word is: ")
              print ("  ".join(board))
              win = True
              break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("\nGame over. You are executed! The word was: {}.".format(word))
        

hangman("home")
