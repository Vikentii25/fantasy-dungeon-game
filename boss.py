from entities import Enemy
import random
from math import ceil

class Dragon(Enemy):
    def __init__(self):
        super().__init__(
            name="Дракон",
            level=5,
            hp=200,
            armor_flat=0,
            armor_percent=0.2,
            weapon=None,
            strength=10,
            agility=4,
            intelligence=6,
            loot="legendary"
        )
        self.turn_count = 0
        self.phase = 1

    def is_phase_two(self):
        return self.hp < self.max_hp * 0.5

    def use_special(self):
        return self.turn_count % 5 == 0 and self.turn_count != 0

    def normal_attack(self):
        return random.randint(1, 12) + ceil(self.strength / 2)

    def special_attack(self):
        return random.randint(10, 20) + ceil(self.strength / 2)