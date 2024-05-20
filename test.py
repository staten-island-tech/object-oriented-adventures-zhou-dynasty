import os
import time
from classes import ClassSelection
a = ClassSelection

def Main():
    Choices = ["START", "QUIT"]
    print("Disclaimer: Your data does not save, it resets everytime you play.")
    UserChoice = input("Start | Quit: ").upper()

    while UserChoice not in Choices:
        os.system('cls')
        print("Disclaimer: Your data does not save, it resets everytime you play.")
        UserChoice = input("Start | Quit: ").upper()
    
    if UserChoice == "QUIT":
        os.abort()
    else:
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        
        Username = input("What will your username be? ")
        SelectionClassInstance = ClassSelection(username=Username)
        print(f"Hello {Username}, welcome to Zhou Dynasty!")

        time.sleep(2)
        os.system('cls')

        LearnChoices = ["Y", "N"]
        LearnUserChoice = input("Would you like to learn about the game? Y/N: ").upper()
        while LearnUserChoice not in LearnChoices:
            os.system('cls')
            LearnUserChoice = input("Would you like to learn about the game? Y/N: ").upper()

        while LearnUserChoice == "Y":
            os.system('cls')
            print("What would you like to know about?")

            LearnAboutChoices = ["MOBS", "ROLES", "QUIT"]
            LearnAboutUserChoice = input("Mobs | Roles | Quit").upper()

            while LearnAboutUserChoice not in LearnAboutChoices:
                os.system('cls')
                LearnAboutChoices = ["MOBS", "ROLES", "QUIT"]
                LearnAboutUserChoice = input("Mobs | Roles | Quit").upper()

            if LearnAboutUserChoice == "MOBS":
                pass
            elif LearnAboutUserChoice == "ROLES":
                pass
            elif LearnAboutUserChoice == "QUIT":
                pass
            
            LearnUserChoice = input("Would you like to learn more about the game? Y/N: ").upper()

        start = input("Are you ready to begin your adventure? Y/N: ")
        os.system('cls')
        print("It didn't matter what you picked.")
        time.sleep(1)
        os.system('cls')

        SelectionClassInstance.SelectAClass()

Main()