import time, random, os, json

class SkibidiBattle:
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

class SkibidiHealth:
    def __init__(self):
        self.skibidihp = 30

    def shot(self, has_artisanal_bow):
        damage = 20
        if has_artisanal_bow:
            damage += 5
        self.skibidihp -= damage
        if self.skibidihp < 0:
            self.skibidihp = 0
        return f'Skibidi has {self.skibidihp} hp left.'

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

class WitherSkibidiBattle:
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

class WitherSkibidiHealth:
    def __init__(self):
        self.witherskibidihp = 50

    def shot(self, has_artisanal_bow):
        damage = 20
        if has_artisanal_bow:
            damage += 5
        self.witherskibidihp -= damage
        if self.witherskibidihp < 0:
            self.witherskibidihp = 0
        return f'Wither Skibidi has {self.witherskibidihp} hp left.'

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
            self.skibidi_battle = SkibidiBattle(self.archerhp, self.has_artisanal_bow)
            self.skibidi_health = SkibidiHealth()
            self.witherskibidi_battle = WitherSkibidiBattle(self.archerhp, self.has_artisanal_bow)
            self.witherskibidi_health = WitherSkibidiHealth()

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
            print('You encounter a level 30k GYAT skibidi toilet!!')
            delay(delay_duration)
            print('It seemed fanum taxed?')
            delay(delay_duration)
            print('It invited you to a tiktok rizz party.')
            print('A battle of the original gangster begins.')
            delay(delay_duration)
            os.system("cls")
            print(f'Player: {self.archerhp} hp, Skibidi: {self.skibidi_health.skibidihp} hp')

        def encounter1(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.archerhp} hp, Skibidi: {self.skibidi_health.skibidihp} hp')
            while self.skibidi_health.skibidihp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an AUSTRALIAN arrow.')
                    print(self.skibidi_battle.shoot())
                    print(self.skibidi_health.shot(self.has_artisanal_bow))
                elif move == 'defend':
                    print('You defended, nice job big back!.')
                    print(self.skibidi_battle.defend())
                elif move == 'run':
                    print('You attempted to vent to a different location.')
                    delay(delay_duration)
                    print('Skibidi found you and threw you into the backrooms.')
                    print(self.skibidi_battle.run())
                else:
                    print('Please pick a valid move.')

                self.archerhp = self.skibidi_battle.archerhp
                print(f'Player: {self.archerhp} hp, Skibidi: {self.skibidi_health.skibidihp} hp')

                if self.archerhp <= 0:
                    print("You died of ligma!")
                    break

            if self.skibidi_health.skibidihp <= 0:
                print("You defeated the skibidi! Congratulations skibidi warrior!")
                print(self.skibidi_health.killed(delay_duration))

        def encounter2(self, delay_duration):
            os.system('cls')
            print(f'Player: {self.archerhp} hp, Wither Skibidi: {self.witherskibidi_health.witherskibidihp} hp')
            while self.witherskibidi_health.witherskibidihp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('Bro shot an arrow.')
                    print(self.witherskibidi_battle.shoot())
                    print(self.witherskibidi_health.shot(self.has_artisanal_bow))
                elif move == 'defend':
                    print('Bro defended.')
                    print(self.witherskibidi_battle.defend())
                elif move == 'run':
                    print('Bro tried running.')
                    delay(delay_duration)
                    print('HAHA BWOMP WOMP.')
                    print(self.witherskibidi_battle.run())
                else:
                    print('PICK A MOVE GODDAMN')

                self.archerhp = self.witherskibidi_battle.archerhp
                print(f'Player: {self.archerhp} hp, Wither Skibidi: {self.witherskibidi_health.witherskibidihp} hp')

                if self.archerhp <= 0:
                    print("YOU SUCK AT SPORTS FATTY")
                    break

            if self.witherskibidi_health.witherskibidihp <= 0:
                print("You defeated the wither skibidi! OCHEN KHOROSHO")
                print(self.witherskibidi_health.killed(delay_duration))

def delay(duration):
    time.sleep(duration)

delay_duration = int(input("Input delay: "))
storyline = Storyline()
archer_story = storyline.ArcherStoryline()
archer_story.beginning(delay_duration)
archer_story.encounter1(delay_duration)

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