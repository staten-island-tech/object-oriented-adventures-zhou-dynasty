import time
a = open("classes.py")


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
            "shoot"
            time.sleep(1)
            print('You have done 20 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 18/20 hp , Skeleton: 10/30 hp')
    def shoot2():
            "shoot, shoot"
            time.sleep(1)
            print('You have done 20 damage.')
            time.sleep(2)
            print('The skeleton has sadly passed away due to you piercing it with your arrow.')
            time.sleep(2)
            print('Player: 18/20 hp , Skeleton: 0/30 hp')
    def shoot3():
            "shoot, defend"
            time.sleep(1)
            print('You have done 0 damage.')
            time.sleep(2)
            print('The skeleton hits you again for 1 damage.')
            time.sleep(2)
            print('Player: 17/20 hp , Skeleton: 10/30 hp')     
    def shoot4():
            "shoot,run"
            time.sleep(1)
            print('No Running')
            time.sleep(2)
            print('The skeleton hits you again for 4 damage.')
            time.sleep(2)
            print('Player: 14/20 hp , Skeleton: 10/30 hp')            
    def defend():
            "defend"
            time.sleep(2)
            print('You have decided to defend, no damage dealt.')
            time.sleep(2)
            print('Skeleton attacks, dealing 1 damage.')
            time.sleep(2)
            print('Player: 19/20 hp, Skeleton: 30 hp')
    def defend2():
            "defend, shoot"
            time.sleep(2)
            print('You have chosen to shoot.')
            time.sleep(2)
            print('You have dealt 20 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 17/20 hp, Skeleton: 10 hp')
    def defendshootcontinuance():
           "defend, shoot, shoot"
           "only option to shoot"
           "else, pick the option given"
           time.sleep(2)
    def defend3():
            "defend, defend"
            time.sleep(2)
            print('You have chosen to Defend again for some reason.')
            time.sleep(2)
            print('You have dealt 0 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 1 damage.')
            time.sleep(2)
            print('Player: 18/20 hp, Skeleton: 10 hp')
    def defendcontinuance():
            'defend, defend, defend'
            time.sleep(2)
            print('Defending again???')
            time.sleep(2)
            print('You have dealt no damage but taken 1 again.')
            time.sleep(2)
            print('Player: 16/20 hp, Skeleton: 10 hp')
    def defend4():
            "defend,run"
            time.sleep(2)
            print('You have chosen to Run.')
            time.sleep(2)
            print('After defending is insane.')
            time.sleep(2)
            print('Why coward out of a fight?')
            time.sleep(2)
            print("I'm taking away your privilege to run.")
    def run():
            "run"
            print('WRONG CHOICE, YOU ARE NOT ALLOWED TO RUN!!!!')
            time.sleep(3)
            print('You have taken 3 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 15/20, Skeleton: 30 hp')
            time.sleep(1)
    def run2():
            "run, shoot"
            time.sleep(1)
            print('You have done 20 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 2 damage.')
            time.sleep(2)
            print('Player: 18/20 hp , Skeleton: 10/30 hp')
    def run3():
            "run, defend"
            time.sleep(2)
            print('You have chosen to Defend for some reason.')
            time.sleep(2)
            print('You have dealt 0 damage.')
            time.sleep(2)
            print('Skeleton attacks, dealing 1 damage.')
            time.sleep(2)
            print('Player: 18/20 hp, Skeleton: 10/30 hp')
    def run4():
            "run, run"
            time.sleep(2)
            print('You have chosen to Run.')
            time.sleep(2)
            print("Someone didn't learn their lesson")
            time.sleep(2)
            print('Why coward out of a fight?')
            time.sleep(2)
            print('You have taken 5 damage')
            time.sleep(3)
            print('Skeleton decides to take pity due to your stupidity')
            time.sleep(2)
            print('Player 10/20, Skeleton: 10/30 hp')
    def runcontinuance():
            "input next move"
            "run, run, run"
            print('You have chosen to run for a third time?')
            time.sleep(2)
            print('This is the end of your miserable life.')
            time.sleep(2)
            print('If you wish to restart your run and be smarter this time.')
            input('Enter the Letter Y, if not press the letter N').upper()