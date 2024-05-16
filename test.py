import time
import os

class storyline:
        class archerstoryline():
                def __init__(self):
                        self.archerstoryline = True 
        
        def storyline2():
                        while True:
                                print('After a long or possibly fought battle, you finally defeated one mob.')
                                x = input('What do you wish to do (Travel North, Travel South, Quit): ').title()
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
        def storyline2south():
                        while True:
                                x = 'a'
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
storyline.storyline2continuance()