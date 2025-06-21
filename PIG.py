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

max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < max_score:

    for players_idx in range(players):
        print(f'\nPlayer {players_idx+1} turn get started!')
        print(f'Your total score is: {player_scores[players_idx]}')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)? ').lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a {value}!')
            
            print(f'Your score is {current_score}')
        
        player_scores[players_idx] += current_score
        print(f'Your total score is: {player_scores[players_idx]}')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f'Player {winning_idx+1} is the winner! With a score of: {max_score}')
