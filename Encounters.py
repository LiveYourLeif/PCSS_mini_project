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

                print(f"You charge your big fucking lazer! Where the fuck did you even get it.")
                break
            elif (playerAction == "Items"):
                print(f"You open your sack of items, and then it shows the items or something idk")
                break
            else:
                print(f"Action not valid.")
                break


run = Encounter
run.story(0)
run.battle(0)

