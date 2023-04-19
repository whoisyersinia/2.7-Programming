import time
import random
import math
import os
import sys
import re
from pprint import pprint

# import tkinter as tk


class player:
    """Gets the player's starting health, atack, luck, defence, and name.
    And sets their health, attack, luck, defence, and name when it changes.
    """

    def __init__(self, pHealth, pAttack, pDefence, pLuck, pName, pLocation):
        self._health = pHealth
        self._attack = pAttack
        self._defence = pDefence
        self._luck = pLuck
        self._name = pName
        self._location = pLocation

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, newHealth):
        self._health = newHealth

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, newAttack):
        self._attack = newAttack

    @property
    def luck(self):
        return self._luck

    @luck.setter
    def luck(self, newLuck):
        self._luck = newLuck

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, newDefence):
        self._defence = newDefence

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, newLocation):
        self._location = newLocation


# getters and setters for enemy
class enemy:
    """Gets the enemy's starting health, atack, luck, defence, and name.
    And sets their health, attack, luck, defence, and name when it changes.
    """

    def __init__(
        self,
        eHealth,
        eAttack,
        eDefence,
        eSpecial,
        eChance,
        eName,
        eSpecialtime,
        eMagicresist,
    ):
        self._health = eHealth
        self._attack = eAttack
        self._defence = eDefence
        self._special = eSpecial
        self._chance = eChance
        self._name = eName
        self._specialtime = eSpecialtime
        self._magicresist = eMagicresist

    @property
    def health(self):
        return self._health

    @property
    def attack(self):
        return self._attack

    @property
    def defence(self):
        return self._defence

    @property
    def special(self):
        return self._special

    @property
    def chance(self):
        return self._chance

    @property
    def name(self):
        return self._name

    @property
    def specialtime(self):
        return self._special

    @property
    def magicresist(self):
        return self._magicresist

    @health.setter
    def health(self, newHealth):
        self._health = newHealth

    @attack.setter
    def attack(self, newAttack):
        self._attack = newAttack

    @defence.setter
    def defence(self, newDefence):
        self._defence = newDefence

    @special.setter
    def special(self, newSpecial):
        self._special = newSpecial

    @chance.setter
    def chance(self, newChance):
        self._chance = newChance

    @name.setter
    def name(self, newName):
        self._name = newName

    @specialtime.setter
    def specialtime(self, newSpecialtime):
        self._specialtime = newSpecialtime

    @magicresist.setter
    def magicresist(self, newMagicresist):
        self._magicresist = newMagicresist


def enemyGen(level):
    """Generates enemies by giving them random generated stats (attack, defense etc...) based on their level.

    Args:
        level (int): The level of enemy to bee generated

    Returns:
        _type_: _description_
    """
    file = open("1.txt", "r")
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    file = open("animal.txt", "r")
    lines = file.readlines()
    animal = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close
    # tutorial bots
    # end of copy + paste
    if level == 0:
        health = random.randint(25, 30)
        attack = random.randint(1, 5)
        defence = 0
        special = random.randint(10, 15)
        chance = 0
        special_time = random.randint(3, 4)
        magic_resist = 0
        return enemy(
            health,
            attack,
            defence,
            special,
            chance,
            adjective + " " + animal,
            special_time,
            magic_resist,
        )
    # level 1 bots
    elif level == 1:
        health = random.randint(40, 50)
        attack = random.randint(5, 15)
        defence = random.randint(1, 3)
        special = random.randint(10, 20)
        chance = random.randint(1, 5)
        special_time = random.randint(4, 5)
        magic_resist = random.randint(1, 3)
        return enemy(
            health,
            attack,
            defence,
            special,
            chance,
            adjective + " " + animal,
            special_time,
            magic_resist,
        )
    # level 2 bots
    elif level == 2:
        health = random.randint(50, 60)
        attack = random.randint(15, 25)
        defence = random.randint(5, 10)
        special = random.randint(30, 50)
        chance = random.randint(2, 6)
        special_time = random.randint(6, 8)
        magic_resist = random.randint(2, 4)
        return enemy(
            health,
            attack,
            defence,
            special,
            chance,
            adjective + " " + animal,
            special_time,
            magic_resist,
        )

    # boss bots
    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        defence = random.randint(10, 15)
        special = random.randint(50, 60)
        chance = random.randint(4, 10)
        special_time = random.randint(10, 12)
        magic_resist = 8
        return enemy(
            health,
            attack,
            defence,
            special,
            chance,
            adjective + " " + animal,
            special_time,
            magic_resist,
        )


