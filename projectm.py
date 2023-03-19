import time
import random
import math
import os
from pprint import pprint
# import tkinter as tk


class player:
    """Gets the player's starting health, atack, luck, defence, and name. 
       And sets their health, attack, luck, defence, and name when it changes.  
    """

    def __init__(self, pHealth, pAttack, pDefence, pLuck, pName, pLocation):
        self.health = pHealth
        self.attack = pAttack
        self.defence = pDefence
        self.luck = pLuck
        self.name = pName
        self.location = pLocation

    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, newHealth):
        self.health = newHealth

    @property
    def attack(self):
        return self.attack

    @attack.setter
    def attack(self, newAttack):
        self.attack = newAttack

    @property
    def luck(self):
        return self.luck

    @luck.setter
    def luck(self, newLuck):
        self.luck = newLuck

    @property
    def defence(self):
        return self.defence

    @defence.setter
    def defence(self, newDefence):
        self.defence = newDefence

    @property
    def name(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        self.location = newLocation


#getters and setters for enemy
class enemy:
    """Gets the enemy's starting health, atack, luck, defence, and name. 
       And sets their health, attack, luck, defence, and name when it changes.  
    """

    def __init__(self, eHealth, eAttack, eDefence, eSpecial, eChance, eName,
                 eSpecialtime, eMagicresist):
        self.health = eHealth
        self.attack = eAttack
        self.defence = eDefence
        self.special = eSpecial
        self.chance = eChance
        self.name = eName
        self.specialtime = eSpecialtime
        self.magicresist = eMagicresist

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefence(self):
        return self.defence

    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.chance

    def getName(self):
        return self.name

    def getSpecialtime(self):
        return self.specialtime

    def getMagicresist(self):
        return self.magicresist

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setSpecial(self, newSpecial):
        self.special = newSpecial

    def setChance(self, newChance):
        self.chance = newChance

    def setName(self, newName):
        self.name = newName

    def setSpecialtime(self, newSpecialtime):
        self.specialtime = newSpecialtime

    def setMagicresist(self, newMagicresist):
        self.magicresist = newMagicresist


def enemyGen(level):
    """Generates enemies by giving them random generated stats (attack, defense etc...) based on their level. 

    Args:
        level (int): The level of enemy to bee generated

    Returns:
        _type_: _description_
    """
    temp = []
    file = open("1.txt", "r")
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    file = open("animal.txt", "r")
    lines = file.readlines()
    animal = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    #tutorial bots
    #end of copy + paste
    if level == 0:
        health = random.randint(25, 30)
        attack = random.randint(1, 5)
        defence = 0
        special = random.randint(10, 15)
        chance = 0
        special_time = random.randint(3, 4)
        magic_resist = 0
        return enemy(health, attack, defence, special, chance,
                     adjective + " " + animal, special_time, magic_resist)
    #level 1 bots
    elif level == 1:
        health = random.randint(40, 50)
        attack = random.randint(5, 15)
        defence = random.randint(1, 3)
        special = random.randint(10, 20)
        chance = random.randint(2, 4)
        special_time = random.randint(4, 5)
        magic_resist = random.randint(1, 3)
        return enemy(health, attack, defence, special, chance,
                     adjective + " " + animal, special_time, magic_resist)
    #level 2 bots
    elif level == 2:
        health = random.randint(50, 60)
        attack = random.randint(15, 25)
        defence = random.randint(5, 10)
        special = random.randint(30, 50)
        chance = random.randint(4, 6)
        special_time = random.randint(6, 8)
        magic_resist = random.randint(2, 4)
        return enemy(health, attack, defence, special, chance,
                     adjective + " " + animal, special_time, magic_resist)

    #boss bots
    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        defence = random.randint(10, 15)
        special = random.randint(50, 60)
        chance = random.randint(4, 10)
        special_time = random.randint(10, 12)
        magic_resist = 8
        return enemy(health, attack, defence, special, chance,
                     adjective + " " + animal, special_time, magic_resist)


### COMBAT FUNCTIONS ###
def enemyAttack(hitChance, attackValue, name, defence, luck):
    """Determines how much an enemy has attacked you for

    Args:
        hitChance (bool)): The chance of an enemy hitting the player
        attackValue (int): The base attack value of an enemy
        name (str): Name of enemy
        defence (int): The player's defence
        luck (int): The player's luck

    Returns:
        int: How much the player has received as damage
    """
    time.sleep(2)
    print(name, "is winding up for an attack...")
    hit = luck
    if hitChance >= hit:
        print("it hits you..")
        if attackValue < defence:
            print("Your Defence startles the enemy!")
            return 0
        else:
            loss = attackValue - defence
            print("You didn't dodge, losing...", loss, "health")
            return math.ceil(loss)
    else:
        print("The enemy misses!")
        return 0


#enemy special attack
def enemySpecialAttack(attackValue, name, defence):
    """Determines how much an enemy has attacked you for using its special

    Args:
        attackValue (int): The base attack value of an enemy
        name (str): Name of enemy
        defence (int): The player's defence

    Returns:
        int: How much the player has received as damage
    """
    time.sleep(2)
    print(name, "is winding up for a power move...")
    time.sleep(2)
    print("it hits you.. ")
    loss = attackValue - defence / 2
    print("You didn't anticipate it, halving your defence, losing...", loss,
          "health")
    return math.ceil(loss)


#if your attack is going to hit
def hitChance(luck, chance):
    """Formula for determining the chance of an enemy hitting the player

    Args:
        luck (int): The player's luck
        chance (_type_): The enemy's luck

    Returns:
        bool: true if it hits, false if it doesn't
    """
    hit_random = random.randint(1, 3)
    if hit_random != 1:
        if luck < chance:
            time.sleep(1)
            print("MISS!")
            return False
        else:
            time.sleep(1)
            print("You hit the enemy!")
            return True
    else:
        if luck >= 5:
            random_chance = random.randint(1, 2)
        else:
            random_chance = random.randint(1, 3)
        if random_chance != 1:
            time.sleep(1)
            print("MISS!")
            return False
        else:
            time.sleep(1)
            print("You hit the enemy!")
            return True


#all special attacks
#crit
def critChance(luck):
    """Determines if attacks are going to crit (deal more damage) or not based on the attacker's luck

    Args:
        luck (int): the attacker's luck

    Returns:
        bool: true if it crits false if not
    """
    if luck < 3:
        crit_chance = random.randint(1, 10)
    elif luck >= 3 and luck <= 7:
        crit_chance = random.randint(1, 8)
    elif luck > 7 and luck <= 9:
        crit_chance = random.randint(1, 5)
    else:
        crit_chance = random.randint(1, 3)
    if crit_chance == 1:
        return True
    else:
        return False


#spells
#sleep
def castSleep(luck, enemyChance, magicRes):
    """Determines if the spell sleep is going to work or not based on the player and enemy's luck and magic resistance

    Args:
        luck (int): Player's luck
        enemyChance (int): Enemy's luck
        magicRes (int): Enemy's magic res

    Returns:
        bool: true if it hits false if not
    """
    cast_chance = enemyChance + magicRes
    if luck > cast_chance:
        return True
    else:
        return False


def isDead(health):
    """ Checks if the enemy is dead or not """
    if health < 1:
        return True
    else:
        return False


#gameover with quit()
def gameOver(Name):
    """ Gameover screen """
    print("-----SYSTEMS SHUTTING DOWN-----")
    print("The Planet will now secure your stored data into our database")
    print("Good Bye", Name)
    time.sleep(5)
    quit()


def combat(enemy, character):
    """The combat system which allows the player to choose what move they are going to do and then the enemy attacks

    Args:
        enemy (obj):
        character (obj):

    Returns:
        true: if enemy is dead
    """
    try_parry = False
    crit = False
    count = 0
    blocked_dmg = 0
    magic_cd = 0
    sleep = False
    fled = False
    sleep_time = 0
    magic_cd = 3

    print(
        "An enemy has spotted you.\nYou get ready and are now entering combat."
    )
    time.sleep(2)
    print("A wild", enemy.getName(), "has appeared!")
    print("The enemy's health is", enemy.getHealth())
    combat = True
    while combat == True:
        time.sleep(1)
        print("What action do you want to take?\nFight(1) - Attack:",
              character.getAttack(),
              "\nCast Spell(2) - Cooldown:", magic_cd, "\nBlock(3) - Defence:",
              character.getDefence(), "\nFlee(4) - Luck:", character.getLuck(),
              "\nInspect(5) - View Enemy's Stats.".format(magic_cd))
        time.sleep(.75)
        action = input(">")
        while action != "1" and action != "2" and action != "3" and action != "4" and action != "5":
            print("Invalid Input! Please try again.")
            action = input("> ")
        if sleep_time == 0 and sleep == True:
            print("The enemy has awoken...")
            sleep = False
        if magic_cd <= 0:
            magic_cd = 0
        if action == "1":
            blocked_dmg = 0
            try_parry = False
            if sleep == True:
                print(
                    "You prepare for an attack against your motionless enemy!")
                time.sleep(1)
                damage = character.getAttack() * 2
                enemy.setHealth(enemy.getHealth() - damage)
                print("You damage the enemy for,", damage,
                      "health.\nIts health is now,", enemy.getHealth(), "!")
                sleep = False
                time.sleep(1)
                print("Your exceptional attack woke up the enemy!")
            elif character.getAttack() < enemy.getDefence():
                print("You notice your enemy's overwhelming defence....")
            else:
                damage = character.getAttack() - enemy.getDefence()
                print("You prepare for an attack.")
                hit = hitChance(character.getLuck(), enemy.getChance())
                crit = critChance(character.getLuck())
                if hit == True:
                    if crit == True:
                        crit_dmg = damage * 2
                        enemy.setHealth(enemy.getHealth() - crit_dmg)
                        print("......")
                        time.sleep(1.5)
                        print("......")
                        time.sleep(2)
                        print("......")
                        time.sleep(2.5)
                        print("CRITICAL HIT!!!!")
                        time.sleep(1)
                        print("You damage the enemy for,",
                              crit_dmg, "health.\nIts health is now,",
                              enemy.getHealth(), "!")
                    else:
                        enemy.setHealth(enemy.getHealth() - damage)
                        time.sleep(2)
                        print("You damage the enemy for,",
                              damage, "health.\nIts health is now,",
                              enemy.getHealth(), "!")
                        count += 1
                else:
                    print("You missed!")
        elif action == "2":
            cast_try = castSleep(character.getLuck(), enemy.getChance(),
                                 enemy.getMagicresist())
            if cast_try == True and magic_cd == 0:
                print("......")
                time.sleep(1.5)
                print("......")
                time.sleep(2)
                print("......")
                time.sleep(2.5)
                print("You have sucessfully casted 'Sleep' on the enemy!!!")
                sleep = True
                magic_cd = 5
                sleep_time = 2
            elif magic_cd > 0:
                print("{} more turns to cast 'Sleep'".format(magic_cd))
                time.sleep(.75)
                print(".......")
            else:
                print("......")
                time.sleep(1.5)
                print("......")
                time.sleep(2)
                print("......")
                time.sleep(2.5)
                print("You have unsucessfully casted 'Sleep' on the enemy!")
                magic_cd = 5
        elif action == "3":
            crit = False
            try_parry = True
            blocked_dmg = character.getDefence()
            print("You prepare for the enemy's attack....")
            count += 1
        elif action == "4":
            crit = False
            flee = character.getLuck()
            if flee < enemy.getChance() or enemy.getDefence() == 0:
                print("You haven't sucessfully fled...")
                count += 1
            else:
                print("You fled...")
                combat = False
                fled = True
        else:
            pprint(vars(enemy))
            action = input("> ")
            continue

        enemyDead = isDead(enemy.getHealth())

        if sleep == True:
            time.sleep(.75)
            print("Zzzzz....")
            magic_cd -= 1
            sleep_time -= 1
            count += 1
        else:
            if enemyDead == False:
                if count + 1 == enemy.getSpecialtime():
                    time.sleep(1)
                    print("The enemy is staring at you.....")
                    magic_cd -= 1
                if count >= enemy.getSpecialtime() and try_parry == True:
                    count = 0
                    print("The enemy's special attack affected your stance!!")
                    try_parry = False
                    character.setHealth(
                        character.getHealth() -
                        enemySpecialAttack(enemy.getSpecial(), enemy.getName(),
                                           character.getDefence()))
                    characterDead = isDead(character.getHealth())
                    magic_cd -= 1
                    count = 0
                elif try_parry == True:
                    if blocked_dmg > enemy.getAttack():
                        time.sleep(2)
                        print("You parried the enemy's attack!")
                        characterDead = isDead(character.getHealth())
                        blocked_dmg = 0
                        magic_cd -= 1
                    else:
                        time.sleep(2)
                        print("The enemy's attack overwhelmed your defence!")
                        character.setHealth(
                            character.getHealth() -
                            enemyAttack(enemy.getChance(), enemy.getAttack(),
                                        enemy.getName(), character.getDefence(
                                        ), character.getLuck()))
                        characterDead = isDead(character.getHealth())
                        magic_cd -= 1
                else:
                    #enemy attack minus player health
                    character.setHealth(character.getHealth() - enemyAttack(
                        enemy.getChance(), enemy.getAttack(), enemy.getName(),
                        character.getDefence(), character.getLuck()))
                    characterDead = isDead(character.getHealth())
                    magic_cd -= 1

                #if you're dead ends combat and plays gameover
                if characterDead == True:
                    combat = False
                    gameOver(character.getName())

                else:
                    time.sleep(1.5)
                    print("You have", character.getHealth(),
                          "health remaining.")
                    print("The enemy has", enemy.getHealth(),
                          "health remaining.")
            else:
                #ends combat if you have defeated the enemy and regenerates health
                combat = False
                print("You have sucessfully defeated the enemy!!!")
                if character.getHealth() != 100:
                    character.setHealth(character.getHealth +
                                        random.randint(1, character.genLuck))
                    if character.getHealth() > 100:
                        character.setHealth = 100
                    else:
                        time.sleep(1.5)
                        print(
                            "You have regenerated.\nYour health after combat is",
                            character.getHealth())
                        print("All cooldowns reset!")
                else:
                    character.setHealth = 100
                    time.sleep(1.5)
                    print("You have 100 Health.")
                    print("All cooldowns reset!")
                return True


def title():
    """Prompts player to start
    """
    return


def clear():
    """Clears the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


PLACENAME = 'placename'
DESCRIPTION = 'description'
INSPECT = 'inspect'
NPC = ''
ENEMY = 'level 0'
UP = 'up', 'north'
DOWN = 'down', 'south'
RIGHT = 'right', 'east'
LEFT = 'left', 'west'

map = {
    'a1': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'a2': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'a3': {
        PLACENAME: 'Start Position',
        DESCRIPTION: 'A fire broke out in the lab, talk to Dr. Ock',
        INSPECT: 'There is a big hallway in front of you.',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: 'b3',
        LEFT: ''
    },
    'a4': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'b1': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'b2': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'b3': {
        PLACENAME: 'Lab Hallway',
        DESCRIPTION: 'A long hallway that leads to the emergency escape pods.',
        INSPECT: 'There is a big hallway in front of you.',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: 'c3',
        LEFT: 'a3'
    },
    'b4': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'c1': {
        PLACENAME: 'Bio Lab',
        DESCRIPTION: 'There is something shiny in front of you',
        INSPECT: 'item',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: 'c2',
        RIGHT: '',
        LEFT: ''
    },
    'c2': {
        PLACENAME: 'Bio Lab Door',
        DESCRIPTION: 'A door that has "Biology Lab" written on it',
        INSPECT: 'open',
        NPC: '',
        ENEMY: '',
        UP: 'c1',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'c3': {
        PLACENAME: 'Lab Hallway',
        DESCRIPTION:
        'A long hallway that leads to the emergency escape pods, there is a door on your left.',
        INSPECT: 'There is a big hallway in front of you.',
        NPC: '',
        ENEMY: '',
        UP: 'c2',
        DOWN: '',
        RIGHT: 'd3',
        LEFT: ''
    },
    'c4': {
        PLACENAME: 'void',
        DESCRIPTION: 'void',
        INSPECT: 'inspect',
        NPC: '',
        ENEMY: '',
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
}


def prompt(character):
    """puts out a prompt for all the possible actions a player can take
    """
    print("What do you want to do?")
    action = input("> ")
    legal_actions = [
        'move', 'inspect', 'fight', 'help', 'quit', 'm', 'i', 'f', 'h', 'q'
    ]
    while action not in legal_actions:
        print("Illegal action, please input again!")
        action = input("> ")

    if action.lower() == 'quit':
        while True:
            print("Are you sure you want to quit?")
            quit = input("> ")
            if quit.lower() == "y":
                exit()
            elif quit.lower() == "n":
                prompt(character)
                break
            else:
                continue
        exit()

    elif action.lower() == 'help':
        print("""Move by inputing 'move' or 'm'\n
                Inspect by inputing 'inspect' or 'i'\n
                Fight by inputing 'fight' or 'f'\n
                Stuck? Input 'help' or 'h'\n 
                Leaving? Input 'quit' or 'q'\n
            """)

    elif action.lower() in ['move', 'm']:
        print(character.getLocation())
        player_move(character.getLocation())
    # elif action == "fight" or 'f':
    #     player_combat(enemy, character)


def player_move(location):
    """Moves the player

    Args:
        movement (str)
    """
    q = "Where to next?"
    dest = input(q).lower()

    if dest in ['up', 'north', 'n']:
        destination = map[location][UP]
        move_handler(destination, location)
    elif dest in ['down', 'south', 's']:
        destination = map[location][DOWN]
        move_handler(destination, location)
    elif dest in ['right', 'east', 'e']:
        destination = map[location][RIGHT]
        move_handler(destination, location)
    elif dest in ['left', 'west', 'w']:
        destination = map[location][LEFT]
        move_handler(destination, location)
    else:
        print("Invalid Input (Try 'right or east')")
        player_move(location)


def move_handler(dest, location):
    """Handles movement by changing the player's current location and setting it as the new pos

    Args:
        dest (str): destination
        character (obj): player
    """

    print("\n" + "You have moved to " + dest + ".")
    current_pos(dest)


def current_pos(location):
    """checks where the player is and prints it
    """
    print(map[location][PLACENAME])
    print(location)


def player_inspect(character):
    """Handles movement by changign the player's current location and setting it as the new pos

    Args:
        dest (str): destination
        character (obj): player
    """
    print(map[character.getLocation()][INSPECT])


def check_move():
    """Checks if the player can move to a square adjacent to them. 

    Returns:
        Boolean
    """
    # if map['']:


### GAMELOOP ###


def createClass():
    global playerAttack
    global playerDefence
    global playerLuck
    global playerName
    global playerLocation

    planet_choice = input(
        "Pick a planet. Earth, Mars(Not Available), Venus(Not Available)"
    ).lower()
    while planet_choice != "earth":
        print("Invalid Input!")
        planet_choice = input(
            "Pick a planet. Earth, Mars(Not Available), Venus(Not Available)"
        ).lower()
    if planet_choice == "earth":
        #stats
        playerAttack = 999  #15
        playerDefence = 10
        playerLuck = random.randint(1, 10)
        playerName = input("Enter your name:").title()
        playerLocation = 'a3'
        while True:
            if playerName == " ":
                print("Your name is not *redacted* ")
                playerName = input(
                    "Enter your name! To put in our database").title()
            else:
                print("Welcome,", playerName, "#413485 to planet, Kepler-62e.")
                break
    else:
        print("Invalid Input!!")
    return (playerAttack, playerDefence, playerLuck, playerName,
            playerLocation)


def intro_to_earth(character):
    while True:
        print(character.getName())
        prompt(character)
    # print("Good job, let's get out of here!")
    # #time.sleep(2)
    # print("Higher command, request your presence in the upper chamber room!")
    # # time.sleep(4)
    # print(
    #     "Without hesitation, you wave goodbye to Candace, and head towards the upper chamber room."
    # )
    # #time.sleep(2)
    # print("30 minutes later")
    # #time.sleep(3)
    # print("Welcome,", character.getName(),
    #       "to the Upper Chambers, a deep voice said.")
    # #time.sleep(4)
    # print("Do you know why your presence has been requested?")
    # #time.sleep(3)
    # print("You nod sideways, reaffirming your confusion.")
    # #time.sleep(3)
    # print(
    #     "Well, he looks down at a piece of paper,", character.getName(),
    #     "you have been transfered to the planet of your choice, which was Earth."
    # )
    # #time.sleep(4)
    # print(
    #     "Your mission is to solve any mysteries on Earth and you have special permission to destroy, eliminate, and kill any enemies your encounter."
    # )
    # #time.sleep(5)
    # print(
    #     "Now go and board the next Trans System Flight to Earth, using the great I.G.U.D, we will also send another person to accompany you in your travels."
    # )
    # #time.sleep(3)
    # print("To you 2000 years ago.")
    # #time.sleep(3)
    # print("Chapter 1 - Earth - Pilot")
    #time.sleep(3)


def tutorial():
    """Start game
    """
    clear()
    print("-----SYSTEMS ONLINE-----")
    #time.sleep(1.75)
    print("Vital signs online. Systems Check. Boys we did it!")
    #time.sleep(1.5)
    print(".....")
    #time.sleep(2)
    print("He's waking up!")
    #time.sleep(1.25)
    print(".....")
    # time.sleep(1.5)
    print("Good morning! My name is Candace, your personal advisor!")
    #time.sleep(2)
    print(
        "Where are you? Well you're in a private room, on planet Kepler-62e.")
    #time.sleep(3)
    print(
        "Who are you? You, my friend, are a collection of several lives over many millennia, you are part of a secret program of the government."
    )
    #time.sleep(4)
    print(
        "Your job is to find life-suitable planets and find any mysteries on it."
    )
    #time.sleep(4)
    print(
        "Our recent research suggests that we have a single star system, with three possible candidates for our program, it is 26 million light years away."
    )
    #time.sleep(5)
    print(
        "Fortunately, we have sucessfully developed, I.G.U.D.\nThe Interstellar Great Universal Directory!\nWhich, means you can travel 26 million light years in seconds!"
    )
    #time.sleep(4)
    print(
        "We also have developed a new gun for you.. If there's anyone that gets in your way.\nWe'll do a little practice later."
    )
    #time.sleep(4)
    print("For now.. we'll finish downloading all the data...")
    #time.sleep(2)
    print("You woke up, in an all white room.")
    #time.sleep(2.5)
    print("'Listen to them!', he said in awfully fearful voice.")
    #time.sleep(3)
    print(
        "Hello!\nBefore we practice the combat system. We need to pick a planet to go to for your main mission. We recommend Earth for your first mission."
    )
    class_data = createClass()
    character = player(100, class_data[0], class_data[1], class_data[2],
                       class_data[3], class_data[4])
    pprint(vars(character))
    #time.sleep(3)
    print(
        """Attack is how much damage you will deal to the enemy minus their defence.
          \nDefence is how much you damage you'll block from an enemy's attack.
          \nLuck affects the choices you make in the story and if your attack is going to hit the enemy or not.
          \nWhen Health reaches 0, you are dead and the game is over. You can g
          ain health at the end of combat and in other places.
          \nYour first spell is 'Sleep', which renders your enemy unable to anything. Your next attack against a asleep enemy deals double damage and awakens your enemy."""
    )
    #time.sleep(10)
    print(
        "Follow the instructions inculuded in the combat system. Do not try to flee."
    )
    #time.sleep(.75)
    print("3")
    #time.sleep(1)
    print("2")
    #time.sleep(1)
    print("1")
    #time.sleep(1)
    print("Let's practice!!")
    intro_to_earth(character)

    # finished_tutorial = combat(enemyGen(0), character)
    # if finished_tutorial:
    #     #time.sleep(2)
    #     print("You have completed the tutorial")
    #     tries = 0
    # else:
    #     print("Mission Failed!")
    #     tries = 0
    # while tries < 5:
    #     print("Do you wanna try again. 1 for yes. 2 for no(continue story).")
    #     tutorial_try = input(">")
    #     if tutorial_try == "1":
    #         print("3")
    #         time.sleep(1)
    #         print("2")
    #         time.sleep(1)
    #         print("1")
    #         time.sleep(1)
    #         print("Let's practice!!")
    #         finished_tutorial = combat(enemyGen(0), character)
    #         if finished_tutorial == True:
    #             time.sleep(2)
    #             print("You have completed the tutorial")
    #             tries += 1
    #         else:
    #             print("Mission Failed!")
    #             tries += 1
    #     elif tutorial_try == "2":
    #         intro_to_earth(character)
    #     else:
    #         print("Invalid input!")


tutorial()

# def main():

# window = tk.Tk()
# window.title('Hello Python')
# window.geometry("300x200+10+20")
# window.mainloop()