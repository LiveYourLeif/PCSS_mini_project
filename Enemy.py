import random
import Stats


class EnemyType(): #Vi kan godt bare inherite constructoren fra ClassType, vi bruger de samme værdier anyways
    def __init__(self, n,  h, sl, su):
        self.name = n
        self.health = h
        self.strengthL = sl
        self.strengthU = su


    def className(self):
        enemyName = ["Goblin", "Troll", "Blob", "Skeleton", "Reanimated Knight", "Bonko Tossen", "Draugr", "Ligma",
                     "Werewolf"]
        return random.choice(enemyName)

    def enemyHP(self):
        hitPoints = Stats.HP()
        hitPoints.set_HP(self.health)
        return hitPoints.get_HP()

    def classStrength(self):
        strength = Stats.Strength()
        strength.set_strength(random.randint(self.strengthL, self.strengthU))
        return strength.get_strength()








