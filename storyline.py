import time
a = open("classes.py")

class storyline:
        class archerstoryline():
                def __init__(self):
                        self.archerstoryline = True 

                def archer():
                        print('Your adventure begins now {username}.')
                        time.sleep(2)
                        print('You look around, confused, you decide to wander around.')
                        time.sleep(1)
                        print('You search for answers, none to be found.')
                        time.sleep(3)
                        print('Until.')
                        time.sleep(2)
                        print('You encounter a skeleton, a fierce battle begins.')
                        time.sleep(3)
                        print('Player: 20 hp')
                
                def shoot():
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 18/20 hp , Skeleton: 10/30 hp')
                def shoot2():
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton has sadly passed away due to you piercing it with your arrow.')
                        time.sleep(2)
                        print('Player: 18/20 hp , Skeleton: 0/30 hp')
                def shoot3():
                        print('You have done 0 damage.')
                        time.sleep(2)
                        print('The skeleton hits you again for 1 damage.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 10/30 hp')     
                def shootcontinuance3():
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton has passed away due to your shot.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 0 hp')                         
                def shoot4():
                        print('No Running')
                        time.sleep(2)
                        print('The skeleton hits you again for 4 damage.')
                        time.sleep(2)
                        print('Player: 14/20 hp , Skeleton: 10/30 hp')            
                def shootcontinuance4():
                        print('You shoot to kill.')
                        time.sleep(2)
                        print('The skeleton has died from your arrow.')
                        time.sleep(2)
                        print('Player: 14 hp, Skeleton 0 hp')
                        time.sleep(1)
                        print('It dropped an Artisanal Shortbow (25 damage)')
                def defend():
                        print('You have decided to defend, no damage dealt.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 1 damage.')
                        time.sleep(2)
                        print('Player: 19/20 hp, Skeleton: 30 hp')
                def defend2():
                        print('You have chosen to shoot.')
                        time.sleep(2)
                        print('You have dealt 20 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 17/20 hp, Skeleton: 10 hp')
                def defendshootcontinuance():
                        print('You killed the skeleton.')
                        time.sleep(2)
                        print('Player: 17/20, Skeleton: 0 hp')
                        print('It dropped an Artisanal Shortbow (25 damage)')
                        print('Your reward for wasting this much time.')
                def defend3():
                        print('You have chosen to Defend again for some reason.')
                        time.sleep(2)
                        print('You have dealt 0 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 1 damage.')
                        time.sleep(2)
                        print('Player: 18/20 hp, Skeleton: 10 hp')
                def defendcontinuance():
                        'defend, defend, shoot'
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton hits you again for 1 damage.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 10/30 hp')          
                def defendcontinuance2():
                        "defend, defend, shoot, shoot"
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton has died.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 0 hp')     
                        time.sleep(1)                               
                        print('It dropped an Artisanal Shortbow (25 damage)')    
                def defend4():
                        "defend,run"
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
                        print('You have taken 3 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 15 hp, Skeleton: 30 hp')
                        time.sleep(1)
                def run2():
                        "run, shoot"
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 15/20 hp , Skeleton: 10/30 hp')
                def run3():
                        "run, defend"
                        print('You have chosen to Defend for some reason.')
                        print('You have dealt 0 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 1 damage.')
                        time.sleep(2)
                        print('Player: 15/20 hp, Skeleton: 30/30 hp')
                def rundefendcontinuance():
                        "run, defend, shoot"
                        "force them to shoot"
                        print('You have done damage.')
                        print('Skeleton has also done damage')
                        time.sleep(2)
                        print('Player: 13 hp, Skeleton 10 hp')
                def rundefendcontinuance2():
                        'run, defend, shoot, shoot'
                        'force them to shoot again'
                        print('Player has shot again, killing the skeleton')
                        print('Took long enough.')
                        time.sleep(2)
                        print('Player: 13 hp, Skeleton 0 hp')
                def run4():
                        "run, run"
                        print('You have chosen to Run.')
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
                        print('You have chosen to run for a third time?')
                        print('This is the end of your miserable life.')
                        time.sleep(2)
                        print('If you wish to restart your run and be smarter this time.')
                        input('Enter the Letter Y, if not press the letter N').upper()
                def storyline2():
                        print('After a long or possibly fought battle, you finally defeated one mob.')
                        input('What do you wish to do: ')

def selector():
        while True:
                print('Please make the first letter uppercase, and choose a given option')
                p = input('Pick your move (Shoot, Defend, Run): ')
                if p == 'Shoot':
                        storyline.archerstoryline.shoot()
                        r = input('Pick your next move (Shoot, Defend, Run): ')
                        if r == 'Shoot':
                                storyline.archerstoryline.shoot2()
                                break
                        elif r == 'Defend': 
                                storyline.archerstoryline.shoot3()
                        q = input('Pick your next move (Only Shoot Available): ')
                        if q == 'Shoot':
                                storyline.archerstoryline.shootcontinuance3
                        elif r == 'Run':
                                storyline.archerstoryline.shoot4()
                        g = input('Pick your next move (Only Shoot Available): ')
                        if g == 'Shoot':
                                storyline.archerstoryline.shootcontinuance4
                                break
                        else:
                                print('pick an actual option give, thanks')
                                selector()
                elif p == 'Defend':
                        storyline.archerstoryline.defend()
                        r = input('Pick your next move (Shoot, Defend, Run): ')
                        if r == 'Shoot':
                                storyline.archerstoryline.defend2()
                        e = input('Pick your next move (Pick Shoot)')
                        if e == 'Shoot':
                                storyline.archerstoryline.defendshootcontinuance
                        elif r == 'Defend':
                                storyline.archerstoryline.defend3()
                        g = input('Pick your next move (Must pick Shoot): ')
                        if g == 'Shoot':
                                storyline.archerstoryline.defendcontinuance
                                time.sleep(10)
                                print("I've decided to move for you.")
                                storyline.archerstoryline.defendcontinuance2
                                break
                        elif r == 'Run':
                                storyline.archerstoryline.defend4()
                                print('pick an actual option give, thanks')
                                selector()
                elif p == 'Run':
                        storyline.archerstoryline.run()
                        r = input('Pick your next move (Shoot, Defend, Run): ')
                        if r == 'Shoot':
                                storyline.archerstoryline.run2()
                        elif r == 'Defend':
                                storyline.archerstoryline.run3()
                                time.sleep(10)
                                print("You raise your bow in preperation to shoot.")
                                storyline.archerstoryline.rundefendcontinuance
                                time.sleep(10)
                                print('It suddenly happens again???')
                                storyline.archerstoryline.rundefendcontinuance2
                        elif r == 'Run':
                                storyline.archerstoryline.run4()
                        e = input('Pick your next move (Shoot, Defend, Run): ')
                        if e == 'Shoot':
                                storyline.archerstoryline()
                        if e == 'Run':
                                storyline.archerstoryline.runcontinuance()
                else:
                        print('pick an actual option given, thanks')
selector()
