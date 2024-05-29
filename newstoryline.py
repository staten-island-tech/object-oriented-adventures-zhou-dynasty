import time, random, os, json

class SkeletonBattle:
    def __init__(self, archerhp, has_artisanal_bow):
        self.archerhp = archerhp
        self.has_artisanal_bow = has_artisanal_bow

    def shoot(self):
        damage = 2
        if self.has_artisanal_bow:
            damage += 5
        self.archerhp -= damage
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

    def defend(self):
        self.archerhp -= 1
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

    def run(self):
        self.archerhp -= 4
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

class SkeletonHealth:
    def __init__(self):
        self.skeletonhp = 30

    def shot(self, has_artisanal_bow):
        damage = 20
        if has_artisanal_bow:
            damage += 5
        self.skeletonhp -= damage
        if self.skeletonhp < 0:
            self.skeletonhp = 0
        return f'skeleton has {self.skeletonhp} hp left.'

    def killed(self, delay_duration):
        drop_chance = random.randint(1, 10)
        if drop_chance <= 5:
            result = {
                'artisanal_shortbow_dropped': True,
                'message': 'You dropped an artisanal shortbow.'
            }

            print('You dropped an artisanal shortbow.')
            delay(delay_duration)
            print('Nice!')
            with open('artisanal_shortbows.json', 'a') as json_file:
                json.dump(result, json_file)
                json_file.write('\n')
        else:
            result = None
            print('No drop, too bad too sad.')
        return result

class WitherSkeletonBattle:
    def __init__(self, archerhp, has_artisanal_bow):
        self.archerhp = archerhp
        self.has_artisanal_bow = has_artisanal_bow

    def shoot(self):
        damage = 3
        if self.has_artisanal_bow:
            damage += 5
        self.archerhp -= damage
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

    def defend(self):
        self.archerhp -= 1
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

    def run(self):
        self.archerhp -= 4
        if self.archerhp < 0:
            self.archerhp = 0
        return f'You have {self.archerhp} hp left.'

class WitherSkeletonHealth:
    def __init__(self):
        self.witherskeletonhp = 50

    def shot(self, has_artisanal_bow):
        damage = 20
        if has_artisanal_bow:
            damage += 5
        self.witherskeletonhp -= damage
        if self.witherskeletonhp < 0:
            self.witherskeletonhp = 0
        return f'Wither skeleton has {self.witherskeletonhp} hp left.'

    def killed(self, delay_duration):
        drop_chance = random.randint(1, 100)
        if drop_chance <= 25:
            result = {
                "wither_bow_dropped": True,
                "message": 'You dropped a wither bow.'
            }
            print(result["message"])
            delay(delay_duration)
            print('Nice!')
            with open('wither_bow.json', 'a') as json_file:
                json.dump(result, json_file)
                json_file.write('\n')
        else:
            result = None
            print('No drop, too bad too sad.')
            print("You can't win, AHAHAHAHAHA.")
        return result

class Storyline:
    class ArcherStoryline:
        def __init__(self):
            self.archerhp = 20
            self.has_artisanal_bow = self.check_artisanal_bow()
            self.skeleton_battle = SkeletonBattle(self.archerhp, self.has_artisanal_bow)
            self.skeleton_health = SkeletonHealth()
            self.witherskeleton_battle = WitherSkeletonBattle(self.archerhp, self.has_artisanal_bow)
            self.witherskeleton_health = WitherSkeletonHealth()

        def check_artisanal_bow(self):
            try:
                with open("artisanal_shortbows.json", encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        return any(bow.get('artisanal_shortbow_dropped') for bow in data)
                    else:
                        return data.get('artisanal_shortbow_dropped', False)
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
            print('A battle of the ages begin.')
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
                    print('You fired off an arrow.')
                    print(self.skeleton_battle.shoot())
                    print(self.skeleton_health.shot(self.has_artisanal_bow))
                elif move == 'defend':
                    print('You defended, nice job big back!.')
                    print(self.skeleton_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('skeleton found you and threw you into the backrooms.')
                    print(self.skeleton_battle.run())
                else:
                    print('Please pick a valid move.')

                self.archerhp = self.skeleton_battle.archerhp
                print(f'Player: {self.archerhp} hp, skeleton: {self.skeleton_health.skeletonhp} hp')

                if self.archerhp <= 0:
                    print("You died!")
                    break

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton! Congratulations skeleton warrior!")
                print(self.skeleton_health.killed(delay_duration))

        def encounter2(self, delay_duration):
            print(f'Player: {self.archerhp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')
            os.system('cls')
            while self.witherskeleton_health.witherskeletonhp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('Bro shot an arrow.')
                    print(self.witherskeleton_battle.shoot())
                    print(self.witherskeleton_health.shot(self.has_artisanal_bow))
                elif move == 'defend':
                    print('Bro defended.')
                    print(self.witherskeleton_battle.defend())
                elif move == 'run':
                    print('Bro tried running.')
                    delay(delay_duration)
                    print('HAHA WOMP WOMP.')
                    print(self.witherskeleton_battle.run())
                else:
                    print('PICK A MOVE GODDAMN')

                self.archerhp = self.witherskeleton_battle.archerhp
                print(f'Player: {self.archerhp} hp, Wither skeleton: {self.witherskeleton_health.witherskeletonhp} hp')

                if self.archerhp <= 0:
                    print("YOU SUCK AT SPORTS FATTY")
                    break

            if self.witherskeleton_health.witherskeletonhp <= 0:
                print("You defeated the wither skeleton! OCHEN KHOROSHO")
                print(self.witherskeleton_health.killed(delay_duration))

def delay(duration):
    time.sleep(duration)

delay_duration = int(input("Input delay: "))
storyline = Storyline()
archer_story = storyline.ArcherStoryline()
archer_story.beginning(delay_duration)
archer_story.encounter1(delay_duration)

with open("artisanal_shortbows.json", mode='w') as VariableName:
    json.dump(VariableName, {})
with open("wither_bow.json", mode='w') as VariableName:
    json.dump(VariableName, {})

"""archer_story.encounter2(delay_duration)"""
"""             def encounter():
                x = input('Pick your first move (Shoot, Defend, Run)').lower()
                if x == 'shoot':
                    print('You fired off an arrow.')
                    skeletonbattle.shoot()
                    skeletonhealth.shot()
                if x == 'defend':
                    print('You defended, smart.')
                    skeletonbattle.defend()
                    skeletonhealth.attackadefended()
                if x == 'run':
                    print('You attempted run.')
                    delay()
                    print('too bad too sad')
                    skeletonbattle.run()
                    skeletonhealth.hittingrunner()
                else:
                    print('please pick a move given')
                    storyline.archerstoryline.encounter()
                delay()
                print('Round 2')
            def encounter2():
                x = input('Pick your next move (Shoot, Defend, Run)').lower()
                if x == 'shoot':
                    print('You fired off a second arrow')
                    skeletonbattle.shoot()
                    skeletonhealth.shot()
                elif x == 'defend':
                    print('You defended, good job')
                    skeletonbattle.shoot()
                    skeletonhealth.shot()
                elif x == 'run':
                    print('wow.')
                    skeletonbattle.run()
                    skeletonhealth.hittingrunner()
                else:
                    print('please pick a move given')
                    storyline.archerstoryline.encounter2() """