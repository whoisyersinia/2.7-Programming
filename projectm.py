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
        return self._specialtime

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
        level (int): The level of enemy to be generated

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
        chance = random.randint(1, 3)
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
        chance = random.randint(1, 5)
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
# ENEMY ATTACK
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
    text_effect(f"\n{name} is winding up for an attack...\n")

    hit_chance = hitchance(luck, hitChance)
    roll = random.randint(1, 100)

    if roll >= hit_chance:
        time.sleep(1.25)
        text_effect("it hits you...\n")
        if attackValue < defence:
            text_effect(f"Your DEFENCE startles {name}!\n")
            return 0
        else:
            loss = attackValue - defence
            loss = math.ceil(loss)
            text_effect(f"You lost {loss} health.\n")
            return loss
    else:
        time.sleep(1.25)
        text_effect("The enemy misses!\n")
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
    time.sleep(1)
    text_effect(f"\n{name} is winding up for a power move...")
    for x in range(3):
        time.sleep(1.75)
        text_effect("......\n")
    time.sleep(1.25)
    text_effect("IT LANDS!")
    loss = attackValue - defence / 2
    loss = math.ceil(loss)
    text_effect(f"You lost {loss} health!\n")
    return loss


def combat_enemyspecial_handler(count, try_parry, character, enemy):
    if count + 1 == enemy.specialtime:
        time.sleep(1)
        text_effect(f"{enemy.name} is staring at you.....\n")
        try_parry = False
        return count, try_parry
    elif count >= enemy.specialtime and try_parry:
        time.sleep(1)
        text_effect(f"You get ready for the upcoming attack...")
        try_parry = False
        character.health = character.health - enemySpecialAttack(
            enemy.special, enemy.name, (character.defence * 1.5)
        )
        count = 0
        return count, try_parry
    elif count >= enemy.specialtime:
        character.health = character.health - enemySpecialAttack(
            enemy.special, enemy.name, character.defence
        )
        count = 0
        return count, try_parry
    else:
        return count, try_parry


# PLAYER ATTACK
def combat_playerAttack(player_luck, player_attack, enemy):
    text_effect("You prepare for an attack.\n")
    hit_chance = hitchance(player_luck, enemy.chance)
    roll = random.randint(1, 100)
    crit = critChance(player_luck)
    damage = player_attack - enemy.defence
    if roll <= hit_chance:
        if crit:
            crit_dmg = player_attack * 2
            enemy.health = enemy.health - crit_dmg
            text_effect("......\n")

            for x in range(2):
                time.sleep(1.25)
                text_effect("......\n")
            text_effect("CRITICAL HIT!!!!\n")
            time.sleep(1)
            text_effect(f"{enemy.name} took {crit_dmg} damage!\n")

        else:
            enemy.health = enemy.health - player_attack
            time.sleep(1.5)
            text_effect("It hits!!!\n")
            time.sleep(1)
            text_effect(f"{enemy.name} took {damage} damage!\n")
    else:
        time.sleep(1.5)
        text_effect("You missed...\n")


def hitchance(player_luck, enemy_luck):
    """Formula for determining the chance of an player hitting the enemy - Calculates the hit chance based on player and enemy luck

    Args:
        luck (int): The player's luck
        chance (_type_): The enemy's luck

    Returns:
        bool: true if it hits, false if it doesn't
    """
    base_chance = 50  # Base chance is 50%
    luck_diff = player_luck - enemy_luck
    if luck_diff > 0:
        return base_chance + (luck_diff * 5)
    elif luck_diff < 0:
        return base_chance - (abs(luck_diff) * 5)
    else:
        return base_chance


# all special attacks
# CRIT FUNCTION
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
        crit_chance = random.randint(1, 4)
    if crit_chance == 1:
        return True
    else:
        return False


# PARRY/BLOCK FUNCTION
# caluclation function
def combat_parry(luck, chance, defence, enemyAttack):
    hit_chance = hitchance(luck, chance)
    min_roll = (enemyAttack * 2) - (defence)
    math.ceil(min_roll)
    roll = random.uniform(min_roll, 100)
    if enemyAttack > defence * 2:
        return False
    elif roll <= hit_chance:
        return True
    else:
        return False


