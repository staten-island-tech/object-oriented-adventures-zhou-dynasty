import json
import os
import time

class SkeletonBattle:
    def __init__(self, player_hp):
        self.player_hp = player_hp

    def shoot(self):
        self.player_hp -=2
        return "You shoot the skeleton with an arrow."

    def defend(self):
        self.player_hp -= 1
        return "You defended against the skeleton's attack."

    def run(self):
        self.player_hp -= 5
        return "You tried to run, but the skeleton caught you."

class SkeletonHealth:
    def __init__(self):
        self.skeletonhp = 30

    def shot(self, has_special_weapon=False):
        damage = 20 if has_special_weapon else 2
        self.skeletonhp -= damage
        return f"Skeleton took {damage} damage."

    def killed(self, delay_duration):
        delay(delay_duration)
        print("You killed the skeleton.")

class WitherSkeletonBattle:
    def __init__(self, player_hp, has_starlight_wand):
        self.player_hp = player_hp
        self.has_starlight_wand = has_starlight_wand

    def shoot(self):
        return "You shoot the wither skeleton with a magical attack."

    def defend(self):
        self.player_hp -= 2
        return "You defended against the wither skeleton's attack."

    def run(self):
        self.player_hp -= 10
        return "You tried to run, but the wither skeleton caught you."

class WitherSkeletonHealth:
    def __init__(self):
        self.witherskeletonhp = 15

    def shot(self, has_special_weapon=False):
        damage = 7 if has_special_weapon else 3
        self.witherskeletonhp -= damage
        return f"Wither Skeleton took {damage} damage."

    def killed(self, delay_duration):
        delay(delay_duration)
        print("You killed the wither skeleton.")

class WitherBattle:
    def __init__(self, player_hp, has_hyperion):
        self.player_hp = player_hp
        self.has_hyperion = has_hyperion

    def shoot(self):
        return "You shoot the wither with a powerful attack."

    def defend(self):
        self.player_hp -= 3
        return "You defended against the wither's attack."

    def run(self):
        self.player_hp -= 15
        return "You tried to run, but the wither caught you."

class WitherHealth:
    def __init__(self):
        self.witherhp = 20

    def shot(self, has_special_weapon=False):
        damage = 10 if has_special_weapon else 4
        self.witherhp -= damage
        return f"Wither took {damage} damage."

    def killed(self, delay_duration):
        delay(delay_duration)
        print("You killed the wither.")

