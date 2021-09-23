import random
import Stats

health = 5
strengthL = 0
strengthU = 0
defenceL = 0
defenceU = 0
magicL = 0
magicU = 0

class Warrior:
    hpWarrior = Stats.HP()
    hpWarrior.set_HP(50)
    print(f"HP: {hpWarrior.get_HP()}")

    strengthWarrior = Stats.Strength()
    strengthWarrior.set_strength(random.randint(6, 8))
    print(f"Strength: {strengthWarrior.get_strength()}")

    defenceWarrior = Stats.Defence()
    defenceWarrior.set_defence(random.randint(8,10))
    print(f"Defence: {defenceWarrior.get_defence()}")

    magicWarrior = Stats.Magic()
    magicWarrior.set_magic(0)
    print(f"Magic: {magicWarrior.get_magic()}")


class Mage:
    hpMage = Stats.HP()
    hpMage.set_HP(50)
    print(f"HP: {hpMage.get_HP()}")

    strengthMage = Stats.Strength()
    strengthMage.set_strength(random.randint(1, 3))
    print(f"Strength: {strengthMage.get_strength()}")

    defenceMage = Stats.Defence()
    defenceMage.set_defence(random.randint(1, 3))
    print(f"Defence: {defenceMage.get_defence()}")

    magicMage = Stats.Magic()
    magicMage.set_magic(random.randint(8, 10))
    print(f"Magic: {magicMage.get_magic()}")

class Wildcard:
    hpWildCard = Stats.HP()
    hpWildCard.set_HP(50)
    print(f"HP: {hpWildCard.get_HP()}")

    strengthWildCard = Stats.Strength()
    strengthWildCard.set_strength(random.randint(0,10))
    print(f"Strength: {strengthWildCard.get_strength()}")

    defenceWildCard = Stats.Defence()
    defenceWildCard.set_defence(random.randint(0,10))
    print(f"Defence: {defenceWildCard.get_defence()}")

    magicWildCard = Stats.Magic()
    magicWildCard.set_magic(random.randint(0, 10))
    print(f"Magic: {magicWildCard.get_magic()}")

