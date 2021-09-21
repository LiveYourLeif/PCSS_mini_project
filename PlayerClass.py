class Player:
    playerName = input("Choose your name wanderer! ")
    print(f"Hello {playerName}!")

    print (f"Which class do you want to be? \n1 = Warrior. 2 = Mage. 3 = Wildcard"
                        f"\nThe Warrior has high defense and a powerful attack, but is very weak to magic"
                        f"\nThe Mage has overly superior magic powers, but is weak to regular hits from enemies"
                        f"\nThe Wild Card has random stats! Roll the dice and prepare your numpys")
    playerClass = input(f"Choose your class, with either the number 1, 2 or 3")

    playerChoice = int(playerClass) # Secures the input from the user when choosing their class

    if playerChoice > 3 or playerChoice < 1:
       print(f"Your choice was not a class {playerName}")
       playerClass = input(f"Choose again, a number between 1, 2 or 3")

    if playerChoice == 1:
        print(f"\nYou have chosen the warrior, great choice {playerName}, get ready for an exciting adventure!")
    if playerChoice == 2:
        print(f"\nYou have chosen the mage, great choice {playerName}, get ready for an exciting adventure!")
    if playerChoice == 3:
        print(f"\nYou have chosen the wild card, brave choice {playerName}, get ready for an exciting adventure!")