### COMBAT FUNCTIONS ###
def enemyAttack(hitChance, attackValue, name, defence, luck):
    """Determines how much an enemy has attacked you for

    Args:
        hitChance (int): The enemy's chance (luck)
        attackValue (int): The base attack value of an enemy
        name (str): Name of enemy
        defence (int): The player's defence
        luck (int): The player's luck

    Returns:
        int: How much the player has received as damage
    """
    time.sleep(2)
    print(name, "is winding up for an attack...")

    if luck < 3:
        hit = random.randint(1, 3)
    elif luck >= 3 and luck <= 7:
        hit = random.randint(1, 5)
    elif luck > 7 and luck <= 9:
        hit = random.randint(1, 8)
    else:
        hit = random.randint(1, 10)

    if hitChance >= hit:
        print("it hits you..")
        if attackValue < defence:
            print(f"Your Defence startles {name}!")
            return 0
        else:
            loss = attackValue - defence
            print("You didn't dodge, losing...", loss, "health")
            return math.ceil(loss)
    else:
        print("The enemy misses!")
        return 0


# enemy special attack
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
    print("You didn't anticipate it, halving your defence, losing...", loss, "health")
    return math.ceil(loss)


# if your attack is going to hit
def hitChance(luck, chance, name):
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
            print(f"You hit the {name}!")
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
            print(f"You hit the {name}!")
            return True


# all special attacks
# crit
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


# spells
# sleep
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
    """Checks if the enemy is dead or not"""
    if health < 1:
        return True
    else:
        return False


# gameover with quit()
def gameOver(Name):
    """Gameover screen"""
    print("-----SYSTEMS SHUTTING DOWN-----")
    print("The Planet will now secure your stored data into our database")
    print("Good Bye", Name)
    time.sleep(5)
    quit()


