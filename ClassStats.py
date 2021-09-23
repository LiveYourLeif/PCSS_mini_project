import random
import Stats

health = 0
strengthL = 0
strengthU = 0
defenceL = 0
defenceU = 0
magicL = 0
magicU = 0


class ClassType:
    def __init__(self, h, sl, su, dl, du, ml, mu):
        self.health = h
        self.strengthL = sl
        self.strengthU = su
        self.defenceL = dl
        self.defenceU = du
        self.magicL = ml
        self.magicU = mu

    def classHP(self):
        hitPoints = Stats.HP()
        hitPoints.set_HP(health)

    def classStrength(self):
        strength = Stats.Strength()
        strength.set_strength(random.randint(strengthL, strengthU))
        return strength.get_strength()


    def classDefence(self):
        defence = Stats.Defence()
        defence.set_defence(random.randint(defenceL,defenceU))

    def classMagic(self):
        magic = Stats.Magic()
        magic.set_magic(random.randint(magicL, magicU))

