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
        hitPoints.set_HP(self.health)
        return hitPoints.get_HP()

    def classStrength(self):
        strength = Stats.Strength()
        strength.set_strength(random.randint(self.strengthL, self.strengthU))
        return strength.get_strength()

    def classDefence(self):
        defence = Stats.Defence()
        defence.set_defence(random.randint(self.defenceL, self.defenceU))
        return defence.get_defence()

    def classMagic(self):
        magic = Stats.Magic()
        magic.set_magic(random.randint(self.magicL, self.magicU))
        return magic.get_magic()

