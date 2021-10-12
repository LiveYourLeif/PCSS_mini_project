import Enemy
import PlayerClass



class Encounter():

    def story(self):
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
        enemyName = newEnemy.className()
        enemyHP = newEnemy.classHP()
        print(f"A {enemyName} approaches!")

        # Battle between the player and the enemy mob
        while enemyHP > 0:
            playerAction = int(input(f"It is your turn! What do you want to do?\n"
                                     f"Press 1 for a melee attack.\n"
                                     f"Press 2 for a magic attack. \n"))
            if playerAction == 1:
                if PlayerClass.Player.playerChoice == 1:
                    currentStrength = PlayerClass.Player.warrior.classStrength() # Varible to set the current strength of the enemy
                    print(f"Enemy health: {currentEnemyHP}")
                    print(f"You swing at the enemy with your sword!")
                    print(f"You dealt {currentStrength} damage to the {enemyName}")
                    print(f"{enemyName} health: {currentEnemyHP - currentStrength} \n")

                if PlayerClass.Player.playerChoice == 2:
                    currentStrength = PlayerClass.Player.mage.classStrength()
                    print(f"You slap the enemy with the back of your hand!")
                    print(f"You dealt {currentStrength} damage to the {enemyName}")
                    print(f"{enemyName} health: {enemyHP - currentStrength} \n")

                if PlayerClass.Player.playerChoice == 3:
                    currentStrength = PlayerClass.Player.wildcard.classStrength()
                    print(f"You roundhouse kick the enemy in the throat!")
                    print(f"You dealt {PlayerClass.Player.wildcard.classStrength()} damage to the {enemyName}")
                    print(f"{enemyName} health: {enemyHP - currentStrength} \n")


            if playerAction == 2:
                if PlayerClass.Player.playerChoice == 1:
                    currentMagic = PlayerClass.Player.warrior.classMagic()
                    print(f"You try to cast a fireball, but only tickle the enemy with sparks!")
                    print(f"You dealt {currentMagic} damage to the {enemyName}")
                    print(f"{enemyName} health: {enemyHP - currentMagic} \n")

                if PlayerClass.Player.playerChoice == 2:
                    currentMagic = PlayerClass.Player.mage.classMagic()
                    print(f"You use a powerful magic attack on the enemy!")
                    print(f"You dealt {currentMagic} damage to the {enemyName}")
                    print(f"{enemyName} health: {enemyHP - currentMagic} \n")

                if PlayerClass.Player.playerChoice == 3:
                    currentMagic = PlayerClass.Player.wildcard.classMagic()
                    print(f"You cast a magic spell on the enemy!")
                    print(f"You dealt {PlayerClass.Player.wildcard.classMagic()} damage to the {enemyName}")
                    print(f"{enemyName} health: {enemyHP - currentMagic} \n")

            if enemyHP <= 0:
                print("You killed the enemy, good job, mom get the camera")
                break





run = Encounter
run.story(0)
run.battle(0)

