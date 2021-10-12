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
        EnemyName = newEnemy.className()
        EnemyHP = newEnemy.classHP()
        print(f"A {EnemyName} approaches!")

        # Battle between the player and the enemy mob
        while EnemyHP > 0:
            playerAction = int(input(f"It is your turn! What do you want to do?"))
            if playerAction == 1:
                if PlayerClass.Player.playerChoice == 1:
                    currentStrength = PlayerClass.Player.warrior.classStrength() # Varible to set the current strength of the enemy
                    print(f"You swing at the enemy with your sword!")
                    print(f"You dealt {currentStrength} damage to the {EnemyName}")
                    print(f"{EnemyName} health: {EnemyHP - currentStrength}")

                if PlayerClass.Player.playerChoice == 2:
                    currentStrength = PlayerClass.Player.mage.classStrength()
                    print(f"You slap the enemy with the back of your hand!")
                    print(f"You dealt {currentStrength} damage to the {EnemyName}")
                    print(f"{EnemyName} health: {EnemyHP - currentStrength}")

                if PlayerClass.Player.playerChoice == 3:
                    currentStrength = PlayerClass.Player.wildcard.classStrength()
                    print(f"You roundhouse kick the enemy in the throat!")
                    print(f"You dealt {PlayerClass.Player.wildcard.classStrength()} damage to the {EnemyName}")
                    print(f"{EnemyName} health: {EnemyHP - currentStrength}")


            #if PlayerClass.Player.playerChoice == 2:
                #if Playerclass.Player.player




run = Encounter
run.story(0)
run.battle(0)

