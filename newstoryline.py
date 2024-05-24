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
            with open('artisanal_shortbows.json', 'w+') as json_file:
                json.dump(result, json_file)
                json_file.write('\n')
        else:
            result = None
            print('No drop, too bad too sad.')
        return result
class Witherskeletonbattle:
    def __init__(self):
        pass


class Witherskeletonhealth:
    def init(self):
        self.witherskeletonhp = 50

    def shot1(self, has_artisinal_shortbow):
        if has_artisinal_shortbow:
            self.witherskeletonhp -= 25
        else:
            self.witherskeletonhp -= 20

        if self.skeletonhp < 0:
            self.skeletonhp = 0
        return f'Skeleton has {self.skeletonhp} hp left.'
class Storyline:
    class ArcherStoryline:
        def __init__(self):
            self.skeleton_battle = SkeletonBattle()
            self.skeleton_health = SkeletonHealth()

        def beginning(self, delay_duration):
            print("Your adventure begins now.")
            print('You look around, confused, you decide to wander around.')
            delay(delay_duration)
            print('You search for answers, none to be found.')
            delay(delay_duration)
            print('Until.')
            delay(delay_duration)
            print('You encounter a skeleton.')
            delay(delay_duration)
            print('It seems agitated?')
            delay(delay_duration)
            print('It charges at you.')
            delay(delay_duration)
            print('A battle begins.')
            delay(delay_duration)
            os.system("cls")
            print(f'Player: {self.skeleton_battle.archerhp} hp, Skeleton: {self.skeleton_health.skeletonhp} hp')
            self.encounter1(1)

        def encounter1(self, delay_duration):
            while self.skeleton_health.skeletonhp > 0:
                os.system('cls')
                print('Player: 20 hp, Skeleton: 30 hp')
                move = input('Pick your first move (Shoot, Defend, Run): ').lower()
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
                    print("You died, hahahahahahha")
                    break

            if self.skeleton_health.skeletonhp <= 0:
                print("You defeated the skeleton!")
                print(self.skeleton_health.killed(delay_duration))

                
""" class storylinecontinuance:
    def storyline2():
        while True:
            print('After a long or possibly fought battle, you finally defeated one mob.')
            x = input('What do you wish to do (Travel North, Travel South, Quit):').title()
            if x == 'Travel North':
                print('You begin your long and harsh journey.')
                print('It hopes of reaching some sort of civilziation.')
                delay(delay_duration)
                print('Pushing through, using all your might, all your energy(at least try to imagine it)')
                print('After a long journey, you come upon a city, a well developed one matter of fact.')
                delay(delay_duration)
                print('You wonder, why would there be such an advanced civilization in a world like this.')
                print('No matter, you wander into the civilization, you get stopped by a stranger.')
                delay(delay_duration)
                print('Unknown: Hey!')
                print('You: Hi, who are you.')
                delay(delay_duration)
                print('Walter: My name is Walter.')
                print('You: Hey Walter!')
                delay(delay_duration)
                print('You: Nice to meet you.')
                print('You: What made you come up to me anyways Walter.')
                delay(delay_duration)
                print('Walter: Oh you know, you looked a little bit lost and I just wanted to help.')
            elif x == 'Travel South':
                print('You begin a long and harsh journey.')
                print('In hopes of reaching some sort of civilization.')
                delay(delay_duration)
                print('You walk long and far, no person or building in sight.')
                print('You notice that something looks wrong?')
                delay(delay_duration)
                print('You see a dark aura illuminating around one of the trees.')
                print('A dark skeleton appears, similar to the one you encountered within the beginning.')
                delay(delay_duration)
                print("It's holding as word, it looks dangerous.")
                print('It begins charging at you, guess you gotta fight.')
                delay(delay_duration)
                os.system('cls')
                print('Your hp has been reset from the last fight, at the cost of the run move.')
                print('Player: 20 hp, Wither Skeleton: 50 hp')
            elif x == 'Quit':
                print('You have decided to quit, Goodbye!!!')
                print('Your progress does not save, have fun!!!')
                break
            else:
                print('Pick a choice given, thanks')
                storyline.archerstoryline.storyline2()
class storyline2continuance():
    def storyline2continuance():
        while True:
            y = input('Walter: Come with me. (Follow, Leave)').upper()
            if y == 'Follow':
                print('You begin following Walter.')
                print('You end up in his house somehow.')
                delay(delay_duration)
                print('Walter: Go to sleep, it is dark out, dw I gotchu.')
                print('You follow his request for some reason??')
                delay(delay_duration)
                print('Never trust Walter, he killed you in your sleep.')
                print('Bye Bye!!')
                break
            elif y == 'Leave':
                ('You are lucky this time buddy.')
                print('Did not listen to a Walter, smart.')
                time.sleep(2)
                print('You: No thanks, Im more of an indepedent guy.')
                print('Walter: Aw man, well see you around.')
                time.sleep(2)
                print('You: Bye!')
                print('As you both begin to part ways, your mind starts racing, what would have happened if you actually decided to follow him.')
                time.sleep(2)
                print('Would would have happened to me, you ponder.')
                print('But anyways you decide to wander off, deeper into the heart of the city.')
                time.sleep(2)
                print("You check your pockets and remember you don't got money..")
                print('Fluckers.')
                time.sleep(2)
                print('You decide to head back out, in pitch darkness.')
                print('It was never a good idea, you ended up getting jumped by a bunch of drunk hooligans and passed on into the afterlife.')
                time.sleep(2)
                print('AHAHAHAAHAHAHAHA, BYE')
                break
            else:
                print('please pick an option within the parentheses, thanks')
                storyline.archerstoryline.storyline2continuance() """
def delay(duration):
    time.sleep(duration)

print('Do not say 0 for input.')
delay_duration = int(input("Input delay: "))
storyline = Storyline()
archer_story = storyline.ArcherStoryline()
archer_story.beginning(delay_duration)
# archer_story.encounter1(delay_duration)

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