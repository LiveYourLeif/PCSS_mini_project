import Enemy
import PlayerClass


class Encounter():

    def story(self):
        print("")
        print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n"
              "You wander out into the wilderness. ")

    def battle(self):
        # Make a list with 10 objects called enemyList
        enemylist = []
        for i in range (10):
            currentEnemy = Enemy.EnemyType(0, 10, 1, 3, 1, 3, 1, 3)
            enemylist.append(currentEnemy)

        # Pop the first element of enemyList and make it a new enemy
        newEnemy = enemylist.pop(0)

        # Print the name of the new enemy
        firstEnemyName = newEnemy.className()
        firstEnemyHP = newEnemy.classHP()
        print(f"A {firstEnemyName} approaches!")


        while firstEnemyHP > 0:
            playerAction = int(input(f"It is your turn! What do you want to do?"))
            if playerAction == 1:
                if PlayerClass.Player.playerChoice == 1:
                    print(f"You swing at the enemy with your sword!")
                    print(f"You dealt {PlayerClass.Player.warrior.classStrength()} damage to the {firstEnemyName}")
                    print(f"{firstEnemyName} health: {firstEnemyHP - PlayerClass.Player.warrior.classStrength()}")
                    break
                if PlayerClass.Player.playerChoice == 2:
                    print(f"You slap the enemy with the back of your hand!")
                    print(f"You dealt {PlayerClass.Player.mage.classStrength()} damage to the {firstEnemyName}")
                    print(f"{firstEnemyName} health: {firstEnemyHP - PlayerClass.Player.mage.classStrength()}")
                    break
                if PlayerClass.Player.playerChoice == 3:
                    print(f"You roundhouse kick the enemy in the throat!")
                    print(f"You dealt {PlayerClass.Player.wildcard.classStrength()} damage to the {firstEnemyName}")
                    print(f"{firstEnemyName} health: {firstEnemyHP - PlayerClass.Player.wildcard.classStrength()}")
                    break

            #if PlayerClass.Player.playerChoice == 2:
                #if Playerclass.Player.player




run = Encounter
run.story(0)
run.battle(0)

