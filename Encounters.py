import random
import sys

import ClassStats
import Enemy
import PlayerClass
import Lore


level = 1
whoIsFighting = True
playerHealth = ClassStats.health
potionCount = 5
score = 0


class battleSystem:
    def enemyGenerator(self):
        enemyList = []
        for i in range(10):
            newName = Enemy.EnemyType.className(self)
            currentEnemy = Enemy.EnemyType(newName, (i * 5) + 10, (i * 2) + 1, (i * 2) + 2)
            enemyList.append(currentEnemy)
        return enemyList

    enemy = enemyGenerator(0)

    def normalBattle(self):
        global enemyName
        global enemyStrength
        global enemyHP
        newEnemy = battleSystem.enemy.pop(0)
        enemyName = newEnemy.className()
        enemyStrength = newEnemy.classStrength()
        enemyHP = newEnemy.health

        print(f"A {enemyName} approaches!")
        # Battle between the player and the enemy mob
        return enemyName, enemyStrength, enemyHP

    def bossBattle(self):
        global minibossName
        global minibossStrength
        global minibossHP
        miniboss = Enemy.EnemyType("Breitthøvd", 50, 10, 15)
        minibossName = miniboss.name
        minibossStrength = random.randint(miniboss.strengthL, miniboss.strengthU)
        minibossHP = miniboss.health
        print(f"A giant {minibossName} appears in front of you!")

    def potionReplenish(self):
            print("Your Underberg stock is replenished!")
            potionCount = 5
            print(f"Underbergs remaining in your pocket: {potionCount}/5.\n")

    def battle(enemyName, enemyStrength, enemyHP):
        global whoIsFighting
        global combatOnGoing
        global playerHealth
        global potionCount
        global score

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
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 2:
                            currentStrength = PlayerClass.Player.mage.classStrength()
                            print(f"You slap the {enemyName} with the back of your hand!")
                            print(f"You dealt {currentStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - currentStrength
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 3:
                            currentStrength = PlayerClass.Player.wildcard.classStrength()
                            print(f"You roundhouse kick the {enemyName} in the throat!")
                            print(f"You dealt {currentStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - currentStrength
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                    if playerAction == 2:
                        if PlayerClass.Player.playerChoice == 1:
                            currentMagic = PlayerClass.Player.warrior.classMagic()
                            print(f"You try to cast a fireball, but only tickle the {enemyName} with sparks!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 2:
                            currentMagic = PlayerClass.Player.mage.classMagic()
                            print(f"You use a powerful magic attack on the {enemyName}!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 3:
                            currentMagic = PlayerClass.Player.wildcard.classMagic()
                            print(f"You cast a magic spell on the {enemyName}!")
                            print(f"You dealt {currentMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - currentMagic
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                    if playerAction == 3:
                        if potionCount > 0:
                            print(f"You reach for an Underberg in your pocket.")
                            potionCount -= 1
                            playerHealth += 30
                            if level < 4:
                                if playerHealth > 50:
                                    playerHealth = 50
                            else:
                                if playerHealth > 100:
                                    playerHealth = 100
                            print(f"You drink the Underberg and restore 20 health. You are reinvigorated.")
                            print(f"Underbergs remaining in your pocket: {potionCount}/5.\n")
                            whoIsFighting = False
                            score += 1
                        else:
                            print(f"You are out of Underberg!\n")


                    if playerAction == 4:
                        print(f"Your stats: {playerHealth} Health | {potionCount} potions remaining\n"
                              f"{enemyName} stats: {enemyHP} Health\n")


                    if enemyHP <= 0:
                        if enemyName == "Breitthøvd":
                            print("\nYou defeated the Breitthøvd and absorb its powers!")
                            playerHealth = 100
                            print(f"Your max health is now: {playerHealth}\n")
                        else:
                            print(f"{enemyName} has fallen to your powers\n")
                            playerHealth += 30

                        if level < 4:
                            if playerHealth > 50:
                                playerHealth = 50
                        else:
                            if playerHealth > 100:
                                playerHealth = 100
                        print(f"You regain some of your energy!\n"
                              f"Player health: {playerHealth}\n")
                        whoIsFighting = True
                        combatOnGoing = False

            while not whoIsFighting:
                print(random.choice(Lore.enemyTaunts(enemyName)))
                print(f"It does {enemyStrength} damage!")
                playerHealth = playerHealth - enemyStrength
                if playerHealth > 0:
                    print(f"Your health is now: {playerHealth}\n")
                    whoIsFighting = True
                else:
                    print(f"{PlayerClass.Player.playerName} has been laid to rest.")
                    whoIsFighting = True
                    combatOnGoing = False
                    sys.exit()

        return score


for i in range(5):
    combatOnGoing = True
    while combatOnGoing:
        level = i
        print(f"LEVEL: {level}")
        if playerHealth > 0:
            if i < 4 or i > 4:
                Lore.story(i)
                battleSystem.normalBattle(i)
                battleSystem.battle(enemyName, enemyStrength, enemyHP)

        if i == 4:
            Lore.bossStory(1)
            battleSystem.bossBattle(i)
            battleSystem.battle(minibossName, minibossStrength, minibossHP)

        if i == 7:
            battleSystem.potionReplenish(0)


if level == 5:
    combatOnGoing = False
    print(f"Your final score is: {score}")
    sys.exit()