def combat(enemy, character, escapable):
    """The combat system which allows the player to choose what move they are going to do and then the enemy attacks

    Args:
        enemy (obj):
        character (obj):

    Returns:
        true: if enemy is dead
    """
    # default starting combat variables
    try_parry = False
    crit = False
    count = 0
    blocked_dmg = 0
    magic_cd = 0
    sleep = False
    sleep_time = 0
    magic_cd = 0
    combat = True

    time.sleep(0.2)
    text_effect(
        "\nAn enemy has spotted you.\nYou get ready and are now entering combat."
    )
    time.sleep(0.2)
    text_effect(f"\nA wild, {enemy.name}, has appeared!")
    while combat == True:
        if magic_cd < 0:
            magic_cd = 0
        time.sleep(0.5)
        text_effect(f"\n{enemy.name} has {enemy.health} health.\n")
        if escapable:
            print(
                "\nWhat action do you want to take?\nFight(1) - Attack:",
                character.attack,
                "\nCast Spell(2) - Cooldown:",
                magic_cd,
                "\nBlock(3) - Defence:",
                character.defence,
                "\nFlee(4) - Luck:",
                character.luck,
                f"\nInspect(5) - View {enemy.name} Stats.".format(magic_cd),
            )
        else:
            print(
                "\nWhat action do you want to take?\nFight(1) - Attack:",
                character.attack,
                "\nCast Spell(2) - Cooldown:",
                magic_cd,
                "\nBlock(3) - Defence:",
                character.defence,
                "\nYou cannot flee! This option is unavaliable!",
                f"\nInspect(5) - View {enemy.name} Stats.".format(magic_cd),
            )
        time.sleep(0.75)
        action = input("> ")
        legal_actions = ["1", "2", "3", "4", "5"]
        while action not in legal_actions:
            print("Invalid Input! Please try again.")
            action = input("> ")
        if sleep_time == 0 and sleep == True:
            print(f"{enemy.name} has awoken...")
            sleep = False
        if magic_cd <= 0:
            magic_cd = 0
        if action == "1":
            blocked_dmg = 0
            try_parry = False
            if sleep == True:
                print(f"You prepare for an attack against the motionless {enemy.name}!")
                time.sleep(1)
                damage = character.attack * 2
                enemy.health = enemy.health - damage
                print(
                    "You damage the enemy for,",
                    damage,
                    "health.\nIts health is now,",
                    enemy.health,
                    "!",
                )
                sleep = False
                time.sleep(1)
                print(f"Your exceptional attack woke up the {enemy.name}!")
            elif character.attack < enemy.defence:
                print(f"You notice the {enemy.name} overwhelming defence....")
            else:
                damage = character.attack - enemy.defence
                print("You prepare for an attack.")
                hit = hitChance(character.luck, enemy.chance, enemy.name)
                crit = critChance(character.luck)
                if hit == True:
                    if crit == True:
                        crit_dmg = damage * 2
                        enemy.health = enemy.health - crit_dmg
                        print("......")
                        time.sleep(1.5)
                        print("......")
                        time.sleep(2)
                        print("......")
                        time.sleep(2.5)
                        print("CRITICAL HIT!!!!")
                        time.sleep(1)
                        print(f"You damage {enemy.name} for,", crit_dmg, "health.\n")
                    else:
                        enemy.health = enemy.health - damage
                        time.sleep(2)
                        print(f"You damage {enemy.name} for,", damage, "health.\n")
                        count += 1
                else:
                    print("You missed!")
        elif action == "2":
            cast_try = castSleep(character.luck, enemy.chance, enemy.magicresist)
            if cast_try == True and magic_cd == 0:
                print("......")
                time.sleep(1.5)
                print("......")
                time.sleep(2)
                print("......")
                time.sleep(2.5)
                print(f"You have sucessfully casted 'Sleep' on {enemy.name}!!!\n")
                sleep = True
                magic_cd = 5
                sleep_time = 2
            elif magic_cd > 0:
                print("{} more turns to cast 'Sleep'\n".format(magic_cd))
                time.sleep(0.75)
                print(".......")
            else:
                print("......")
                time.sleep(1.5)
                print("......")
                time.sleep(2)
                print("......")
                time.sleep(2.5)
                print(f"You have unsucessfully casted 'Sleep' on {enemy.name}!\n")
                magic_cd = 5
        elif action == "3":
            crit = False
            try_parry = True
            blocked_dmg = character.defence
            print(f"You prepare for {enemy.name} attack....")
            count += 1
        elif action == "4":
            try_parry = False
            if escapable:
                crit = False
                flee = character.luck
                if flee < enemy.chance or enemy.defence == 0:
                    print("You haven't sucessfully fled...")
                    count += 1
                else:
                    print("You fled...")
                    combat = False
            else:
                print("You haven't sucessfully fled...")
                count += 1
        else:
            try_parry = False
            print(
                f"\nName: {enemy.name}\nAttack: {enemy.attack}\nDefence: {enemy.defence}\nLuck: {enemy.chance}\nMagic Resist: {enemy.magicresist}"
            )
            continue

        enemyDead = isDead(enemy.health)

        if sleep == True:
            time.sleep(0.75)
            print("Zzzzz....")
            magic_cd -= 1
            sleep_time -= 1
            count += 1
        else:
            if enemyDead == False:
                if count + 1 == enemy.specialtime:
                    time.sleep(1)
                    print(f"{enemy.name}is staring at you.....")
                    magic_cd -= 1
                if count >= enemy.specialtime and try_parry == True:
                    count = 0
                    print(f"The {enemy.name}'s special attack affected your stance!!")
                    try_parry = False
                    character.health = character.health - enemySpecialAttack(
                        enemy.special, enemy.name, character.defence
                    )
                    characterDead = isDead(character.health)
                    magic_cd -= 1
                    count = 0
                elif try_parry == True:
                    if blocked_dmg > enemy.attack:
                        time.sleep(2)
                        print(f"You parried {enemy.name}'s attack!")
                        characterDead = isDead(character.health)
                        blocked_dmg = 0
                        magic_cd -= 1
                    else:
                        time.sleep(2)
                        print(f"The {enemy.name}'s attack overwhelmed your defence!")
                        character.health = character.health - enemyAttack(
                            enemy.chance,
                            enemy.attack,
                            enemy.name,
                            character.defence,
                            character.luck,
                        )
                        characterDead = isDead(character.health)
                        magic_cd -= 1
                else:
                    # enemy attack minus player health
                    character.health = character.health - enemyAttack(
                        enemy.chance,
                        enemy.attack,
                        enemy.name,
                        character.defence,
                        character.luck,
                    )
                    characterDead = isDead(character.health)
                    magic_cd -= 1

                # if you're dead ends combat and plays gameover
                if characterDead == True:
                    combat = False
                    gameOver(character.name)

                else:
                    time.sleep(1.5)
                    print("You have", character.health, "health remaining.")
                    print(f"{enemy.name} has", enemy.health, "health remaining.")
            else:
                # ends combat if you have defeated the enemy and regenerates health
                combat = False
                print(f"You have sucessfully defeated {enemy.name}!!!")
                if character.health != 100:
                    character.health(
                        character.health + random.randint(1, character.luck)
                    )
                    if character.health > 100:
                        character.health = 100
                    else:
                        time.sleep(1.5)
                        print(
                            "You have regenerated.\nYour health after combat is",
                            character.health,
                        )
                        print("All cooldowns reset!")
                else:
                    character.health = 100
                    time.sleep(1.5)
                    print("You have 100 Health.")
                    print("All cooldowns reset!")
                return True


