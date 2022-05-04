import random


def hangman():
    words_list = ["pencil", "penguin", "zodiac", "centipede", "grizzly", "mountain", "axe", "camping", "chair", "fire", "tree"]
    random_number = random.randint(0, 11)
    word = words_list[random_number]
    wrong = 0
    stages = ["",
             "__________      ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    print("Welcome to Hangman!")
    print("\n ------ Number of letters in the word.------ \n", board)
    win = False
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "_" not in board:
            print("You win! The word was {}!".format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0 : wrong]))
        print("You lose!")

hangman()