# handler function
def combat_parry_handler(character, enemy):
    if combat_parry(character.luck, enemy.chance, character.defence, enemy.attack):
        time.sleep(1.25)
        text_effect(f"You blocked {enemy.name}'s attack!")
    else:
        time.sleep(1.25)
        text_effect(
            f"You can feel {enemy.name}'s terrifying aura, unallowing you to block..."
        )
        character.health = character.health - enemyAttack(
            enemy.chance,
            enemy.attack,
            enemy.name,
            character.defence,
            character.luck,
        )
        characterDead = isDead(character.health)
        return characterDead


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
    cast_chance = hitchance(luck, enemyChance)
    roll = random.randint((magicRes * 5), 100)
    if roll <= cast_chance:
        return True
    else:
        return False


def enemy_sleep(sleep_time, magic_cd, sleep, enemy, character, tryattack, trycast):
    if sleep and not tryattack and sleep_time > 0:
        print(f"\n{enemy.name} is asleep...")
        return (sleep, magic_cd, sleep_time)
    elif tryattack:
        text_effect(f"You attack the motionless {enemy.name}!\n")
        damage = character.attack * 2
        enemy.health = enemy.health - damage
        time.sleep(0.5)
        text_effect(f"You damage the enemy for {damage} health.\n")
        text_effect(f"Your exceptional attack woke up the {enemy.name}!\n")
        sleep = False
        magic_cd = 5
        sleep_time = 0
        return sleep, magic_cd, sleep_time
    elif trycast:
        cast_try = castSleep(character.luck, enemy.chance, enemy.magicresist)
        if cast_try and magic_cd == 0:
            text_effect("......\n")
            for x in range(2):
                time.sleep(1.25)
                text_effect("......\n")
            time.sleep(1.75)
            text_effect(f"Sucessfully casted 'Sleep' on {enemy.name}!!!\n")
            sleep = True
            magic_cd = 5
            sleep_time = 3
            return sleep, magic_cd, sleep_time

        else:
            text_effect("......\n")
            for x in range(2):
                time.sleep(1.25)
                text_effect("......\n")
            time.sleep(1.75)
            text_effect(f"Unsucessfully casted 'Sleep' on {enemy.name}!\n")
            magic_cd = 5
            return sleep, magic_cd, sleep_time
    elif sleep and sleep_time <= 0:
        text_effect(f"\n{enemy.name} woke up!\n")
        sleep = False
        return sleep


def isDead(health):
    """Checks if the enemy is dead or not"""
    if health < 1:
        return True
    else:
        return False


# gameover with quit()
def gameOver(Name):
    """Gameover screen"""
    text_effect("\n-----SYSTEMS SHUTTING DOWN-----")
    text_effect("The Planet will now secure your stored data into our database...")
    time.sleep(1.5)
    text_effect(f"Goodbye {Name}...")
    time.sleep(2)
    quit()


# COMBAT PROMPT FUNCTIONS
def action_checker(action):
    legal_action = ["1", "2", "3", "4", "5"]
    while action not in legal_action:
        text_effect("Invalid Input! Please input again...")
        action = input("> ")
    else:
        return action


def combat_prompt(escapable, character, enemy, magic_cd):
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
            f"\nInspect(5) - View {enemy.name}'s Stats.".format(magic_cd),
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
            f"\nInspect(5) - View {enemy.name}'s Stats.".format(magic_cd),
        )


def combat_header(turn, count, character, enemy, characterdead):
    turn += 1
    count += 1
    if characterdead:
        gameOver(character.name)
    else:
        print(f"\nTurn {turn}")
        text_effect(f"\nYou have {character.health} health.")
        text_effect(f"\n{enemy.name} has {enemy.health} health.\n")
        return turn, count


def combat_magic_cd(magic_cd):
    magic_cd -= 1
    if magic_cd < 0:
        return 0
    else:
        return magic_cd


def combat_view_action(turn, count, magic_cd, enemy):
    print(
        f"\nName: {enemy.name}\nAttack: {enemy.attack}\nDefence: {enemy.defence}\nLuck: {enemy.chance}\nMagic Resist: {enemy.magicresist}\nSpecial Time: {enemy.specialtime}\n"
    )
    turn -= 1
    count -= 1
    magic_cd -= 1
    time.sleep(1)
    return turn, count, magic_cd


