
import argparse
import sys
import RPS
import Guess
import time
from enum import Enum

class Games(Enum):
    RPS = {"name": "Rock Paper Scissors","index": 1, "module": RPS}
    Guess = {"name": "Guess the Number","index": 2, "module": Guess}


def arcade():
    playAgain = True
    parser = argparse.ArgumentParser(prog="Arcade", description= "An arcade game that contains two games")
    parser.add_argument("-n","--name",metavar="name", required= True, help= "Name of the player")
    args = parser.parse_args()

    print(f"{args.name}, welcome to the Arcade! 🤖 \n")

    def menu():
        validOption = False
        print("Please choose a game: \n")
        for game in Games:
            print(f"{game.value["index"]} = {game.value["name"]}" )
        
        print("Or press \"x\" to exit the Arcade \n")

        choice = input("")

        if choice == "X":
            validOption = True
            sys.exit()

        for game in Games:
            if choice == str(game.value["index"]):
                validOption = True
                game.value["module"].game(args.name)
        
        if validOption == False:
            print("\n Please select a valid option \n")
            time.sleep(4)
            menu()

        
        

    while playAgain:
        menu()



if __name__ == "__main__":
    arcade()