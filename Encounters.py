import ClassStats
import Enemy
import PlayerClass


level = 0  # Current level in the game is set to zero
whoIsFighting = True
gameOverState = 0
playerHealth = ClassStats.health

class battleSystem:
    def __init__(self):
        pass

    def enemyGenerator(self):
        enemyList = []
        for i in range(10):
            newName = Enemy.EnemyType.className(self)
            currentEnemy = Enemy.EnemyType(newName, (i * 5) + 10, (i * 2) + 1, (i * 2) + 3)
            enemyList.append(currentEnemy)

        return enemyList

    enemyGenerator(0)

    def battle(self):
        global whoIsFighting
        global combatOnGoing
        global playerHealth

        enemy = PlayerEncounters.enemyGenerator(0)
        newEnemy = enemy.pop(0)
        enemyName = newEnemy.className()
        enemyStrength = newEnemy.classStrength()
        enemyHP = newEnemy.health

        print(f"A {enemyName} approaches!")
        # Battle between the player and the enemy mob
        while combatOnGoing:
            while enemyHP > 0 and whoIsFighting:
                    playerAction = int(input(f"It is your turn! What do you want to do?\n"
                                             "Melee = 1 | Magic = 2 | Heal = 3 | Stats = 4 \n"))
                    if playerAction == 1:
                        if PlayerClass.Player.playerChoice == 1:
                            currentStrength = PlayerClass.Player.warrior.classStrength() # Varible to set the current strength of the enemy
                            print(f"You swing at the {enemyName} with your sword!")
                            print(f"You dealt {currentStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - currentStrength
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                        if PlayerClass.Player.playerChoice == 2:
                            currentStrength = PlayerClass.Player.mage.classStrength()
                            print(f"You slap the {enemyName} with the back of your hand!")
                            print(f"You dealt {currentStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - currentStrength
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                        if PlayerClass.Player.playerChoice == 3:
                            currentStrength = PlayerClass.Player.wildcard.classStrength()
                            print(f"You roundhouse kick the {enemyName} in the throat!")
                            print(f"You dealt {currentStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - currentStrength
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                    if playerAction == 2:
                        if PlayerClass.Player.playerChoice == 1:
                            currentMagic = PlayerClass.Player.warrior.classMagic()
                            print(f"You try to cast a fireball, but only tickle the {enemyName} with sparks!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                        if PlayerClass.Player.playerChoice == 2:
                            currentMagic = PlayerClass.Player.mage.classMagic()
                            print(f"You use a powerful magic attack on the {enemyName}!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                        if PlayerClass.Player.playerChoice == 3:
                            currentMagic = PlayerClass.Player.wildcard.classMagic()
                            print(f"You cast a magic spell on the {enemyName}!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False

                    if playerAction == 3:
                        if potionCount > 0:
                            print(f"You reach for an Underberg in your pocket.")
                            potionCount -= 1
                            playerHealth += 20
                            if playerHealth > 50:
                                playerHealth = 50  # Sets the player health to maximum hp possible
                            print(f"You drink the Underberg and restore 20 health. You are reinvigorated.")
                            print(f"Underbergs remaining in your pocket: {potionCount}/5.\n")
                            whoIsFighting = False
                        else:
                            print(f"You are out of Underberg!\n")


                    if playerAction == 4:
                        print(f"Your stats: {playerHealth} Health | {potionCount} potions remaining\n"
                              f"{enemyName} stats: {enemyHP} Health\n")


                    if enemyHP <= 0:
                        print(f"{enemyName} has fallen to your powers\n")
                        whoIsFighting = True
                        combatOnGoing = False

            while not whoIsFighting:
                print(f"The {enemyName} slashes at you!")
                print(f"It does {enemyStrength} damage!")
                playerHealth = playerHealth - enemyStrength
                print(f"Your health is now: {playerHealth}\n")
                whoIsFighting = True

    def story(level):
        if level == 0:
            print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n"
                  f"You wander into the wilderness. You hear a rumbling in the bushes, before a appears in front of you.\n")
        if level == 1:
            print("The first beast of your adventure is slain, and you traverse further into the dreadful woods.\n"
                  "Behind some trees, you spot a cave entrance, with a [ENEMY 2] guarding it. You approach\n.")
        if level == 2:
            print("Your dead enemy is left bleeding in the mud, as you push it aside to enter the cave. \n"
                  "Dark and mysterious, the cave sends shivers down your spine. \n"
                  "Mysterious lit candles adorn the sides of the cave’s tall walls, which forms a pathway in the darkness.\n"
                  "You know where you have to go.\n" 
                  "Suddenly the silence of the cave is broken by a deafening roar, as a [ENEMY 3] emerges from the shadows.\n")
        if level == 3:
            print("You continue walking down the dimly lit pathway in the darkness for what feels like hours.\n"
                  "The walls of the cave almost seem to close in on you, as the pathway becomes narrower and narrower, until you can barely stand upright. \n"
                  "You spot an old wooden door with old metal chains keeping it shut, and in front, a [ENEMY 4]\n")
        if level == 4:
            print("After a close fight, you narrowly escape with your life.\n"
                  "During the fight, the metal chains on the door in front of you seemingly broke.\n"
                  "You give the door a hard push, and as it slams open with a loud creak, you find yourself standing in front of a massive mausoleum.\n"
                  "A single stone coffin lays atop a flight of steps.\n"
                  "As you walk closer to investigate, the lid of the coffin bursts into the air, and lands right next to you.\n"
                  "With a roar that rumbles the entire mausoleum, a [MINIBOSS] crawls out of the coffin.\n")
        if level == 5:
            print("Miraculously, you’ve slain the beast.\n"
                  "You take a moment to catch your breath, before you venture further into the mausoleum.\n"
                  "At the back of the room, you spot a large door, with light shining through the cracks. You give it a push, and it creaks open.\n"
                  "Filled with hope of reaching the outside world again, you hurry through the opening, but what meets your eye isn’t the bright sky, but a fiery portal with a [ENEMY 6] crouched in front.\n"
                  "You draw your weapon.\n")


player = battleSystem
for i in range(10):
    player.story(i)
    combatOnGoing = True
    while combatOnGoing:
        player.battle(i)
        if i >= 10:
            combatOnGoing = False



#def gameOverState:
 #   if warriorHP == 0:
  #      gameOverState = 99
   #     warriorHP = 50