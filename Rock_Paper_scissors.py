import random

user_wins = 0
computer_wins = 0

options = ["ROCK", "PAPER", "SCISSORS"]

while True:
    user_input = " ".join(input('Type Rock/Paper/Scissors or Q to quit. ').upper().split())
    if user_input == "Q":
        break
    
    if user_input not in options:
        print('Value is not valid, try again')
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f'Computer picked: {computer_pick}')

    if user_input == 'ROCK' and computer_pick == 'SCISSORS':
        print('You won!')
        user_wins += 1

    elif user_input == 'PAPER' and computer_pick == 'ROCK':
        print('You won!')
        user_wins += 1
    
    elif user_input == 'SCISSORS' and computer_pick == 'PAPER':
        print('You won!')
        user_wins += 1
    
    elif user_input == computer_pick:
        print('its a Tie!')
    
    else:
        print('You lost!')
        computer_wins += 1

print(f'You won {user_wins} times')
print(f'Computer wins {computer_wins} times')
print('Bye)')
    





    


