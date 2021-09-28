import Stats
import random
import ClassStats

name = ["Goblin", "Troll", "Blob", "Skeleton", "Dragon", "Bonko Tossen", "Draugr", "Whitehead"]


class EnemyType(ClassStats.ClassType):
    def __init__(self, n, h, sl, su, dl, du, ml, mu):
        self.name = n
        self.health = h
        self.strengthL = sl
        self.strengthU = su
        self.defenceL = dl
        self.defenceU = du
        self.magicL = ml
        self.magicU = mu

    def className(self):
        enemyName = (random.choose(name))
        enemyName.setName(self.name)
        return enemyName.getName()

    #reeee


