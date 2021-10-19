import random
import ClassStats


class EnemyType(): #Vi kan godt bare inherite constructoren fra ClassType, vi bruger de samme værdier anyways
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
        heroes = {"Peter":HeroType(h=100), "Oskar":HeroType(h=4)}
        peter = heroes["Peter"]
        oskar = heroes["Oskar"]
        return random.choice(enemyName)

    def enemyHP(self):
        hitPoints = Stats.HP()
        hitPoints.set_HP(self.health)
        return hitPoints.get_HP()



