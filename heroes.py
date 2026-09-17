import random
from math import ceil

from entities import Hero
from items import Item

class Warrior(Hero):
    def deal_damage(self):
        if self.weapon is None:
            return 2 + ceil(self.strength / 2)
        else:
            return random.randint(1, self.weapon.dice_sides) + self.weapon.bonus + ceil(self.strength / 2)

class Archer(Hero):
    def deal_damage(self):
        if self.weapon is None:
            return 1 + ceil(self.strength / 2)
        else:
            return random.randint(1, self.weapon.dice_sides) + self.weapon.bonus + ceil(self.agility / 2)

class Mage(Hero):
    def deal_damage(self):
        if self.spell is not None:
            return random.randint(1, self.spell.dice_sides) + self.spell.bonus + ceil(self.intelligence / 2)
        elif self.weapon is not None:
            return random.randint(1, self.weapon.dice_sides) + self.weapon.bonus + ceil(self.strength / 2)
        else:
            return 1 + ceil(self.strength / 2)
