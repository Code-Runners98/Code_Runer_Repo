name = input('Type your name:')
print(f'Welcome {name} to this adventure!')

answer = input("Which way would you like to go? <--(left) or (right)-->  ").lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim accross... <--(swim) or (walk)-->').lower()
    if answer == "swim":
        print("You swam acrross and were eaten by alligator.")
    elif answer == "walk":
        print('You walked for many miles, run out of water. You lose the game...')
    else:
        print('Not a valid option! You lose')

elif answer =='right':
    print('Start')

else:
    print('Not a valid option! You lose')
