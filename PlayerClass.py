import ClassStats


class Player(ClassStats):
    playerName = input("Choose your name, wanderer! ")
    print(f"Hello {playerName}!")


    print(f"Which class do you want to be? \n1 = Warrior. 2 = Mage. 3 = Wildcard"
                        f"\nThe Warrior has high defense and a powerful attack, but is very weak to magic"
                        f"\nThe Mage has overly superior magic powers, but is weak to regular hits from enemies"
                        f"\nThe Wild Card has random stats! Roll the dice and prepare your numpys")
    playerChoice = int(input(f"Choose your class, with either the number 1, 2 or 3 : "))

    def get_playerChoice(self):
        return self._playerChoice


    while 1:
        if playerChoice == 1:
            print(f"\nYou have chosen the warrior, great choice {playerName}, get ready for an exciting adventure!")
            warrior = ClassStats.ClassType(50, 7, 10, 5, 10, 0, 2)
            print(f"Your health is: {warrior.health}\n"
                  f"Your strength is: {warrior.get_}\n"
                  f"Your defence is: {warrior.classDefence()}\n"
                  f"Your magic is: {warrior.classMagic()}")
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

