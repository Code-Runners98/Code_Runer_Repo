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
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back? <--(cross) (back)--> ')
    if answer == "back":
        print("You go back to the main road. An old man, dying under a stone standing at a crossroads, calls you to come to him.")
        answer = input('You can stab an old man with his own pitchfork or approach him <--(stab) (approach)-->')
        if answer == "stab":
            print("You pierce his stomach and realize that there is emptiness inside, the old man bursts into flames and blows himself up. You died")
        elif answer == "approach":
            print('You approach him, tilt your head to hear what he wants to say. He says you won.')
        else:
            print('Not a valid option! You lose') 
    elif answer == "cross":
        print('')
    else:
        print('Not a valid option! You lose')

else:
    print('Not a valid option! You lose')
