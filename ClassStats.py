import random
import Stats

# Values som bliver ændret nede i constructoren for ClassType
health = 50
strengthL = 0
strengthU = 0
magicL = 0
magicU = 0


# ClassType indeholder methods for at få de forskellige values til characters i spillet.
class ClassType:
    def __init__(self, h, sl, su, ml, mu):
        self.health = h
        self.strengthL = sl
        self.strengthU = su
        self.magicL = ml
        self.magicU = mu

    def classStrength(self):
        strength = Stats.Strength()
        strength.set_strength(random.randint(self.strengthL, self.strengthU))
        return strength.get_strength()

    def classMagic(self):
        magic = Stats.Magic()
        magic.set_magic(random.randint(self.magicL, self.magicU))
        return magic.get_magic()
