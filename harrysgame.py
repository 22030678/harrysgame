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

                #Overrides the attack method to implement attack logic based on character type.
        print(f"{self.name} attacks {opponent.name} and causes {damage} points of damage.")
        opponent.take_damage(damage) 
        """Depending on the type of the character and the opponent, 
        random damage values are generated using the random.randint function.
         A message indicating the attack is then printed and the opponent's 
         take_damage method is called."""

# Game class
class Game:
    def __init__(self):
        self.characters = []
#add characters to the game and to simulate a battle
    def add_character(self, character):
        self.characters.append(character)

    def simulate_battle(self):
        """
(simular_battle)
Two random characters are selected for each turn and the selected characters are verified to be different and alive.
 The first character then attacks the second character by calling the attack method. 
It is checked if the opponent was defeated and a message is printed if so.
"""
        while True:
            # Select two random characters for the turn
            character1 = random.choice(self.characters)
            character2 = random.choice(self.characters)

            # Verify that the selected characters are different and alive
            if character1 != character2 and character1.is_alive() and character2.is_alive():
                character1.attack(character2)

                # Check if the opponent is defeated
                if not character2.is_alive():
                    print(f"{character2.name} has been defeated.")

                    if character1.is_alive():
                        print(f"{character1.name} has been crowned the winner.")
                    break

# Create characters
harry_potter = HarryPotterCharacter("Harry Potter", "Magic", 100, 100)
hermione_granger = HarryPotterCharacter("Hermione Granger", "Magic", 100, 100)
ron_weasley = HarryPotterCharacter("Ron Weasley", "Magic", 100, 100)
dobby = HarryPotterCharacter("Dobby", "Creature", 100, 100)
dudley = HarryPotterCharacter("Dudley Dursley", "Muggle", 100, 100)
draco_malfoy = HarryPotterCharacter("Draco Malfoy", "Magic", 100, 100)

# Create game and add characters
game = Game()
game.add_character(harry_potter)
game.add_character(hermione_granger)
game.add_character(ron_weasley)
game.add_character(dobby)
game.add_character(dudley)
game.add_character(draco_malfoy)

# Simulate battle
game.simulate_battle()
