import random


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
