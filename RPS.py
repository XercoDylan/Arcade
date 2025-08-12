from enum import Enum
import random
import time
class RPS(Enum):
    Rock = {"name": "Rock", "value": 1}
    Paper = {"name": "Paper", "value": 2}
    Scissors = {"name": "Scissors", "value": 3}



def game(name):
    playAgain = True
    playerWins = 0
    draws = 0
    aiWins = 0
    plays = 0


    def decideWinner(playerChoice, aiChoice):
        def playerWin(): 
            nonlocal playerWins
            print(f"Congrats {name} you win")
            playerWins += 1

        def aiWin():
            nonlocal aiWins
            print(f"The AI wins")
            print(f"Sorry {name}")
            aiWins += 1
        
        def draw():
            nonlocal draws
            print(f"Its a draw")
            draws += 1
        
        print(f"\n{name} you chose {playerChoice}")
        print(f"The AI chose {aiChoice}")

        if playerChoice == "Rock" and aiChoice == "Scissors":
            playerWin()
        elif playerChoice == "Scissors" and aiChoice == "Paper":
            playerWin()
        elif playerChoice == "Paper" and aiChoice == "Rock":
            playerWin()
        elif playerChoice == aiChoice:
            draw()
        else:
            aiWin()
        
        time.sleep(3)


    def play():
        nonlocal plays
        validInput = False
        print(f"\n{name}, please enter ...")
        for choice in RPS:
            print(f"{choice.value["value"]} for {choice.value["name"]}")

        playerChoice = input("\n").lower()

        for choice in RPS:
            if playerChoice == str(choice.value["value"]):
                validInput = True
                plays += 1
                aiChoice = random.choice(list(RPS))
                decideWinner(choice.value["name"] , aiChoice.value["name"])
            
        if validInput == False:
            print("\n please enter the correct input")
            play()
       

    while playAgain:
        play()

        print(f"\nGame count: {plays}")
        print(f"AI wins: {aiWins}")
        print(f"{name}'s wins: {playerWins}")
        print(f"Draws: {draws}")

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


       
            
        


