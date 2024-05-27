import time, random, os, json

class SkeletonBattle:
    def __init__(self):
        self.archerhp = 20

    def shoot(self):
        self.archerhp -= 2
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

    def shot(self):
        self.skeletonhp -= 20
        if self.skeletonhp < 0:
            self.skeletonhp = 0
        return f'Skeleton has {self.skeletonhp} hp left.'

    def attackadefended(self):
        return f'Skeleton has {self.skeletonhp} hp left.'

    def hittingrunner(self):
        return f'Skeleton has {self.skeletonhp} hp left.'

    def killed(self, delay_duration):
        drop_chance = random.randint(1, 10)
        if drop_chance <= 5:
            result = {
                "artisanal_shortbow_dropped": True,
                "message": 'You dropped an artisanal shortbow.'
            }
            print(result["message"])
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
    def init(self):
        self.witherskeletonhp = 50

    def shot(self, has_artisinal_shortbow):
        if has_artisinal_shortbow:
            self.witherskeletonhp -= 25
        else:
            self.witherskeletonhp -= 20

        if self.witherskeletonhp < 0:
            self.witherskeletonhp = 0
        return f'Skeleton has {self.witherskeletonhp} hp left.'

class Storyline:
    class ArcherStoryline:
        def __init__(self):
            self.skeleton_battle = SkeletonBattle()
            self.skeleton_health = SkeletonHealth()

        def beginning(self, delay_duration):
            print("Your adventure begins now.")
            print('You look around, confused, you decide to wander around.')
            print('You search for answers, none to be found.')
            print('Until.')
            delay(delay_duration)
            print('You encounter a skeleton!')
            delay(delay_duration)
            print('It seems agitated?')
            delay(delay_duration)
            print('It charges at you.')
            print('A battle begins.')
            delay(delay_duration)
            os.system("cls")
            print(f'Player: {self.skeleton_battle.archerhp} hp, Skeleton: {self.skeleton_health.skeletonhp} hp')

        def encounter1(self, delay_duration):
            os.system('cls')
            print('Player: 20 hp, Skeleton: 30 hp')
            while self.skeleton_health.skeletonhp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an arrow.')
                    print(self.skeleton_battle.shoot())
                    print(self.skeleton_health.shot())
                elif move == 'defend':
                    print('You defended, smart.')
                    print(self.skeleton_battle.defend())
                    print(self.skeleton_health.attackadefended())
                elif move == 'run':
                    print('You attempted to run.')
                    delay(delay_duration)
                    print('Too bad, too sad.')
                    print(self.skeleton_battle.run())
                    print(self.skeleton_health.hittingrunner())
                else:
                    print('Please pick a valid move.')
                
                if self.skeleton_battle.archerhp <= 0:
                    self.skeleton_battle.archerhp = 0
                    print("You died!")
                    break

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton!")
                print(self.skeleton_health.killed(delay_duration))

        def encounter2(self, delay_duration):
            os.system('cls')
            print('Player: 20 hp, Wither Skeleton: 50 hp')
            while self.skeleton_health.skeletonhp > 0:
                move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
                os.system('cls')
                if move == 'shoot':
                    print('You fired off an arrow.')
                    print(self.skeleton_battle.shoot())
                    print(self.skeleton_health.shot())
                elif move == 'defend':
                    print('You defended, smart.')
                    print(self.skeleton_battle.defend())
                    print(self.skeleton_health.attackadefended())
                elif move == 'run':
                    print('You attempted to run.')
                    delay(delay_duration)
                    print('Too bad, too sad.')
                    print(self.skeleton_battle.run())
                    print(self.skeleton_health.hittingrunner())
                else:
                    print('Please pick a valid move.')
                
                if self.skeleton_battle.archerhp <= 0:
                    self.skeleton_battle.archerhp = 0
                    print("You died!")
                    break

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton!")
                print(self.skeleton_health.killed(delay_duration))

def delay(duration):
    time.sleep(duration)

delay_duration = int(input("Input delay: "))
storyline = Storyline()
archer_story = storyline.ArcherStoryline()
archer_story.beginning(delay_duration)
archer_story.encounter1(delay_duration)

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