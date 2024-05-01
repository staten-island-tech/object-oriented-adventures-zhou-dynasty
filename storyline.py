import time

class storyline():
    def __init__(self):
        self.storyline = True 

    def archer():
        print('Your adventure begins now {username}.')
        time.sleep(2)
        print('You look around, confused, you decide to wander around.')
        time.sleep(1)
        print('You search for answers, none to be found.')
        time.sleep(4)
        print('UNTIL......')
        print('You encounter a skeleton, a fierce battle begins.')
        time.sleep(3)
    def shoot():
        x = input('Choose your move (Shoot, Defend, Run): ').upper()
        if x == 'Shoot':
            time.sleep(1)
            print('You have done 20 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 8/10 hp , Skeleton: 10/30 hp')
    def defend():
        x = input('Choose your move (Shoot, Defend, Run): ').upper()
        if x == 'Defend':
            time.sleep(2)
            print('You have decided to defend, no damage dealt.')
            time.sleep(2)
            print('Skeleton attacks, dealing 1 damage.')
            time.sleep(2)
            print('Player: 9/10 hp, Skeleton: 30 hp')
    def defend2():
        y = input('Choose your next move (Shoot, Defend, Run): ').upper()
        if y == 'Shoot':
            time.sleep(2)
            print('You have chosen to shoot.')
            time.sleep(2)
            print('You have dealt 20 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 8/10 hp, Skeleton: 10 hp')
    def run():
        x = input('Choose your move (Shoot, Defend, Run): ').upper()
        if  x == 'Run':
            print('WRONG CHOICE, YOU ARE NOT ALLOWED TO RUN!!!!')
            time.sleep(3)
            print('You have taken 3 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 5/10, Skeleton: 30 hp')
            time.sleep(1)
        y = input("Pick your next move: ")
        if y == 'Shoot':
            time.sleep(2)
        print('You have done 20 damage.')
        time.sleep(2)
        print('Skeleton attacks, dealing 2 damage')
        time.sleep(2)
        print('Player: 7/10 hp, Skeleton: 10/30 hp')

        if y == 'Shoot':
            time.sleep(3)
            print('You have done 20 damage.')
            time.sleep(2)
            print('Skeleton')