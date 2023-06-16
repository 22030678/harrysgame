import random

# Clase base para los personajes
class Character:#define the Character class.
    def __init__(self, name, type, life, health):#(_init_)initialize character properties
        """
        Character is the base class that has properties common to all characters, 
        such as name, type, life, and health.
        """
        self.name = name
        self.type = type
        self.life = life
        self.health = health
#has methods to take damage, check if the character is alive and attack the opponent.
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack(self, opponent):
        pass

# Class for Harry Potter characters
"""
The CharacterHarryPotter class is a subclass of Character and specific to Harry Potter characters.
"""
class HarryPotterCharacter(Character):
    def __init__(self, name, type, life, health):
        super().__init__(name, type, life, health)

    def attack(self, opponent):
        # Attack implementation based on character type
        if self.type == "Magic":
            if opponent.type == "Magic":
                damage = random.randint(10, 20)
            elif opponent.type == "Muggle":
                damage = random.randint(5, 10)
            elif opponent.type == "Creature":
                damage = random.randint(15, 25)
        elif self.type == "Muggle":
            if opponent.type == "Magic":
                damage = random.randint(5, 10)
            elif opponent.type == "Muggle":
                damage = random.randint(10, 20)
            elif opponent.type == "Creature":
                damage = random.randint(10, 15)
        elif self.type == "Creature":
            if opponent.type == "Magic":
                damage = random.randint(15, 25)
            elif opponent.type == "Muggle":
                damage = random.randint(10, 15)
            elif opponent.type == "Creature":
                damage = random.randint(20, 30)