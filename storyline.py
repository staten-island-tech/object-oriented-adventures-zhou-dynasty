import time
import os
import random
os.system("cls")
a = open("classes.py")

class loot:
        def random():
                randint = random.randint(1,10)
                if randint == [1, 2, 3, 4, 5]:
                        print('You dropped ')

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
                        print('You encounter a skeleton')
                        time.sleep(1)
                        print('It seems agitated?')
                        time.sleep(1)
                        print('It fires an arrow.')
                        print('A battle begins.')
                        time.sleep(1)
                        os.system("cls")
                        print('Player: 20 hp, Skeleton: 30 hp')            
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
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton hits you again for 1 damage.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 10/30 hp')          
                def defendcontinuance2():
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('The skeleton has died.')
                        time.sleep(2)
                        print('Player: 17/20 hp , Skeleton: 0 hp')     
                        time.sleep(1)                               
                        print('It dropped an Artisanal Shortbow (25 damage)')    
                def defend4():
                        print('You have chosen to Run.')
                        time.sleep(2)
                        print('After defending is insane.')
                        time.sleep(2)
                        print('Why coward out of a fight?')
                        time.sleep(2)
                        print("I'm taking away your privilege to run.")
                def run():
                        print('WRONG CHOICE, YOU ARE NOT ALLOWED TO RUN!!!!')
                        print('You have taken 3 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 15 hp, Skeleton: 30 hp')
                        time.sleep(1)
                def run2():
                        print('You have done 20 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 2 damage.')
                        time.sleep(2)
                        print('Player: 15/20 hp , Skeleton: 10/30 hp')
                def run3():
                        print('You have chosen to Defend for some reason.')
                        print('You have dealt 0 damage.')
                        time.sleep(2)
                        print('Skeleton attacks, dealing 1 damage.')
                        time.sleep(2)
                        print('Player: 15/20 hp, Skeleton: 30/30 hp')
                def rundefendcontinuance():
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
                        print('You have chosen to Run.')
                        print("Someone didn't learn their lesson")
                        time.sleep(2)
                        print('Why coward out of a fight?')
                        time.sleep(2)
                        print('You have taken 5 damage')
                        time.sleep(3)
                        print('Skeleton decides to take pity due to your stupidity')
                        time.sleep(2)
                        print('Player 10 hp, Skeleton: 10/30 hp')
                def runcontinuance():
                        print('You have chosen to run for a third time?')
                        print('This is the end of your miserable life.')
                        time.sleep(2)
                        print('If you wish to restart your run and be smarter this time.')
                        input('Enter the Letter Y, if not press the letter N').upper()
                def storyline2():
                        while True:
                                print('After a long or possibly fought battle, you finally defeated one mob.')
                                x = input('What do you wish to do (Travel North, Travel South, Quit):').title()
                                if x == 'Travel North':
                                        print('You begin your long and harsh journey.')
                                        print('It hopes of reaching some sort of civilziation.')
                                        time.sleep(2)
                                        print('Pushing through, using all your might, all your energy(at least try to imagine it)')
                                        time.sleep(1)
                                        print('After a long journey, you come upon a city, a well developed one matter of fact.')
                                        time.sleep(1)
                                        print('You wonder, why would there be such an advanced civilization in a world like this.')
                                        time.sleep(1)
                                        print('No matter, you wander into the civilization, you get stopped by a stranger.')
                                        time.sleep(1)
                                        print('Unknown: Hey!')
                                        print('You: Hi, who are you.')
                                        time.sleep(1)
                                        print('Walter: My name is Walter.')
                                        print('You: Hey Walter!')
                                        time.sleep(1)
                                        print('You: Nice to meet you.')
                                        print('You: What made you come up to me anyways Walter.')
                                        time.sleep(1)
                                        print('Walter: Oh you know, you looked a little bit lost and I just wanted to help.')
                                elif x == 'Travel South':
                                        print('You begin a long and harsh journey.')
                                        print('In hopes of reaching some sort of civilization.')
                                        time.sleep(2)
                                        print('You walk long and far, no person or building in sight.')
                                        print('You notice that something looks wrong?')
                                        time.sleep(2)
                                        print('You see a dark aura illuminating around one of the trees.')
                                        print('A dark skeleton appears, similar to the one you encountered within the beginning.')
                                        time.sleep(2)
                                        print("It's holding as word, it looks dangerous.")
                                        print('It begins charging at you, guess you gotta fight.')
                                        time.sleep(2)
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
                def storyline2southshoot():
                        'shoot1'
                        print('You fired off an arrow at it, it pierced through it.')
                        print("It attempts to strike with it's sword, it connects.")
                        time.sleep(3)
                        print('Player: 17 hp, Wither Skeleton: 30 hp')
                def storyline2southdefend():
                        'defend1'
                        print('You defend. ')
                        print('It does so much to help you not gonna lie.')
                        time.sleep(3)
                        print('You did not deal damage.')
                        print('The wither skeleton attacked dealing 1 damage.')
                        time.sleep(2)
                        print('Player 19 hp, Wither Skeleton 50 hp')
                def storyline2southshoot3():
                        'shoot3'
                        print('You kill it.')
                        print('Good Job.')
                        time.sleep(3)
                        print('Player 14 hp, Wither Skeleton 0 hp')
                def storyline2southdefend3():
                        'defend3'
                        print('Yeah this guy has no clue what he is doing.')
                        print('Player 17 hp, Wither Skeleton 50 hp')
                def storyline2southsouthshootdefend():
                        'attack, defend'
                        print('Defending after attacking, ingenious.')
                        print('You defend, only taking 1 damage.')
                        time.sleep(3)
                        print('Player 16 hp, Wither Skeleton 30 hp')
                def storyline2southshoot2():
                        'shoot2'
                        print('You fired off another arrow, you made another hole within it.')
                        print('It hits you again.')
                        time.sleep(3)
                        print('Player: 14 hp, Wither Skeleton 10 hp')
                def storyline2southshootdefendshoot():
                        'shoot defend shoot'
                        print('You fire off another arrow again.')
                        print('You dealt damage.')
                        time.sleep(3)
                        print('Learning already?')
                        print('The wither skeleton barely hit you.')
                        print('Player: 14 hp, Wither Skeleton 10 hp')
                def storyline2southshootdefenddefend():
                        print('Defend one more time and I will end this run.')
                        time.sleep(2)
                        print('Player: 16 hp, Wither Skeleton 0 hp')
                def storyline2southshootdefendefenddefend():
                        while True:
                                print('Bye.')
                                break
                def storyline2southshootdefendshootshoot():
                        'shoot, defend, shoot, shoot'
                        print('You killed it.')
                        print('Good job.')
                        time.sleep(3)
                        print('Player: 14 hp, Wither Skeleton 0 hp')
                def storyline2southdefend2():
                        'defend 2'
                        print('You defend again.')
                        print('Absolute genius.')
                        time.sleep(2)
                        print('The wither skeleton deals another 1 damage.')
                        time.sleep(1)
                        print('Player 18 hp, Wither Skeleton 50hp')
                def storyline2southdefend3():
                        'defend 3'
                        print('Defending a third time?')
                        print('Do you plan on just giving up???')
                        time.sleep(3)
                        print('Player 17 hp, Wither Skeleton 50 hp')
                def storyline2southdefend4():
                        'defend 4'
                        while True:
                                print('Well since you wish on doing no damage.')
                                print('Might as well end this run because you are wasting my time.')
                                time.sleep(3)
                                break
                def storyline2continuance():
                        while True:
                                y = input('Walter: Come with me. (Follow, Leave)').upper()
                                if y == 'Follow':
                                                print('You begin following Walter.')
                                                print('You end up in his house somehow.')
                                                time.sleep(2)
                                                print('Walter: Go to sleep, it is dark out, dw I gotchu.')
                                                print('You follow his request for some reason??')
                                                time.sleep(1)
                                                print('Never trust Walter, he killed you in your sleep.')
                                                print('Bye Bye!!')
                                                break
                                elif y == 'Leave':
                                                print('You are lucky this time buddy.')
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
                                                storyline.archerstoryline.storyline2continuance()