def combat_flee(luck, enemy_luck, escapable, location, name):
    flee_chance = hitchance(luck, enemy_luck)
    roll = random.randint(1, 100)
    if escapable:
        if roll <= flee_chance or enemy.defence == 0:
            text_effect("......\n")
            for x in range(2):
                time.sleep(1.75)
                text_effect("......\n")
            time.sleep(1.75)
            text_effect("You haven't sucessfully fled...")
        else:
            text_effect("......\n")
            for x in range(2):
                time.sleep(1.25)
                text_effect("......\n")
            time.sleep(1.75)
            text_effect("You fled...")
            map[location][ENEMY]["escapable"] = None
            combat = False
            return False
    else:
        text_effect(f"{name}: Running away is impossible against this enemy!")


def end_of_combat_prompt(character, enemy):
    combat = False
    text_effect(f"\nYou have sucessfully defeated {enemy.name}!!!\n")
    if character.health != 100:
        post_health = character.health
        regenerated_health = character.health = character.health + random.randint(
            character.luck, 15
        )
        if character.health > 100:
            character.health = 100
        regen = regenerated_health - post_health
        time.sleep(0.5)
        text_effect(
            f"You have regenerated {regen} health.\nYour health post-combat is {character.health}.\n",
        )
        text_effect("All cooldowns reset!")
    else:
        character.health = 100
        time.sleep(0.5)
        text_effect("FLAWLESS VICTORY!\n")
        text_effect("All cooldowns reset!\n")
    return combat


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
    count = -1
    magic_cd = -1
    sleep = False
    sleep_time = 0
    combat = True
    turn = 0

    text_effect("\nAn enemy has spotted you.")
    text_effect(f"\nA wild, {enemy.name}, has appeared!\n")
    while combat:
        # checkers
        characterDead = isDead(character.health)
        magic_cd = combat_magic_cd(magic_cd)

        # prompts
        turn, count = combat_header(turn, count, character, enemy, characterDead)  # type: ignore
        sleep = enemy_sleep(sleep_time, magic_cd, sleep, enemy, character, False, False)
        combat_prompt(escapable, character, enemy, magic_cd)
        action = action_checker(input("> "))
        # FIGHT
        if action == "1":
            try_parry = False
            # SLEEP WHICH DOUBLES ATTACK
            if sleep:
                sleep, magic_cd, sleep_time = enemy_sleep(
                    sleep_time, magic_cd, sleep, enemy, character, True, False
                )  # type: ignore
            # Unables the enemy to attack when their attack is lower than defence
            elif character.attack < enemy.defence:
                text_effect(f"You notice the {enemy.name} overwhelming defence....")
            # normal attack
            else:
                combat_playerAttack(character.luck, character.attack, enemy)
        # CAST SLEEP - Later for more spells
        elif action == "2":
            if magic_cd > 0:
                print("{} more turns to cast 'Sleep'\n".format(magic_cd))
                time.sleep(0.75)
                continue
            else:
                sleep, magic_cd, sleep_time = enemy_sleep(sleep_time, magic_cd, sleep, enemy, character, False, True)  # type: ignore
        # parry/block
        elif action == "3":
            try_parry = True
            text_effect(f"You prepare for {enemy.name}'s attack....")
        # flee function
        elif action == "4":
            try_parry = False
            combat_flee(
                character.luck,
                enemy.chance,
                escapable,
                character.location,
                character.name,
            )
        # View stats
        else:
            try_parry = False
            turn, count, magic_cd = combat_view_action(turn, count, magic_cd, enemy)
            continue

        enemyDead = isDead(enemy.health)

        # ENEMY TURN
        if sleep:
            time.sleep(1.5)
            text_effect("Zzzzzzzzzz....\n")

            sleep_time -= 1
        # when the enemy isn't under the sleep aliment
        else:
            if not enemyDead:
                # when the enemy is about to do a special move (based on property from object) run this function
                if count + 1 >= enemy.specialtime:
                    count, try_parry = combat_enemyspecial_handler(count, try_parry, character, enemy)  # type: ignore

                # when player blocked
                elif try_parry:
                    characterDead = combat_parry_handler(character, enemy)
                    try_parry = False
                else:
                    # normal attack from enemy
                    character.health = character.health - enemyAttack(
                        enemy.chance,
                        enemy.attack,
                        enemy.name,
                        character.defence,
                        character.luck,
                    )
            else:
                # ends combat if you have defeated the enemy and regenerates health
                combat = end_of_combat_prompt(character, enemy)
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
LOCKED = "locked"
map = {
    # ITEM TEST (PASSED)
    "a3": {
        PLACENAME: "Dr. Ock's lab",
        DESCRIPTION: "A fire broke out in the lab - find your boss, Dr. Ock",
        INSPECT: "There is a big hallway in front (north) of you.",
        DIRECTIONS: {"north": "b3"},
        ITEMS: {
            "Bio Lab Key": {
                "description": "A small key with a label that reads 'Biology Lab'.",
                "type": "misc",
            },
            "Rustic Laser Pistol (Attack: +2)": {
                "description": "A old lazer pistol - looks ancient.",
                "attack": 2,  # temporary
                "type": "weapon",
                "level": 1,
            },
        },
    },
    # ENEMY TEST LOCATION - PUT KEY LATER HERE
    "b3": {
        PLACENAME: "Lab Hallway",
        DESCRIPTION: "A long hallway that leads to the emergency escape pods.",
        INSPECT: "There is a big hallway in front of you.",
        DIRECTIONS: {"north": "c3"},
        ENEMY: {"level": 1, "escapable": False},
        LOCKED: {"status": True, "key": "Bio Lab Key"},
    },
    # item - place later
    "c1": {
        PLACENAME: "Bio Lab",
        DESCRIPTION: "There is something shiny in front of you",
        INSPECT: "item",
        ITEMS: [],
        DIRECTIONS: {"south": "c2"},
    },
    # LOCKED DOOR NORTH
    "c2": {
        PLACENAME: "Bio Lab Door",
        DESCRIPTION: 'A door that has "Biology Lab" written on it',
        INSPECT: "The door leading to the biology lab seems to be shut tight...",
        DIRECTIONS: {"north": "c1", "south": "c3"},
        LOCKED: {"status": True, "key": "bio_lab_key"},
    },
    # NORTH OR WEST ENEMY TEST PASSED
    "c3": {
        PLACENAME: "Lab Hallway Bio Lab Junction",
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
        ENEMY: {"level": 1, "escapable": False},
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


def prompt_quit(character):
    while True:
        print("Are you sure you want to quit? (y or n)")
        quit = input("> ")
        if quit.lower() in ["y", "yes"]:
            exit()
        elif quit.lower() in ["n", "no"]:
            prompt(character)
            return
        else:
            continue


def prompt(character):
    """puts out a prompt for all the possible actions a player can take"""
    # global vars for tips
    global unescapable_enemy_tip
    global enemy_tip
    global item_tip
    # list for dynamic data
    possible_dir = []
    dynamic_commands = []
    enemy_location = {}
    for dir in map[character.location][DIRECTIONS]:
        possible_dir.append(dir)

        enemy_position = map[character.location][DIRECTIONS][dir]
        if ENEMY not in map[enemy_position]:
            pass
        else:
            # finds all the locations where they're inescapable enemies
            if map[enemy_position][ENEMY]["escapable"] == False:
                enemy_location[dir] = enemy_position

    # DYNAMIC COMMANDS - PRINTS OUT EXTRA INFOMRATION DEPENDING ON THEIR LOCATION (e.g warns if there are enemy in locations the player can possibly go to)
    if ENEMY not in map[character.location]:
        pass
    elif map[character.location][ENEMY]["escapable"]:
        if enemy_tip:
            dynamic_commands.append(
                "A foe stands in your way, you can still FLEE, FIGHT, or MOVE.\nTIP: There is an enemy you can choose to FIGHT (input 'FIGHT' OF 'F') or FLEE ('FLEE' or 'E'). You can still MOVE ('MOVE' or 'M').\nFLEEING eliminates the enemy with no reward, preventing you from coming back and fighting it."
            )
            enemy_tip = False
        else:
            dynamic_commands.append(
                "A foe stands in your way, you can still FLEE, FIGHT, or MOVE."
            )
    else:
        pass

    # checks if there are enemies in the possible locations the player can go to through a for loop
    for dir, pos in enemy_location.items():
        if map[pos][ENEMY]["escapable"] == False:
            if unescapable_enemy_tip:
                dynamic_commands.append(
                    f"You sense an overwheliming aura {', '.join(enemy_location.keys()).upper()} of you. You should proceed with caution.\nTIP: There is an enemy you can't FLEE from in that location. Get ready before moving there..."
                )
                unescapable_enemy_tip = False
                break
            else:
                dynamic_commands.append(
                    f"You sense an overwheliming aura {', '.join(enemy_location.keys()).upper()} of you. You should proceed with caution."
                )
                break

    if (
        INSPECT in map[character.location]
        and ITEMS in map[character.location]
        and map[character.location][ITEMS]
    ):
        if item_tip:
            dynamic_commands.append(
                f"There is something glistening in the corner...\nTIP: There is an item nearby, INSPECT and find out what lies behind."
            )
            item_tip = False

        else:
            dynamic_commands.append(f"There is something glistening in the corner...")

    print("\n------------------------")
    print(map[character.location][PLACENAME] + "\n")
    print("What do you want to do?")
    print(f"You can move {', '.join(possible_dir)}.")
    if dynamic_commands:
        for command in dynamic_commands:
            # TEXT EFFECT LATER
            print(f"\n{command}")
    action = input("> ").lower()
    while True:
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
                action = input("> ").lower()
                continue

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
                else:
                    print("Illegal action, please input again!")
                    action = input("> ")

            if action in ["quit", "q"]:
                prompt_quit(character)
                break
            elif action in ["help", "h"]:
                print(
                    "Move by inputing MOVE or M OR type move then the location (e.g. MOVE NORTH or M N)\nInspect by inputing INSPECT or I\nFight by inputing FIGHT or F\nFlee by inputing FLEE or e\nStuck? Input HELP or H\nLeaving? Input QUIT or Q.\nChecking your inventory? Input INVENTORY or INV\nPick up an item? Input TAKE. For multiple items. Input TAKE (ITEM NAME). Pick up everything? Input TAKE ALL\nCheck your stats? Input C\nAll inputs are case-insentive."
                )
                break

            elif action in ["move", "m"]:
                if (
                    NPC in map[character.location]
                    and not map[character.location][NPC]["escapable"]
                ):
                    print(
                        f"{map[character.location][NPC]['name']} is waving at you (Type talk)"
                    )
                    break
                else:
                    player_move(character, character.location, None)
                    break

            elif action in ["talk", "t"]:
                if NPC in map[character.location]:
                    npc_handler(character)
                    break
                else:
                    print("There is no one to talk to...")
                    break

            elif action in ["inspect", "i"]:
                player_inspect(character.location)
                break

            elif action in ["inventory", "inv"]:
                if not inventory:
                    print("You have nothing on you...")
                    break
                else:
                    items = []
                    for item in inventory:
                        items.append(item)
                    print(f"Inventory: {', '.join(items)}.")
                    break

            elif action in ["take"]:
                if INSPECT in map[character.location]:
                    if map[character.location][INSPECT]:
                        print("There is nothing to take...")
                        break
                    else:
                        item_handler(character, character.location, None)
                        break
                else:
                    text_effect("There is nothing here....")
                    break
            elif action in ["c"]:
                print(
                    f"\nName: {character.name}\nHealth: {character.health} \nAttack: {character.attack}\nDefence: {character.defence}\nLuck: {character.luck}"
                )
                break
            elif action in ["fight", "f"]:
                if ENEMY in map[character.location]:
                    if (
                        map[character.location][ENEMY]
                        and map[character.location][ENEMY]["escapable"]
                    ):
                        # win combat
                        if combat(
                            enemyGen(map[character.location][ENEMY]["level"]),
                            character,
                            map[character.location][ENEMY]["escapable"],
                        ):
                            map[character.location][ENEMY]["escapable"] = None
                            enemy_drop(map[character.location][ENEMY]["level"])
                            break

                        # lose
                    else:
                        print("There is no one to fight against...")
                        break
                else:
                    print("There is no one to fight against...")
                    break
            elif action in ["flee", "e"]:
                if ENEMY in map[character.location]:
                    if (
                        map[character.location][ENEMY]
                        and map[character.location][ENEMY]["escapable"]
                    ):
                        map[character.location][ENEMY]["escapable"] = None
                        print(
                            "You ran away from the enemy. It seems like it loss track of you..."
                        )
                        break
                    else:
                        print("There is no one to escape from...")
                        break
                else:
                    print("There is no one to escape from...")
                    break
            else:
                print("Illegal action, please input again!")
                action = input("> ")


def key_checker(destination):
    for item in inventory:
        if item in map[destination][LOCKED]["key"]:
            text_effect(f"Used {item}.\n.")
        return True
    else:
        return False


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
                        if (
                            LOCKED in map[destination]
                            and map[destination][LOCKED]["status"]
                        ):
                            if key_checker(destination):
                                map[destination][LOCKED]["status"] = False
                                move_handler(destination, character)
                            else:
                                print(
                                    f"The door {key.upper()} is locked. A key should be around...."
                                )
                                prompt(character)
                                break
                        else:
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
                        if (
                            LOCKED in map[destination]
                            and map[destination][LOCKED]["status"]
                        ):
                            if key_checker(destination):
                                map[destination][LOCKED]["status"] = False
                                move_handler(destination, character)
                            else:
                                print(
                                    f"The door {key.upper()} is locked. A key should be around...."
                                )
                                prompt(character)
                                break

                        else:
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
        enemy_initiate = [
            "Someone's tapping your shoulder!\n",
            "You can hear someone running towards you!\n",
            "UNKNOWN: STOP RIGHT THERE!\n",
        ]
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


# ITEM HANDLING
def item_handler(character, location, action):
    if ITEMS not in map[character.location]:
        text_effect("There is nothing to take...\n")
    elif not action:
        items = []
        for item in map[location][ITEMS]:
            items.append(item)
            inventory.append(item)
        if not items:
            print("You've already taken all the items here...")
        else:
            for item in items:
                if map[location][ITEMS][item]["type"] == "weapon":
                    attack_increase = map[location][ITEMS][item]["attack"]
                    character.attack = character.attack + attack_increase
                    text_effect(
                        f"You equipped {item}. {map[location][ITEMS][item]['description']} Attack increased by {attack_increase}! Your attack is now {character.attack}!\n"
                    )
                elif map[location][ITEMS][item]["type"] == "armour":
                    defence_increase = item_list[ITEMS][item]["defence"]
                    character.defence = character.defence + defence_increase
                    text_effect(
                        f"By equipping {item} defence increased by {defence_increase}! Your defence is now {character.defence}!\n"
                    )
                elif map[location][ITEMS][item]["type"] == "charm":
                    luck_increase = map[location][ITEMS][item]["luck"]
                    character.defence = character.defence + luck_increase
                    text_effect(
                        f"By equipping {item} luck increased by {luck_increase}! Your luck is now {character.luck}!\n"
                    )
                elif map[location][ITEMS][item]["type"] == "misc":
                    text_effect(
                        f"You picked up {item}. {map[location][ITEMS][item]['description']}\n"
                    )
                map[location][ITEMS].pop(item)


def enemy_drop(enemylevel):
    return


# item list and stats (CHANGE STATS LATER)
item_list = {
    "Rustic Lazer Pistol (Attack: +2)": {
        "description": "A old lazer pistol - looks ancient.",
        "attack": 2,  # temporary
        "type": "weapon",
        "level": 1,
    },
    "Rustic Spacesuit (Defence: +2)": {
        "description": "A old spacesuit - it gets the job done",
        "defence": 2,
        "type": "armour",
        "level": 1,
    },
    "Rustic Spacecharm (Luck: +1)": {
        "description": "You feel a bit luckier",
        "luck": 1,
        "type": "charm",
        "level": 1,
    },
}

### GAMELOOP ###


def createClass():
    global playerHealth
    global playerAttack
    global playerDefence
    global playerLuck
    global playerName
    global playerLocation

    # stats
    playerHealth = 100
    playerAttack = 15
    playerDefence = 5
    playerLuck = 10  # random.randint(1, 10)
    playerName = input("Enter your name:").title()
    playerLocation = "a3"
    while True:
        if playerName == "":
            print("CANDACE: Your name is not *redacted*")
            playerName = input("CANDACE: Please put your actual name").title()
        else:
            print("CANDACE: Welcome,", playerName, "#413485 to planet, Kepler-62e.")
            break
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
    global unescapable_enemy_tip
    global enemy_tip
    global item_tip
    enemy_tip = True
    take_tip = True
    item_tip = True
    unescapable_enemy_tip = True
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
learned_spells = []
# end player default settings
tutorial()


# window = tk.Tk()
# window.title('Hello Python')
# window.geometry("300x200+10+20")
# window.mainloop()
