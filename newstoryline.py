import time, os,  random
os.system("cls")
a = open("classes.py")

x = archerhp = 20
class skeletonbattle:
    def shoot():
        x = archerhp - 2
        return(f'You have {x} hp left.')
    def defend():
        x = archerhp - 1
        return(f'You have {x} hp left.')
    def death():
        while True:
            if x == 0:
                return(f'You have {x} hp left.')
            break
y = skeletonhp = 30
class skeletonhealth:
    def shot():
        y = skeletonhp - 20
        return(f'Skeleton has {y} hp left.')
    def attackadefended():
        y = skeletonhp - 0
        return(f'Skeleton has {y} hp left.')
    def killed():
        y = print(random.randint(1,10))
        if y == '1,2,3,4,5':
            print('You dropped an artisanal shortbow.')
            delay()
            print('Nice!')
        else: 
            print('No drop, too bad too sad.')
        y = skeletonhp == 0
        return(f'Skeleton has {y} hp left.')


def delay():
    time.sleep(2)          
class storyline:
        class archerstoryline:
            def __init__(self):
                self.archerstoryline = True 
            def beginning(): 
                print("Your adventure begins now {username}.")
                delay()
                print('You look around, confused, you decide to wander around.')
                delay()
                print('You search for answers, none to be found.')
                delay()
                print('Until.')
                time.sleep(1)
                print('You encounter a skeleton!')
                time.sleep(1)
                print('It seems agitated?')
                time.sleep(1)
                print('It charges at you.')
                print('A battle begins.')
                time.sleep(1)
                os.system("cls")
                print('Player: 20 hp, Skeleton: 30 hp')
            def encounter():
                x - input('Pick your first move (Shoot, Defend, Run)').lower()
                if x == 'shoot':
                    print('You fired off an arrow.')
                    skeletonbattle.shoot()
