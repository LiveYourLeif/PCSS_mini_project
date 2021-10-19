import Enemy
import PlayerClass
import ipdb

level = 0  # Current level in the game is set to zero
whoIsFighting = True

class PlayerEncounters:
    def __init__(self):
        pass

    def story(level):
        if level == 0:
            print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n"
              "You wander out into the wilderness. ")
        if level == 1:
            print("This is the SECOND LEVEL! You are in a forest now and you see a shadow move!")
        if level == 2:
            print("THis is the THIRD LEVEL! You are doing a nasty whip and nae nae when you see a monster!")

    def battle(self):
        global whoIsFighting
        global combatOnGoing
        global enemyHP
        # Make a list with 10 objects called enemyList
        enemylist = []
        for i in range(10):
            newName = Enemy.EnemyType.className(self)
            currentEnemy = Enemy.EnemyType(newName, 10+(i*5), 1, 3, 1, 3, 1, 3)
            enemylist.append(currentEnemy)

        # Pop the first element of enemyList and make it a new enemy
        newEnemy = enemylist.pop(0)

        # Print the name of the new enemy
        enemyName = newEnemy.name
        enemyHP = newEnemy.health
        print(f"A {enemyName} approaches!")
        # Battle between the player and the enemy mob
        while enemyHP > 0 and whoIsFighting:
                playerAction = int(input(f"It is your turn! What do you want to do?"))
                if playerAction == 1:
                    if PlayerClass.Player.playerChoice == 1:
                        currentStrength = PlayerClass.Player.warrior.classStrength() # Varible to set the current strength of the enemy
                        print(f"You swing at the {enemyName} with your sword!")
                        print(f"You dealt {currentStrength} damage to the {enemyName}")
                        enemyHP = enemyHP - currentStrength
                        print(f"{enemyName} health: {enemyHP} \n")

                    if PlayerClass.Player.playerChoice == 2:
                        currentStrength = PlayerClass.Player.mage.classStrength()
                        print(f"You slap the {currentEnemy} with the back of your hand!")
                        print(f"You dealt {currentStrength} damage to the {enemyName}")
                        enemyHP = enemyHP - currentStrength
                        print(f"{enemyName} health: {enemyHP} \n")

                    if PlayerClass.Player.playerChoice == 3:
                        currentStrength = PlayerClass.Player.wildcard.classStrength()
                        print(f"You roundhouse kick the {enemyName} in the throat!")
                        print(f"You dealt {currentStrength} damage to the {enemyName}")
                        enemyHP = enemyHP - currentStrength
                        print(f"{enemyName} health: {enemyHP} \n")

                if playerAction == 2:
                    if PlayerClass.Player.playerChoice == 1:
                        currentMagic = PlayerClass.Player.warrior.classMagic()
                        print(f"You try to cast a fireball, but only tickle the {enemyName} with sparks!")
                        print(f"You dealt {currentMagic} damage to the {enemyName}")
                        enemyHP = enemyHP - currentMagic
                        print(f"{enemyName} health: {enemyHP} \n")

                    if PlayerClass.Player.playerChoice == 2:
                        currentMagic = PlayerClass.Player.mage.classMagic()
                        print(f"You use a powerful magic attack on the {enemyName}!")
                        print(f"You dealt {currentMagic} damage to the {enemyName}")
                        enemyHP = enemyHP - currentMagic
                        print(f"{enemyName} health: {enemyHP} \n")

                    if PlayerClass.Player.playerChoice == 3:
                        currentMagic = PlayerClass.Player.wildcard.classMagic()
                        print(f"You cast a magic spell on the {enemyName}!")
                        print(f"You dealt {currentMagic} damage to the {enemyName}")
                        enemyHP = enemyHP - currentMagic
                        print(f"{enemyName} health: {enemyHP} \n")
                if enemyHP <= 0:
                    #ipdb.set_trace()
                    print(f"{enemyName} has fallen to your powers\n")
                    whoIsFighting = True
                    combatOnGoing = False


    def enemyBattle(self):
        print("enemy does something")
        #whoIsFighting = True


player = PlayerEncounters
for i in range(10):
    player.story(i)
    combatOnGoing = True
    while combatOnGoing:
        if whoIsFighting:
            player.battle(i)
            whoIsFighting = False
        else:
            if(enemyHP > 0):
                player.enemyBattle(i)
            whoIsFighting = True

