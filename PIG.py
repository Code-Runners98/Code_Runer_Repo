import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input('Enter the number of players (min - 2, max - 4): ')
    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        
        else:
            print('Value of players must be from 2 to 4. Try again')

    else:
        print('You must use numbers(from 2 to 4) to chouse numbers of players')

print(players)
