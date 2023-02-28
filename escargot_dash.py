# Escargot Dash


import random
import time
import sys

# Set up the constants
MAX_NUM_SNAIL = 4
MAX_NUM_LENGTH = 20
FINISH_LINE = 60

# Ask how many snails to race
while True:  # Keeps asking until the player enters a number
    response = input('How many snails will race?\n> ')
    if response.isdecimal():
        num_of_snails_racing = int(response)
        if 1 < num_of_snails_racing <= MAX_NUM_SNAIL:
            break
        print(f'Enter a number between 2 and {MAX_NUM_SNAIL}')


# Enter the names for each snail
snail_names = []  # List of string snail_names
for i in range(1, num_of_snails_racing + 1):
    while True:  # Keeps asking until the player enters a valid name
        name = input(f'Enter snail #{i} snail name\n> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snail_names:
            print('Choose a name that has not already been used.')
        else:
            break  # The entered name is acceptable
    snail_names.append(name)


# Display each snail at the start line
print('\n' * 30)
print('Start' + (' ' * (FINISH_LINE - len('Start'))) + 'Finish')
print('|' + (' ' * (FINISH_LINE - len('|'))) + '|')
snail_progress = {}
for snail_name in snail_names:
    print(snail_name[:MAX_NUM_LENGTH])
    print('@╜')
    # snail
    snail_progress[snail_name] = 0


time.sleep(1.5)  # The pause right before the race


while True:  # Main program loop
    # Pick a random snail to move forward
    for i in range(random.randint(1, num_of_snails_racing // 2)):
        random_snail_name = random.choice(snail_names)
        snail_progress[random_snail_name] += 1

        # Checks if a snail has reached the finish line
        if snail_progress[random_snail_name] == FINISH_LINE:
            print(random_snail_name, 'has won')

            sys.exit()

    # Cheat Code:
    if random_snail_name == 'Turbo':
        snail_progress['Turbo'] += 10
        time.sleep(0.5)
        if snail_progress['Turbo'] >= FINISH_LINE:
            print('Turbo has won!')
            print('That snail is fast!')
            sys.exit()

    # Display the start and finish lines
    print('Start' + (' ' * (FINISH_LINE - len('Start'))) + 'Finish')
    print('|' + (' ' * (FINISH_LINE - len('|'))) + '|')

    # Display the snails with name
    for snail_name in snail_names:
        space = snail_progress[snail_name]
        # print((' ' * space) + snail_name[:MAX_NUM_LENGTH] + '')
        print(('.' * space) + snail_name[:MAX_NUM_LENGTH] + '@╜')
