name = input('Type your name:')
print(f'Welcome {name} to this adventure!')

answer = input("Which way would you like to go? <--(left) or (right)-->  ").lower()

if answer == 'left':
    answ2 = input('You come to a river, you can walk around it or swim accross... <--(swim) or (walk)-->').lower()

elif answer =='right':
    print('')
else:
    print('Not a valid option! You lose')
