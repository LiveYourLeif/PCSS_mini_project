import ClassStats


class Player(ClassStats.ClassType): # Player class som extender classType
    playerName = input("Choose your name, wanderer! ")
    print(f"Hello {playerName}!")
    # Første dialog hvor spilleren bliver præsenteret for de forskellige class typer i "spillet".
    print(f"Which class do you want to be? \n1 = Warrior. 2 = Mage. 3 = Wildcard"
                        f"\nThe Warrior has high defense and a powerful attack, but is very weak to magic"
                        f"\nThe Mage has overly superior magic powers, but is weak to regular hits from enemies"
                        f"\nThe Wild Card has random stats! Roll the dice and prepare your numpys")
    playerChoice = int(input(f"Choose your class, with either the number 1, 2 or 3 : "))

    # While-loop hvor brugeren bliver bedt om at vælge hvilken class de ønsker at spille. Derudover bliver der efter
    # brugerens valg lavet et objekt af den type, som brugeren vælger at spille og dets attributer.
    while 1:
        if playerChoice == 1:
            print(f"\nYou have chosen the warrior, great choice {playerName}, get ready for an exciting adventure!")
            warrior = ClassStats.ClassType(50, 7, 10, 5, 10, 0, 2) # Creates object for the class Warrior
            print(f"Your health is: {warrior.classHP()}\n"
                  f"Your strength is: {warrior.classStrength()}\n"
                  f"Your defence is: {warrior.classDefence()}\n"
                  f"Your magic is: {warrior.classMagic()}")
            break
        elif playerChoice == 2:
            print(f"\nYou have chosen the mage, great choice {playerName}, get ready for an exciting adventure!")
            mage = ClassStats.ClassType(50, 3, 6, 3, 5, 8, 10) # Creates object for the class Mage
            print(f"Your health is: {mage.classHP()}\n"
                  f"Your strength is: {mage.classStrength()}\n"
                  f"Your defence is: {mage.classDefence()}\n"
                  f"Your magic is: {mage.classMagic()}")
            break
        elif playerChoice == 3:
            print(f"\nYou have chosen the wild card, brave choice {playerName}, get ready for an exciting adventure!")
            wildcard = ClassStats.ClassType(50, 1, 10, 1, 10, 1, 10) # Creates object for the class Wildcard
            print(f"Your health is: {wildcard.classHP()}\n"
                  f"Your strength is: {wildcard.classStrength()}\n"
                  f"Your defence is: {wildcard.classDefence()}\n"
                  f"Your magic is: {wildcard.classMagic()}")
            break
        else:
            print(f"Your choice was not a class, {playerName}")
            playerChoice = int(input(f"Choose your class, with either the number 1, 2 or 3 : "))

