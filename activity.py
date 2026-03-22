from juegos.hangman import play_hangman
from juegos.reverse import play_reverse
from juegos.tictactoe import play_tictactoe

dic = {
    "1": play_hangman,
    "2": play_reverse,
    "3": play_tictactoe
}

while True: 
    print("What game do you want to play?")
    print("1- Hangman")
    print("2- Reverse")
    print("3- Tictactoe")
    print("Press any other key to leave the menu.")
    option = input ("Choose your option: ")
    if option in dic.keys():
        dic[option]()
    else:
        answer = input('Do you want to exit the program? (yes or no) ').lower()
        if answer.startswith('y'):
            print("Goodbye!")
            break