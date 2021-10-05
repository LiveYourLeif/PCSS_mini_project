import Enemy
import PlayerClass


class Encounter(Enemy.EnemyType):

    def story(self):
        print("")
        print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n "
              "You wander out into the wilderness. ")

    def battle(self):
        currentEnemy = Enemy.EnemyType(0, 10, 1, 3, 1, 3, 1, 3)
        print(f"A {currentEnemy.className()} approaches!")
        print(f"{currentEnemy.className()} health: {currentEnemy.classHP()}\n"
              f"{currentEnemy.className()} strength: {currentEnemy.classStrength()}\n"
              f"{currentEnemy.className()} defence: {currentEnemy.classDefence()}\n"
              f"{currentEnemy.className()} magic: {currentEnemy.classMagic()}")


        #while(Enemy.classHP > 0):
        playerAction = input(f"It is your turn! What do you want to do? (Type an action): ")
        while 1:
                if (playerAction == "Attack"):
                    print(f"You swing at the enemy with your sword!")
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

