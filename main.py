from localization import *
from boss import Dragon
from battle import boss_battle
from rooms import *
from heroes import *

def create_hero():

    print("Оберіть мову / Choose language:")
    print("1. Українська")
    print("2. English")
    lang_choice = input("Мова/Language: ").strip()
    lang = "en" if lang_choice == "2" else "ua"

    print(t("welcome", lang))

    name = input(t("enter_name", lang))

    print(t("choose_class", lang))
    print(t("warrior", lang))
    print(t("archer", lang))
    print(t("mage", lang))
    print(t("random", lang))

    while True:
        player_choice = input(t("choice", lang)).strip()

        if player_choice == "1":
            return Warrior(f"{name}", 1, 80, 2, 0.0, None, 5,3,2,0,"Warrior"), lang
        elif player_choice == "2":
            return Archer (f"{name}", 1, 70, 0, 0.05, None, 2, 5, 3, 0, "Archer"), lang
        elif player_choice == "3":
            return Mage(f"{name}", 1, 60, 0, 0.0, None, 1, 3, 5, 0, "Mage"), lang
        elif player_choice == "4":
            hero = random.choice([
                Warrior(name, 1, 100, 2, 0.0, None, 5, 3, 2, 0, "Warrior"),
                Archer(name, 1, 80, 0, 0.05, None, 2, 5, 3, 0, "Archer"),
                Mage(name, 1, 60, 0, 0.0, None, 1, 3, 5, 0, "Mage")
            ])
            return hero, lang
        else:
            print(t("invalid", lang))
def main():
    hero, lang = create_hero()
    dungeon_level = 1
    room_count = 0
    while hero.is_alive():
        print(t("dungeon_level", lang, dungeon_level))
        print(t("crossroads", lang, dungeon_level))
        print(t("left", lang))
        print(t("forward", lang))
        print(t("right",lang))

        direction = input(t("direction", lang)).strip()
        if direction not in ["1", "2", "3"]:
            print(t("invalid", lang))
            continue

        room = generate_room()
        show_room(room, hero, dungeon_level, lang)

        room_count += 1
        if room_count % 5 == 0:
            dungeon_level += 1
            if dungeon_level == 5:  # ← тригер боса
                dragon = Dragon()
                boss_battle(hero, dragon, lang)
                break
            print(t(f"deeper", lang, dungeon_level))

    print(t("game_over", lang))

main()