def title():
    """Prompts player to start"""
    return


def clear():
    """Clears the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


PLACENAME = "placename"
DESCRIPTION = "description"
INSPECT = "inspect"
ITEMS = "items"
NPC = "npc"
ENEMY = "enemy"
DIRECTIONS = "directions"
map = {
    # npc test a3
    "a3": {
        PLACENAME: "Dr. Ock's lab",
        DESCRIPTION: "A fire broke out in the lab - find your boss, Dr. Ock",
        INSPECT: "There is a big hallway in front (north) of you.",
        # test
        ITEMS: ["test"],
        DIRECTIONS: {"north": "b3"},
    },
    "b3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "A long hallway that leads to the emergency escape pods.",
        INSPECT: "There is a big hallway in front of you.",
        ENEMY: {"name": None, "level": 1, "escapable": False},
        DIRECTIONS: {"north": "c3"},
    },
    # item - place later
    "c1": {
        PLACENAME: "Bio Lab",
        DESCRIPTION: "There is something shiny in front of you",
        INSPECT: "item",
        ITEMS: [],
        DIRECTIONS: {"south": "c2"},
    },
    "c2": {
        PLACENAME: "Bio Lab Door",
        DESCRIPTION: 'A door that has "Biology Lab" written on it',
        INSPECT: "open",
        DIRECTIONS: {"north": "c1", "south": "c3"},
    },
    "c3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "A long hallway that leads to the emergency escape pods, there is a door on your left.",
        INSPECT: "There is a big hallway in front of you.",
        DIRECTIONS: {"north": "d3", "west": "c2"},
    },
    "d3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "It continues...",
        INSPECT: "You see a light in the distance.",
        DIRECTIONS: {"north": "e3"},
    },
    # lvl 1 enemy
    "e1": {
        PLACENAME: "Escape Pod Hallway",
        DESCRIPTION: "There is something in front of you.",
        ENEMY: {"name": "test", "level": 1, "escapable": False},
        DIRECTIONS: {"south": "e2", "east": "f1"},
    },
    "e2": {
        PLACENAME: "Escape Pod Hallway",
        DESCRIPTION: "There is no one here.",
        DIRECTIONS: {"south": "e3", "north": "e1"},
    },
    "e3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "There is another hallway on your left.",
        INSPECT: "You see a light in the distance.",
        DIRECTIONS: {"north": "f3", "east": "e2"},
    },
    "f1": {
        PLACENAME: "Escape Pod Hallway",
        DESCRIPTION: "There is a green light in front of you...",
        DIRECTIONS: {"north": "g1", "east": "e2"},
    },
    # dr ock
    "f3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "You're almost there keep going....",
        INSPECT: "You see a light in the distance.",
        NPC: {
            "name": "Dr. Ock",
            "description": "A fat man resembling my boss, Dr. Ock.",
            "dialogue": 1,
            "escapable": False,
        },
        DIRECTIONS: {
            "north": "g3",
        },
    },
    # escape - tp to other square (make function first)
    "g1": {
        PLACENAME: "Escape Pods",
        DESCRIPTION: "Escape.",
        INSPECT: "escape",
    },
    "g2": {
        PLACENAME: "Escape Pod Hallway",
        DESCRIPTION: "There is a green light in front of you...",
        DIRECTIONS: {"north": "g1", "south": "g3"},
    },
    "g3": {
        PLACENAME: "Junction Lab Hallway",
        DESCRIPTION: 'There is a sign in front of you "<---- Escape Pods"',
        INSPECT: "The left hallway is blocked...",
        DIRECTIONS: {
            "west": "g2",
        },
    },
}


def regex(string):
    """the regular expression for the string to be split

    Args:
        string (str): the raw string

    Returns:
        bool: true or false if the string fits the REGEX.
    """
    pattern = r"[A-Za-z]+\s[A-Za-z]+"
    if re.match(pattern, string):
        return True
    else:
        return False


def split_string(string):
    """splits the string to two values

    Args:
        string (str): the raw string

    Returns:
        str: the split string
        bool: returns false if str cannot be split
    """
    if regex(string):
        command = string.split(" ")[0]
        noun = string.split(" ")[1]
        return command, noun
    else:
        return False


def text_effect(string):
    """adds a text effect that writes out strings letter by letter

    Args:
        string (str): the text
    """
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def npc_handler(character):
    """handles npc interaction

    Args:
        character (str): the npc name
    """
    location = character.location
    npc_name = map[location][NPC]["name"]
    npc_desc = map[location][NPC]["description"]
    npc_dialogue = map[location][NPC]["dialogue"]

    if npc_name == "Dr. Ock":
        text_effect(npc_desc)
        dr_ock(npc_dialogue, character)


# npc
def dr_ock(dialogue, character):
    """TO-DO: print letter by letter"""
    if dialogue == 1:
        time.sleep(0.5)
        text_effect(
            "\nDr. Ock: You over there! You don't have much time! This whole thing is gonna burn down! Run!"
        )
        while True:
            time.sleep(0.5)
            text_effect(
                "\n1. What happened here?\n2. Where do I go?\n3. Goodbye\n(Type 1,2,3)\n"
            )
            action = input("> ")

            if action == "1":
                text_effect(
                    "Someone started a fire in the lab! That person, he escaped! There's no time to catch him, just run."
                )
            elif action == "2":
                text_effect(
                    "Turn right to the escape pods! It's configurated to go to our lunar base on the Moon. There's only one left. Hurry!"
                )
            elif action == "3":
                text_effect("Farewell!")
                map[character.location][NPC]["escapable"] = True
                prompt(character)
                break
            else:
                continue


def prompt(character):
    """puts out a prompt for all the possible actions a player can take"""
    possible_dir = []
    for dir in map[character.location][DIRECTIONS]:
        possible_dir.append(dir)
    print("\n------------------------")
    print(map[character.location][PLACENAME] + "\n")
    print("What do you want to do?")
    print(f"You can move {', '.join(possible_dir)}.")
    action = input("> ").lower()

    if split_string(action):
        command, noun = split_string(action)  # type: ignore
        if command.lower() in ["move", "m"]:
            if (
                NPC in map[character.location]
                and not map[character.location][NPC]["escapable"]
            ):
                print(
                    f"{map[character.location][NPC]['name']} is waving at you (Type Talk)"
                )
            else:
                player_move(character, character.location, noun)
    else:
        legal_actions = [
            "move",
            "inspect",
            "fight",
            "help",
            "quit",
            "m",
            "i",
            "f",
            "h",
            "q",
            "talk",
            "t",
            "inv",
            "inventory",
            "take",
            "c",
            "flee",
            "e",
        ]
        while action not in legal_actions:
            # ensures that the player can do mutliple actions on one line after the player already inputed only one action in one line
            if split_string(action):
                command, noun = split_string(action)  # type: ignore
                if command.lower() in ["move", "m"]:
                    if (
                        NPC in map[character.location]
                        and not map[character.location][NPC]["escapable"]
                    ):
                        print(
                            f"{map[character.location][NPC]['name']} is waving at you (Type Talk)"
                        )
                        break
                    else:
                        player_move(character, character.location, noun)
                        break
            else:
                print("Illegal action, please input again!")
                action = input("> ")
                continue

        if action in ["quit", "q"]:
            while True:
                print("Are you sure you want to quit? (y or n)")
                quit = input("> ")
                if quit.lower() in ["y", "yes"]:
                    exit()
                elif quit.lower() in ["n", "no"]:
                    prompt(character)
                    break
                else:
                    continue

        elif action in ["help", "h"]:
            print(
                "Move by inputing MOVE or M OR type move then the location (e.g. MOVE NORTH or M N)\nInspect by inputing INSPECT or I\nFight by inputing FIGHT or F\nFlee by inputing FLEE or e\nStuck? Input HELP or H\nLeaving? Input QUIT or Q.\nChecking your inventory? Input INVENTORY or INV\nPick up an item? Input TAKE. For multiple items. Input TAKE (ITEM NAME). Pick up everything? Input TAKE ALL\nCheck your stats? Input C\nnAll inputs are case-insentive.\n "
            )

        elif action in ["move", "m"]:
            if (
                NPC in map[character.location]
                and not map[character.location][NPC]["escapable"]
            ):
                print(
                    f"{map[character.location][NPC]['name']} is waving at you (Type talk)"
                )
            else:
                player_move(character, character.location, None)

        elif action in ["talk", "t"]:
            if NPC in map[character.location]:
                npc_handler(character)
            else:
                print("There is no one to talk to...")

        elif action in ["inspect", "i"]:
            player_inspect(character.location)

        elif action in ["inventory", "inv"]:
            if not inventory:
                print("You have nothing on you...")
            else:
                items = []
                for item in inventory:
                    items.append(item)
                print(f"Inventory: {', '.join(items)}.")

        elif action in ["take"]:
            if map[character.location][INSPECT]:
                print("There is nothing to take...")
            else:
                item_handler(character, character.location, None)
        elif action in ["c"]:
            print(
                f"\nName: {character.name}\nAttack: {character.attack}\nDefence: {character.defence}\nLuck: {character.luck}"
            )
        elif action in ["fight", "f"]:
            if (
                map[character.location][ENEMY]
                and not map[character.location][ENEMY]["escapable"]
            ):
                combat(
                    enemyGen(map[character.location][ENEMY]["level"]),
                    character,
                    map[character.location][ENEMY]["escapable"],
                )
                map[character.location][ENEMY]["escapable"] = None
            else:
                print("There is no one to fight against...")
        elif action in ["flee", "e"]:
            if (
                map[character.location][ENEMY]
                and not map[character.location][ENEMY]["escapable"]
            ):
                map[character.location][ENEMY]["escapable"] = None
            else:
                print("There is no one to escape from...")


def player_move(character, location, action):
    """Moves the player

    Args:
        movement (str)
    """
    direction_synonyms = {
        "north": ["n", "up", "u"],
        "south": ["s", "down", "d"],
        "east": ["e", "right", "r"],
        "west": ["w", "left", "l"],
    }
    if not action:
        q = "Where to next? (N, S, E, W)"
        dest = input(q).lower()

        if dest in map[location][DIRECTIONS]:
            destination = map[location][DIRECTIONS][dest]
            print(f"\nYou have moved {dest.upper()}.")
            move_handler(destination, character)
        else:
            for key, value in direction_synonyms.items():
                if dest in value:
                    if key in map[location][DIRECTIONS]:
                        destination = map[location][DIRECTIONS][key]
                        print(f"\nYou have moved {key.upper()}.")
                        move_handler(destination, character)
                        break
            else:
                print("You cannot move that way!")
                player_move(character, location, None)
    else:
        dest = action

        if dest in map[location][DIRECTIONS]:
            destination = map[location][DIRECTIONS][dest]
            print(f"\nYou have moved {dest.upper()}.")
            move_handler(destination, character)
        else:
            for key, value in direction_synonyms.items():
                if dest in value:
                    if key in map[location][DIRECTIONS]:
                        destination = map[location][DIRECTIONS][key]
                        print(f"\nYou have moved {key.upper()}.")
                        move_handler(destination, character)
                        break
            else:
                print("You cannot move that way!")
                prompt(character)


def move_handler(dest, character):
    """Handles movement by changing the player's current location and setting it as the new pos

    Args:
        dest (str): destination
    """

    # REMOVE AFTER TESTING
    print("\n" + "You have moved to " + dest + ".")

    setattr(player, "location", dest)
    current_pos(dest, character)


def current_pos(location, character):
    """checks where the player is and prints it - INCREASE TIME.SLEEP"""
    print(map[location][PLACENAME])
    print(map[location][DESCRIPTION])
    if NPC in map[location]:
        text_effect("Someone's waving at you... (Type talk)")

    if ENEMY in map[location] and map[location][ENEMY]["escapable"] is not None:
        enemy_initiate_escapable = [
            "Someone's behind you! You can still escape!",
            "You can hear footsteps behind you!",
            "Someone's trying to ambush you!",
        ]
        enemy_initiate = ["Someone's tapping your shoulder!\n"]
        if map[location][ENEMY]["escapable"] == True:
            time.sleep(0.75)
            text_effect(random.choice(enemy_initiate_escapable))
        else:
            time.sleep(0.75)
            text_effect(random.choice(enemy_initiate))
            combat(
                enemyGen(map[location][ENEMY]["level"]),
                character,
                map[character.location][ENEMY]["escapable"],
            )
        # escapable false:

        # ENEMY FIGHT OR flee interaction function


# tip pop-up
def player_inspect(location):
    """Handles movement by changign the player's current location and setting it as the new pos

    Args:
        dest (str): destination
        character (obj): player
    """
    global take_tip
    if INSPECT in map[location]:
        if not map[location][INSPECT]:
            print("You've already checked here...")
        else:
            print("\n" + map[location][INSPECT])
            map[location][INSPECT] = None
    else:
        text_effect("There is nothing here....")
    if ITEMS in map[location]:
        items = []
        for item in map[location][ITEMS]:
            items.append(item)
        if not items:
            pass
        else:
            if take_tip:
                print(
                    f"There is a {', '.join(items)} (To pick up type TAKE or if they're mutiple items type TAKE (ITEM NAME) or TAKE ALL to take everything)."
                )
                take_tip = False
            else:
                text_effect(f"There is a {', '.join(items)}.")

            map[location][INSPECT] = None


def item_handler(character, location, action):
    if not action:
        items = []
        for item in map[location][ITEMS]:
            items.append(item)
            inventory.append(item)
            map[location][ITEMS].remove(item)
        if not items:
            print("You've already taken all the items here...")
        else:
            text_effect(f"Added {', '.join(items)} to inventory.")
            for item in items:
                attack_increase = item_list[item]["attack"]
                character.attack = character.attack + attack_increase
                print(
                    f" By equipping {item} attack increased by {attack_increase}! Your attack is now {character.attack}!"
                )


# item list and stats
item_list = {
    "Rustic Lazer Pistol": {
        "description": "A old lazer pistol - looks ancient.",
        "attack": 2,
        "type": "weapon",
    },
    "test": {"description": "test", "attack": 1, "type": "weapon"},
}

### GAMELOOP ###


def createClass():
    global playerHealth
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
        # stats
        playerHealth = 100
        playerAttack = 15
        playerDefence = 3
        playerLuck = random.randint(1, 10)
        playerName = input("Enter your name:").title()
        playerLocation = "a3"
        while True:
            if playerName == "":
                print("CANDACE: Your name is not *redacted*")
                playerName = input("CANDACE: Please put your actual name").title()
            else:
                print("CANDACE: Welcome,", playerName, "#413485 to planet, Kepler-62e.")
                break
    else:
        print("Invalid Input!!")
    return (
        playerHealth,
        playerAttack,
        playerDefence,
        playerLuck,
        playerName,
        playerLocation,
    )


def intro_to_earth(character):
    global take_tip
    take_tip = True
    print("\n" + "QUEST: " + map[character.location][DESCRIPTION])
    print("TIP - Stuck? Type HELP.")
    while True:
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
    # print("Welcome,", character.name,
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
    # time.sleep(3)


def tutorial():
    """Start game"""
    clear()
    print("-----SYSTEMS ONLINE-----")
    # time.sleep(1.75)
    print("Vital signs online. Systems Check. Boys we did it!")
    # time.sleep(1.5)
    print(".....")
    # time.sleep(2)
    print("He's waking up!")
    # time.sleep(1.25)
    print(".....")
    # time.sleep(1.5)
    print("Good morning! My name is Candace, your personal advisor!")
    # time.sleep(2)
    print("Where are you? Well you're in a private room, on planet Kepler-62e.")
    # time.sleep(3)
    print(
        "Who are you? You, my friend, are a collection of several lives over many millennia, you are part of a secret program of the government."
    )
    # time.sleep(4)
    print("Your job is to find life-suitable planets and find any mysteries on it.")
    # time.sleep(4)
    print(
        "Our recent research suggests that we have a single star system, with three possible candidates for our program, it is 26 million light years away."
    )
    # time.sleep(5)
    print(
        "Fortunately, we have sucessfully developed, I.G.U.D.\nThe Interstellar Great Universal Directory!\nWhich, means you can travel 26 million light years in seconds!"
    )
    # time.sleep(4)
    print(
        "We also have developed a new gun for you.. If there's anyone that gets in your way.\nWe'll do a little practice later."
    )
    # time.sleep(4)
    print("For now.. we'll finish downloading all the data...")
    # time.sleep(2)
    print("You woke up, in an all white room.")
    # time.sleep(2.5)
    print("'Listen to them!', he said in awfully fearful voice.")
    # time.sleep(3)
    print(
        "Hello!\nBefore we practice the combat system. We need to pick a planet to go to for your main mission. We recommend Earth for your first mission."
    )
    class_data = createClass()

    character = player(
        class_data[0],
        class_data[1],
        class_data[2],
        class_data[3],
        class_data[4],
        class_data[5],
    )

    # time.sleep(3)
    print(
        "Attack is how much damage you will deal to the enemy minus their defence.\nDefence is how much you damage you'll block from an enemy's attack.\nLuck affects the choices you make in the story and if your attack is going to hit the enemy or not.\nWhen Health reaches 0, you are dead and the game is over. You can gain health at the end of combat and in other places.\nYour first spell is 'Sleep', which renders your enemy unable to anything. Your next attack against a asleep enemy deals double damage and awakens your enemy."
    )
    # time.sleep(10)
    print("Follow the instructions inculuded in the combat system. Do not try to flee.")
    # time.sleep(.75)
    print("3")
    # time.sleep(1)
    print("2")
    # time.sleep(1)
    print("1")
    # time.sleep(1)
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


# player default settings
inventory = []
# end player default settings
tutorial()


# window = tk.Tk()
# window.title('Hello Python')
# window.geometry("300x200+10+20")
# window.mainloop()
