import Enemy


class Encounter(Enemy.EnemyType):

    def dialogs(self):
        enemyName = Enemy.EnemyType.chooseName(0)
        firstEnemy = Enemy.EnemyType(10, 1, 3, 1, 3, 1, 3)
        print(f"A {enemyName} approaches!")
        print(f"{enemyName} health: {firstEnemy.classHP()}\n"
              f"{enemyName} strength: {firstEnemy.classStrength()}\n"
              f"{enemyName} defence: {firstEnemy.classDefence()}\n"
              f"{enemyName} magic: {firstEnemy.classMagic()}")

        playerAction = input(f"It is your turn! What do you want to do? (Type an action): ")
        while 1:
            if (playerAction == "Attack"):
                print(f"You swing at the enemy with your di- I mean sword!")
                break
            elif (playerAction == "Magic"):

                print(f"You charge your big fucking lazer! Where the fuck did you even get it.")
                break
            elif (playerAction == "Items"):
                print(f"You open your sack of items, and then it shows the items or something idk")
                break
            else:
                print(f"Action not valid.")


    #def fight(self):




test = Encounter
test.dialogs(0)

