class Item:
    def __init__(self, name, level, item_type, item_range):
        self.name = name
        self.level = level
        self.item_type = item_type
        self.item_range = item_range

class Weapon(Item):
    def __init__(self, name, level, item_type, item_range, dice_sides, bonus):
        super().__init__(name,level, item_type,item_range)
        self.dice_sides = dice_sides
        self.bonus = bonus
