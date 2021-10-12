import random
import ClassStats


class EnemyType(ClassStats.ClassType): #Vi kan godt bare inherite constructoren fra ClassType, vi bruger de samme værdier anyways
    def __init__(self, n,  h, sl, su, dl, du, ml, mu):
        self.name = n
        self.health = h
        self.strengthL = sl
        self.strengthU = su
        self.defenceL = dl
        self.defenceU = du
        self.magicL = ml
        self.magicU = mu

    def className(self):
        enemyName = ["Goblin", "Troll", "Blob", "Skeleton", "Reanimated Knight", "Bonko Tossen", "Draugr", "Ligma",
                     "Werewolf"]
        return random.choice(enemyName)



