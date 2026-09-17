from entities import *
import random
from localization import *

def player_turn(hero, enemy, dungeon_level, can_flee=True, lang="ua"):
    print(t("your_turn", lang))
    print(f"HP: {hero.hp}/{hero.max_hp}")
    print(t("attack", lang))
    print(t("block", lang))
    print(t("run", lang  ))

    choice = input(t("battle_choice", lang))

    if choice == "1":
        damage = hero.deal_damage()
        enemy.take_damage(damage)
        print(t("hero_attack_damage", lang,  hero.name, damage, enemy.name, int(enemy.hp), enemy.max_hp))
    elif choice == "2":
        hero.is_blocking = True
        print(t("block_damage", lang, hero.name, int(hero.hp), hero.max_hp))
    elif choice == "3":
        if not can_flee:
            print(t("dragon_run", lang))
            return True
        dc = 12 + dungeon_level * 2
        roll = random.randint(1, 20) + ceil(hero.agility / 2)
        if roll >= dc:
            print(t("roll", lang, roll, dc))
            print(t("run_success", lang))
            return False
        else:
            print(t("roll", lang, roll, dc))
            print(t("run_fail", lang))
            return True
    else:
        print (t("invalid_choice", lang))

    return True

def battle(hero, enemy, dungeon_level, lang="ua"):
    if hero.agility >= enemy.agility:
        first, second = hero, enemy
    else:
        first, second = enemy, hero

    print (t("battle_starts", lang, hero.name, enemy.name))

    while hero.is_alive() and enemy.is_alive():
        if hero.agility >= enemy.agility:
            result = player_turn(hero, enemy, dungeon_level, lang=lang)
            if not result:
                print(t("run_success 2", lang))
                return False
            if not enemy.is_alive():
                break

            damage = enemy.deal_damage()
            hero.take_damage(damage)
            print(t("enemy_attack_damage", lang, enemy.name, damage, hero.name, hero.hp, hero.max_hp))
        else:
            damage = enemy.deal_damage()
            hero.take_damage(damage)
            print(t("enemy_attack_damage", lang, enemy.name, damage, hero.name, hero.hp, hero.max_hp))
            if not hero.is_alive():
                break
            result = player_turn(hero, enemy, dungeon_level, lang=lang)
            if not result:
                print(t("run_success 2", lang))
                return False
            if not enemy.is_alive():
                break


    if hero.is_alive():
        print(t("battle_win", lang, hero.name))
        return True
    else:
        print(t("battle_lose", lang, hero.name))
        return False

def boss_battle(hero, dragon, lang):
    print(t("dragon_line 1", lang))
    print(t("dragon_line 2", lang))
    print(t("dragon_hp", lang, dragon.hp, dragon.max_hp))

    while hero.is_alive() and dragon.is_alive():
        result = player_turn(hero, dragon, dungeon_level=1, can_flee=False, lang=lang)
        if not result:
            print(t("dragon_run", lang))
            continue

        if not dragon.is_alive():
            break

        if dragon.is_phase_two() and dragon.phase == 1:
            dragon.phase = 2
            print(t("dragon_line 3", lang))
            hero.armor_percent = max(0, hero.armor_percent - 0.2)
            hero.armor_flat = max(0, hero.armor_flat - 2)
            print(t("dragon_dbf", lang))

        dragon.turn_count += 1
        if dragon.use_special():
            print(t("dragon_fire", lang))

            while True:
                player_input = input(t("make_roll", lang)).strip().lower()
                if player_input == "кидок" or player_input == "roll":
                    roll = random.randint(1, 20)
                    bonus = ceil(hero.agility/2)
                    total = roll + bonus
                    print(t("roll_bonus", lang, roll, bonus, total))

                    full_damage = dragon.special_attack()
                    if total >= 15:
                        damage = full_damage // 2
                        print(t("half_damage", lang, damage))
                    else:
                        damage = full_damage
                        print(t("full_damage", lang, damage))

                    hero.take_damage(damage)
                    print(f"HP: {hero.hp}/{hero.max_hp}")
                    break
                else:
                    print(t("invalid_roll", lang))
        else:
            damage = dragon.normal_attack()
            hero.take_damage(damage)
            print(t("dragon_damage", lang, damage, hero.hp, hero.max_hp))

    if hero.is_alive():
        print(t("dragon_defeated", lang))
        print(t("game_win", lang))
        return True
    else:
        print(t("dragon_wins", lang))
        return False
