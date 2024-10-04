from random import randint

class Die:
    """A class representing a single die"""

    def __init__(selfself, num_sides=6):
        """Assum a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)
