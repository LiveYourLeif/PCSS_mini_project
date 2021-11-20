import random
import sys
import threading
import ClassStats
import Enemy
import PlayerClass
import Lore
import queue
import time


level = 1
whoIsFighting = True
minibossDefeated = False
playerHealth = ClassStats.health
potionCount = 5
score = 0

def func(id, result_queue):
    time.sleep(0.1)
    result_queue.put(id)

def threadPicker():
    q = queue.Queue()
    threads = [threading.Thread(target=func, args=(i, q)) for i in range(6)]
    for th in threads:
        th.daemon = True
        th.start()

    result = q.get()
    if result >= 2:
        battleSystem.potionReplenish(0)
    else:
        battleSystem.maxHalthIncrease(0)

class battleSystem:
    def enemyGenerator(self):
        enemyList = []
        for i in range(10):
            newName = Enemy.EnemyType.className(self)
            currentEnemy = Enemy.EnemyType(newName, (i * 5) + 10, (i * 2) + 1, (i * 2) + 2)
            enemyList.append(currentEnemy)
        return enemyList

    enemy = enemyGenerator(0)

    def potionReplenish(self):
        global potionCount
        print("You find Underbergs, your stock is replenished!")
        potionCount = 5
        print(f"Underbergs remaining in your pocket: {potionCount}/5.\n")

    def maxHalthIncrease(self):
        print("You find a health increase potion! ")
        playerHealth = 150
        print(f"Your max health is now: {playerHealth}\n")

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

    def minibossBattle(self):
        global minibossName
        global minibossStrength
        global minibossHP
        miniboss = Enemy.EnemyType("Breitthøvd", 50, 10, 15)
        minibossName = miniboss.name
        minibossStrength = random.randint(miniboss.strengthL, miniboss.strengthU)
        minibossHP = miniboss.health
        print(f"A giant {minibossName} appears in front of you!")

    def finalbossBattle(self):
        global finalbossName
        global finalbossStrength
        global finalbossHP
        finalboss = Enemy.EnemyType("General Rommel", 75, 16, 18)
        finalbossName = finalboss.name
        finalbossStrength = random.randint(finalboss.strengthL, finalboss.strengthU)
        finalbossHP = finalboss.health
        print(f"The devious {finalbossName} rises in front of you!")

    def battle(enemyName, enemyStrength, enemyHP):
        global whoIsFighting
        global combatOnGoing
        global playerHealth
        global potionCount
        global score
        global minibossDefeated
        strengthIncrease = 2

        while combatOnGoing:
            while enemyHP > 0 and whoIsFighting:
                    playerAction = int(input(f"It is your turn! What do you want to do?\n"
                                             "Melee = 1 | Magic = 2 | Heal = 3 | Stats = 4 \n"))


                    if playerAction == 1:
                        if PlayerClass.Player.playerChoice == 1:
                            warriorStrength = PlayerClass.Player.warrior.classStrength()
                            if minibossDefeated:
                                warriorStrength += strengthIncrease
                            print(f"You swing at the {enemyName} with your sword!")
                            print(f"You dealt {warriorStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - warriorStrength
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 2:
                            mageStrength = PlayerClass.Player.mage.classStrength()
                            if minibossDefeated:
                                mageStrength += strengthIncrease
                            print(f"You slap the {enemyName} with the back of your hand!")
                            print(f"You dealt {mageStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - mageStrength
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 3:
                            wildcardStrength = PlayerClass.Player.wildcard.classStrength()
                            if minibossDefeated:
                                wildcardStrength += strengthIncrease
                            print(f"You roundhouse kick the {enemyName} in the throat!")
                            print(f"You dealt {wildcardStrength} damage to the {enemyName}")
                            enemyHP = enemyHP - wildcardStrength
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                    if playerAction == 2:
                        if PlayerClass.Player.playerChoice == 1:
                            warriorMagic = PlayerClass.Player.warrior.classMagic()
                            if minibossDefeated:
                                warriorMagic += strengthIncrease
                            print(f"You try to cast a fireball, but only tickle the {enemyName} with sparks!")
                            print(f"You dealt {warriorMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - warriorMagic
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 2:
                            mageMagic = PlayerClass.Player.mage.classMagic()
                            if minibossDefeated:
                                mageMagic += strengthIncrease
                            print(f"You use a powerful magic attack on the {enemyName}!")
                            print(f"You dealt {mageMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - mageMagic
                            if enemyHP > 0:
                                print(f"{enemyName} health: {enemyHP} \n")
                            whoIsFighting = False
                            score += 1

                        if PlayerClass.Player.playerChoice == 3:
                            wildcardMagic = PlayerClass.Player.wildcard.classMagic()
                            if minibossDefeated:
                                wildcardMagic += strengthIncrease
                            print(f"You cast a magic spell on the {enemyName}!")
                            print(f"You dealt {wildcardMagic} damage to the {enemyName}")
                            enemyHP = enemyHP - wildcardMagic
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
                            elif 4 < level < 9:
                                if playerHealth > 100:
                                    playerHealth = 100
                            print(f"You drink the Underberg and restore 30 health. You are reinvigorated.")
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
                            print(f"Your max health is now: {playerHealth} and your powers have increased by two!\n")
                        else:
                            print(f"{enemyName} has fallen to your powers\n")
                            playerHealth += 30

                        if level < 4:
                            if playerHealth > 50:
                                playerHealth = 50
                            print(f"You regain some of your energy!\n"
                                  f"Player health: {playerHealth}\n")
                        elif 4 < level < 9:
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



for i in range(10):
    combatOnGoing = True
    while combatOnGoing:
        level = i
        print(f"LEVEL: {level+1}")
        if playerHealth > 0:
            if i < 4:
                Lore.story(i)
                battleSystem.normalBattle(i)
                battleSystem.battle(enemyName, enemyStrength, enemyHP)

            if i == 4:
                Lore.bossStory(1)
                battleSystem.minibossBattle(i)
                battleSystem.battle(minibossName, minibossStrength, minibossHP)

            if 4 < i < 9:
                minibossDefeated = True
                Lore.story(i)
                battleSystem.normalBattle(i)
                battleSystem.battle(enemyName, enemyStrength, enemyHP)

            if i == 7:
                threadPicker()

            if i == 9:
                Lore.bossStory(2)
                battleSystem.finalbossBattle(i)
                battleSystem.battle(finalbossName, finalbossStrength, finalbossHP)


if level == 10:
    combatOnGoing = False
    sys.exit()
