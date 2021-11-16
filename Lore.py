def story(level):
    if level == 0:
        print("Your task is to defeat the legendary enemy who is threatening the kingdom.\n"
              f"You wander into the wilderness. You hear a rumbling in the bushes, before an enemy appears in front of you!\n")
    if level == 1:
        print("The first beast of your adventure is slain, and you traverse further into the dreadful woods.\n"
              "Behind some trees, you spot a cave entrance, with something guarding it. You approach\n.")
    if level == 2:
        print("Your dead enemy is left bleeding in the mud, as you push it aside to enter the cave. \n"
              "Dark and mysterious, the cave sends shivers down your spine. \n"
              "Mysterious lit candles adorn the sides of the cave’s tall walls, which forms a pathway in the darkness.\n"
              "You know where you have to go.\n"
              "Suddenly the silence of the cave is broken by a deafening roar, and something emerges from the shadows!\n")
    if level == 3:
        print("You continue walking down the dimly lit pathway in the darkness for what feels like hours.\n"
              "The walls of the cave almost seem to close in on you, as the pathway becomes narrower and narrower, until you can barely stand upright. \n"
              "You spot an old wooden door with old metal chains keeping it shut, and in front, something guarding it\n")
    if level == 4:
        print("After a close fight, you narrowly escape with your life.\n"
              "During the fight, the metal chains on the door in front of you seemingly broke.\n"
              "You give the door a hard push, and as it slams open with a loud creak, you find yourself standing in front of a massive mausoleum.\n"
              "A single stone coffin lays atop a flight of steps.\n"
              "As you walk closer to investigate, the lid of the coffin bursts into the air, and lands right next to you.\n"
              "With a roar that rumbles the entire mausoleum, a monster crawls out of the coffin.\n")
    if level == 5:
        print("Miraculously, you’ve slain the beast.\n"
              "You take a moment to catch your breath, before you venture further into the mausoleum.\n"
              "At the back of the room, you spot a large door, with light shining through the cracks. You give it a push, and it creaks open.\n"
              "Filled with hope of reaching the outside world again, you hurry through the opening, but what meets your eye isn’t the bright sky, but a fiery portal with a beast crouched in front.\n"
              "You draw your weapon.\n")
    if level == 6:
        print("With your enemy dead by your feet, you enter the ominous portal.\n"
              "You find yourself in a land not unlike the world you know, however you can feel a disturbance in the air\n"
              "Goblins are running around you, with roll'n'eat kebabs in hand. You look to your right and spot an ominous sign\n"
              "Slagelse.\n"
              "You realize that this is the kingdom threatening your own, and your purpose is clear:\n"
              "Find and eliminate the ruler of this realm.\n"
              "")


def enemyTaunts(name):
    taunts = [f"The {name} slashes at you!",
              f"The {name} attacks!",
              f"The {name} stabs you!",
              f"The {name} cancels you on twitter!",
              f"The {name} lowers your social credit score!",
              f"The {name} uses a poison attack!",
              f"The {name} sucks out your life essence!"]
    return taunts
