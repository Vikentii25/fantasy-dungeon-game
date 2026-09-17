import random
from math import ceil

class Entity:
    def __init__(self, name, level, hp, armor_flat, armor_percent, weapon, strength, agility, intelligence):
        self.name = name
        self.level = level
        self.max_hp=hp
        self.hp = hp
        self.armor_flat = armor_flat
        self.armor_percent = armor_percent
        self.weapon = weapon
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.spell = None
        self.is_blocking = False

    def get_armor_percent(self):
        return self.armor_percent + ceil(self.agility / 2) / 100

    def take_damage(self, damage):
        damage_after_flat = max(0, damage - self.armor_flat)
        damage_after_percent = damage_after_flat * (1 - self.get_armor_percent())
        if self.is_blocking:
            damage_after_percent *= 0.5
            self.is_blocking = False
        self.hp -= round(damage_after_percent)

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def deal_damage(self):
        if self.weapon is None:
            return 1 + ceil(self.strength / 2)
        else:
            return random.randint(1, self.weapon.dice_sides) + self.weapon.bonus + self.strength

class Hero(Entity):
    def __init__(self, name, level, hp, armor_flat, armor_percent, weapon, strength, agility, intelligence, exp, hero_class):
        super().__init__(name, level, hp, armor_flat, armor_percent, weapon, strength, agility, intelligence)
        self.exp = exp
        self.hero_class = hero_class

class Enemy(Entity):
    def __init__(self, name, level, hp, armor_flat, armor_percent, weapon, strength, agility, intelligence, loot):
        super().__init__(name,level,hp, armor_flat, armor_percent, weapon, strength, agility, intelligence)
        self.loot = loot
