from enum import Enum
import random
import time




def game(name):
    playAgain = True
    playerWins = 0
    plays = 0


    def decideWinner(playerChoice):
        aiChoice = random.choice(["1","2","3"])

        def correct(): 
            nonlocal playerWins
            print(f"Congrats {name} you guess right")
            playerWins += 1

        def wrong():
            print(f"Womp Womp {name} you did not guess right")

        
        print(f"\n{name} you chose {playerChoice}")
        print(f"I was thinking about the number {aiChoice}")

        if playerChoice == aiChoice:
            correct()
        else:
            wrong()
        
        time.sleep(3)


    def play():
        nonlocal plays
        validInput = False
        print(f"\n{name}, guess which number I'm thinking of ... 1, 2, or 3")

        playerChoice = input("\n")

        if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
            validInput = True
            plays += 1
            decideWinner(playerChoice)

        if validInput == False:
            print("\n please enter the correct input")
            play()
       

    while playAgain:
        play()

        print(f"\nGame count: {plays}")
        print(f"{name}'s wins: {playerWins}")

        print(f"Play Again {name} ?\n")
        print("Y for Yes and N for No")

        def validateInput():
            nonlocal playAgain
            choice = input("").lower()
            if choice == "y":
                playAgain = True
            elif choice == "n":
                playAgain = False
            else:
                print("Enter a valid choice \n")
                validateInput()
        
        validateInput()