class Selector1:
        def selector():
                while True:
                        p = input('Pick your move (Shoot, Defend, Run): ').capitalize()
                        if p == 'Shoot':
                                storyline.archerstoryline.shoot()
                        r = input('Pick your next move (Shoot, Defend, Run): ').capitalize()
                        if r == 'Shoot':
                                storyline.archerstoryline.shoot2()
                                break
                        elif r == 'Defend': 
                                storyline.archerstoryline.shoot3()
                        q = input('Pick your next move (Only Shoot Available): ').capitalize()
                        if q == 'Shoot':
                                storyline.archerstoryline.shootcontinuance3()
                        elif r == 'Run':
                                storyline.archerstoryline.shoot4()
                        g = input('Pick your next move (Only Shoot Available): ').capitalize()
                        if g == 'Shoot':
                                storyline.archerstoryline.shootcontinuance4()
                                break
                        elif p == 'Defend':
                                storyline.archerstoryline.defend()
                        r = input('Pick your next move (Shoot, Defend, Run): ').capitalize()
                        if r == 'Shoot':
                                storyline.archerstoryline.defend2()
                        e = input('Pick your next move (Pick Shoot)').capitalize()
                        if e == 'Shoot':
                                storyline.archerstoryline.defendshootcontinuance()
                        elif r == 'Defend':
                                storyline.archerstoryline.defend3()
                        g = input('Pick your next move (Must pick Shoot): ').capitalize()
                        if g == 'Shoot':
                                storyline.archerstoryline.defendcontinuance()
                                time.sleep(10)
                                print("I've decided to move for you.")
                                storyline.archerstoryline.defendcontinuance2()
                                break
                        elif r == 'Run':
                                storyline.archerstoryline.defend4()
                                print('pick an actual option give, thanks')
                                Selector1.selector()
                        elif p == 'Run':
                                storyline.archerstoryline.run()
                        r = input('Pick your next move (Shoot, Defend, Run): ').lower()
                        if r == 'shoot':
                                storyline.archerstoryline.run2()
                        elif r == 'defend':
                                storyline.archerstoryline.run3()
                                time.sleep(10)
                                print("You raise your bow in preperation to shoot.")
                                storyline.archerstoryline.rundefendcontinuance
                                time.sleep(10)
                                print('It suddenly happens again???')
                                storyline.archerstoryline.rundefendcontinuance2
                        elif r == 'run':
                                storyline.archerstoryline.run4()
                        e = input('Pick your next move (Shoot, Defend, Run): ').lower()
                        if e == 'shoot':
                                storyline.archerstoryline('placeholder') 
                        if e == 'Run':
                                storyline.archerstoryline.runcontinuance()
                        else:
                                print('pick an actual option given, thanks')
                                Selector1.selector()

class Selector2():
        def selector2():
                        while True:
                                r = input('Pick your move (Shoot, Defend): ').lower
                                if r == 'shoot':
                                        storyline.archerstoryline.storyline2southshoot()