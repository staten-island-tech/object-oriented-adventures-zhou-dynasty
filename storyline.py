import time

print('Your adventure begins now {username}.')
time.sleep(1)
print('You encounter a skeleton, a fierce battle begins.')
time.sleep(3)
x = input(print('Pick (Fight, Defend, Run): '))
if x == 'Fight':
    print('')
elif x == 'Defend':
    print('You lost 2 health points')
elif x == 'Run':
    print("WRONG CHOICE, you're not allowed to run")
    print('You lost 5 health points')
    print()