class Storyline:
    class ArcherStoryline:
        def __init__(self):
            self.archerhp = 20
            self.has_artisanal_bow = self.check_artisanal_bow()
            self.skeleton_battle = SkeletonBattle(self.archerhp)
            self.skeleton_health = SkeletonHealth()
            self.witherskeleton_battle = WitherSkeletonBattle(self.archerhp, self.has_artisanal_bow)
            self.witherskeleton_health = WitherSkeletonHealth()
            self.has_wither_bow = self.check_wither_bow()
            self.wither_battle = WitherBattle(self.archerhp, self.has_wither_bow)
            self.wither_health = WitherHealth()

        def check_artisanal_bow(self):
            try:
                with open("artisanal_bow.json", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        return any(bow.get('artisanal_bow_dropped') for bow in data)
                    else:
                        return data.get('artisanal_bow_dropped', False)
            except (FileNotFoundError, json.JSONDecodeError):
                return False

        def check_wither_bow(self):
            try:
                with open("wither_bow.json", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        return any(bow.get('wither_bow_dropped') for bow in data)
                    else:
                        return data.get('wither_bow_dropped', False)
            except (FileNotFoundError, json.JSONDecodeError):
                return False

        def beginning(self, delay_duration):
            print("Your adventure begins now.")
            print('You look around, confused, you decide to wander around.')
            print('You search for answers, none to be found.')
            print('Until.')
            delay(delay_duration)
            print('You encounter a skeleton!')
            delay(delay_duration)
            print('It seemed agitated?')
            delay(delay_duration)
            print('It charges at you.')
            print('A battle of the ages begins.')
            delay(delay_duration)
            os.system("cls")
            print(f'Player: {self.archerhp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')

        def encounter1(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.archerhp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')
            while self.skeleton_health.skeletonhp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.skeleton_battle.shoot())
                    print(self.skeleton_health.shot())
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.skeleton_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The skeleton found you and threw you into the backrooms.')
                    print(self.skeleton_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.archerhp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')

                if self.archerhp <= 0:
                    print("You died!")
                    return

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton! Congratulations!")
                self.skeleton_health.killed(delay_duration)

        def encounter2(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.archerhp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')
            while self.witherskeleton_health.witherskeletonhp > 0:
                move = input('Pick your next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.witherskeleton_battle.shoot())
                    print(self.witherskeleton_health.shot(self.has_artisanal_bow))
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.witherskeleton_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The wither skeleton found you and threw you into the backrooms.')
                    print(self.witherskeleton_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.archerhp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')

                if self.archerhp <= 0:
                    print("You died!")
                    return

            if self.witherskeleton_health.witherskeletonhp <= 0:
                print("You defeated the wither skeleton! Congratulations!")
                self.witherskeleton_health.killed(delay_duration)

        def encounter3(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.archerhp} hp, Wither: {self.wither_health.witherhp} hp')
            while self.wither_health.witherhp > 0:
                move = input('Pick your next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.wither_battle.shoot())
                    print(self.wither_health.shot(self.has_wither_bow))
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.wither_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The wither found you and threw you into the backrooms.')
                    print(self.wither_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.archerhp} hp, Wither: {self.wither_health.witherhp} hp')

                if self.archerhp <= 0:
                    print("You died!")
                    return

            if self.wither_health.witherhp <= 0:
                print("You defeated the wither! Congratulations!")
                self.wither_health.killed(delay_duration)

    class MageStoryline:
        def __init__(self):
            self.magehp = 20
            self.has_starlight_wand = self.check_starlight_wand()
            self.skeleton_battle = SkeletonBattle(self.magehp)
            self.skeleton_health = SkeletonHealth()
            self.witherskeleton_battle = WitherSkeletonBattle(self.magehp, self.has_starlight_wand)
            self.witherskeleton_health = WitherSkeletonHealth()
            self.has_hyperion = self.check_hyperion()
            self.wither_battle = WitherBattle(self.magehp, self.has_hyperion)
            self.wither_health = WitherHealth()

        def check_starlight_wand(self):
            try:
                with open("starlight_wand.json", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        return any(wand.get('starlight_wand_dropped') for wand in data)
                    else:
                        return data.get('starlight_wand_dropped', False)
            except (FileNotFoundError, json.JSONDecodeError):
                return False

        def check_hyperion(self):
            try:
                with open("hyperion.json", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        return any(weapon.get('hyperion_dropped') for weapon in data)
                    else:
                        return data.get('hyperion_dropped', False)
            except (FileNotFoundError, json.JSONDecodeError):
                return False

        def beginning(self, delay_duration):
            print("Your adventure begins now.")
            print('You look around, confused, you decide to wander around.')
            print('You search for answers, none to be found.')
            print('Until.')
            delay(delay_duration)
            print('You encounter a skeleton!')
            delay(delay_duration)
            print('It seemed agitated?')
            delay(delay_duration)
            print('It charges at you.')
            print('A battle of the ages begins.')
            delay(delay_duration)
            os.system("cls")
            print(f'Player: {self.magehp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')

        def encounter1(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.magehp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')
            while self.skeleton_health.skeletonhp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.skeleton_battle.shoot())
                    print(self.skeleton_health.shot())
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.skeleton_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The skeleton found you and threw you into the backrooms.')
                    print(self.skeleton_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.magehp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')

                if self.magehp <= 0:
                    print("You died!")
                    return

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton! Congratulations!")
                self.skeleton_health.killed(delay_duration)

        def encounter2(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.magehp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')
            while self.witherskeleton_health.witherskeletonhp > 0:
                move = input('Pick your next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.witherskeleton_battle.shoot())
                    print(self.witherskeleton_health.shot(self.has_starlight_wand))
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.witherskeleton_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The wither skeleton found you and threw you into the backrooms.')
                    print(self.witherskeleton_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.magehp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')

                if self.magehp <= 0:
                    print("You died!")
                    return

            if self.witherskeleton_health.witherskeletonhp <= 0:
                print("You defeated the wither skeleton! Congratulations!")
                self.witherskeleton_health.killed(delay_duration)

        def encounter3(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.magehp} hp, Wither: {self.wither_health.witherhp} hp')
            while self.wither_health.witherhp > 0:
                move = input('Pick your next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an attack.')
                    print(self.wither_battle.shoot())
                    print(self.wither_health.shot(self.has_hyperion))
                elif move == 'defend':
                    print('You defended, nice job!')
                    print(self.wither_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('The wither found you and threw you into the backrooms.')
                    print(self.wither_battle.run())
                else:
                    print('Please pick a valid move.')
                print(f'Player: {self.magehp} hp, Wither: {self.wither_health.witherhp} hp')

                if self.magehp <= 0:
                    print("You died!")
                    return

            if self.wither_health.witherhp <= 0:
                print("You defeated the wither! Congratulations!")
                self.wither_health.killed(delay_duration)

def delay(seconds):
    time.sleep(seconds)

def main():
    try:
        delay_duration = int(input("Enter delay duration in seconds (default 2): "))
    except ValueError:
        delay_duration = 2

    player_class = input("Choose your class (Archer, Mage): ").lower()
    if player_class == "archer":
        storyline = Storyline.ArcherStoryline()
        storyline.beginning(delay_duration)
        storyline.encounter1(delay_duration)
        storyline.encounter2(delay_duration)
        storyline.encounter3(delay_duration)
    elif player_class == "mage":
        storyline = Storyline.MageStoryline()
        storyline.beginning(delay_duration)
        storyline.encounter1(delay_duration)
        storyline.encounter2(delay_duration)
        storyline.encounter3(delay_duration)
    else:
        print("Invalid class choice. Please choose 'Archer' or 'Mage'.")

if __name__ == "__main__":
    main()