from Stats import Stats as Stats #Stats


class Player(Stats):
    playerName = input("Choose your name, wanderer! ")
    print(f"Hello {playerName}!")

    print(f"Which class do you want to be? \n1 = Warrior. 2 = Mage. 3 = Wildcard"
                        f"\nThe Warrior has high defense and a powerful attack, but is very weak to magic"
                        f"\nThe Mage has overly superior magic powers, but is weak to regular hits from enemies"
                        f"\nThe Wild Card has random stats! Roll the dice and prepare your numpys")
    playerChoice = int(input(f"Choose your class, with either the number 1, 2 or 3 : "))

    while 1:
        if playerChoice == 1:
            print(f"\nYou have chosen the warrior, great choice {playerName}, get ready for an exciting adventure!")
            break
        elif playerChoice == 2:
            print(f"\nYou have chosen the mage, great choice {playerName}, get ready for an exciting adventure!")
            break
        elif playerChoice == 3:
            print(f"\nYou have chosen the wild card, brave choice {playerName}, get ready for an exciting adventure!")
            break
        else:
            print(f"Your choice was not a class, {playerName}")
            playerChoice = int(input(f"Choose your class, with either the number 1, 2 or 3 : "))


#