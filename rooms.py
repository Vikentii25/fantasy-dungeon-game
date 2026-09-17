from localization import *
from battle import battle
from entities import *

room_types = ["battle", "chest", "battle_chest", "trap", "shop", "empty"]

def generate_room():
    weights = [35, 3, 10, 20, 7, 25]
    return random.choices(room_types, weights=weights)[0]

def generate_enemy(dungeon_level):
    enemies = [
        Enemy("Гоблін", dungeon_level, 20 + dungeon_level * 5, 0, 0.05, None, 4,2,2, "50g"),
        Enemy("Скелет", dungeon_level, 25 + dungeon_level * 5, 0, 0.10, None, 3, 4, 2, "60g"),
        Enemy("Орк", dungeon_level, 35 + dungeon_level * 5, 3, 0.1, None, 7, 2, 1, "100g" ),
    ]
    return random.choice(enemies)

class Trap:
    def __init__(self, trap_type, dungeon_level):
        self.trap_type = trap_type
        self.dc = 10 + dungeon_level * 3
        self.damage_dice = 20

    def trigger(self, hero):
        if self.trap_type == "strength":
            stat = hero.strength
            print("Двері падають на вас і вам потрібно їх втримати. Потрібна перевірка сили")
        elif self.trap_type == "agility":
            stat = hero.agility
            print("Стріли летять з усіх боків і вам потрібно від них ухилитись. Потрібна перевірка спритності")
        elif self.trap_type == "intelligence":
            stat = hero.intelligence
            print("На стіні написана стародавня загадка та висить череп, червоні очі якого дивляться вам в душу. Потрібна перевірка інтелекту")
        while True:
            player_input = input("Здійсніть кидок (напишіть \"кидок\")").strip().lower()
            if player_input == "кидок":
                roll = random.randint(1, 20)
                bonus = ceil(stat/2)
                total = roll + bonus

                print(f"Кидок: {roll} + {bonus} (бонус) = {total} проти DC {self.dc}")

                if total >= self.dc:
                    print("Успіх! Пастка не спрацювала.")
                else:
                    damage = random.randint(1, self.damage_dice)
                    hero.take_damage(damage)
                    print(f"Провал! Пастка завдає {damage} шкоди. HP: {hero.hp}/{hero.max_hp}")
                break
            else:
                print("Введіть \"кидок\" щоб здійснити кидок...")

trap_types = ["strength", "agility", "intelligence"]

def show_room(room_type, hero, dungeon_level, lang="ua"):
    if room_type == "battle":
        enemy = generate_enemy(dungeon_level)
        print(f"Перед собою ви помічаєте лякуючого {enemy.name}а!")
        result = battle(hero, enemy, dungeon_level, lang)
        if not result:
            return False
    elif room_type == "chest":
        print("\nВи знаходите скриню... (поки не реалізовано)")
    elif room_type == "battle_chest":
        print("\nВороги охороняють скриню... (поки не реалізовано)")
    elif room_type == "trap":
        trap_type = random.choice(trap_types)
        trap = Trap(trap_type, dungeon_level)
        trap.trigger(hero)
    elif room_type == "shop":
        print("\nТаємний торговець посміхається... (поки не реалізовано)")
    elif room_type == "empty":
        old_hp = hero.hp
        heal_amount = random.randint(1, 10)
        hero.heal(heal_amount)
        actual_heal = hero.hp - old_hp
        print(f"\nКімната порожня. Тут тихо і спокійно. Ви відпочиваєте і відновлюєте {actual_heal} HP")
        print(f"HP: {hero.hp}/{hero.max_hp}")