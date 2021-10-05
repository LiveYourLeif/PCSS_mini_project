import Enemy
import PlayerClass


class Encounter():

    def story(self):
        print("")
        print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n"
              "You wander out into the wilderness. ")

    def battle(self):
        # Make a list with 10 objects called enemyList
        for i in range(10):
            enemylist = []
            currentEnemy = Enemy.EnemyType(0, 10, 1, 3, 1, 3, 1, 3)
            enemylist.append(currentEnemy)

        # Pop the first element of enemyList and make it a new enemy
        newEnemy = enemylist.pop(0)

        # Print the name of the new enemy
        print(f"A {newEnemy.className()} approaches!")


        playerAction = int(input(f"It is your turn! What do you want to do?"))
        while 1:
                if playerAction == 1:
                    if PlayerClass.Player.playerChoice == 1:
                        print(f"You swing at the enemy with your sword!")
                        print(f"you damaged the {newEnemy.className()} {PlayerClass.Player.warrior.classStrength()} damage")

                    break
                elif (playerAction == "Magic"):

                    print(f"You ready your stance and cast a thunderous magic spell!")
                    break
                elif (playerAction == "Items"):
                    print(f"Inside your pouch, you find plenty of helpful items, such as:")
                    break
                elif (playerAction == "BattleHelp"):
                    print(f"List of commands in battle:")
                    print(f"'Attack' - Deal physical damage to the enemy")
                    print(f"'Magic' - Deal magical damange to the enemy")
                    print(f"'Items' - Use an item, if you have one")
                    break
                else:
                    print(f"Action not valid. Type 'BattleHelp' for list of actions.")
                    playerChoice = input(f"It is your turn! What do you want to do? (Type an action): ")
                    break


run = Encounter
run.story(0)
run.battle(0)

