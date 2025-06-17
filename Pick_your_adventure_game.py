name = input('Type your name:')
print(f'Welcome {name} to this adventure!')

answer = input("Which way would you like to go? <--(left) or (right)-->  ").lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim across... <--(swim) or (walk)-->').lower()
    if answer == "swim":
        print("You swam across and were eaten by alligator.")
    elif answer == "walk":
        print('You walked for many miles, run out of water. You lose the game...')
    else:
        print('Not a valid option! You lose')

elif answer =='right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back? <--(cross) (back)--> ').lower()
    if answer == "back":
        print("You go back to the main road. An old man, dying under a stone standing at a crossroads, calls you to come to him.")
        answer = input('You can stab an old man with his own pitchfork or approach him <--(stab) (approach)-->').lower()
        if answer == "stab":
            print("You pierce his stomach and realize that there is emptiness inside, the old man bursts into flames and blows himself up. You died")
        elif answer == "approach":
            print('You approach him, tilt your head to hear what he wants to say. He says you won.')
        else:
            print('Not a valid option! You lose') 
    elif answer == "cross":
        print('You are walking on an old bridge, it wobbles and creaks, but it does its job well.\nYou are almost across the bridge, but a troll appears on the other side of the bridge.')
        answer = input('You can shout a battle cry and start fighting the troll with your fists or you can talk to him. <--(fight) (talk)--> ').lower()
        if answer == "fight":
            print("You start hitting the troll with your bare hands, the troll is tickled, he starts laughing, but you hit him in the eye.\nThe troll quickly got angry, took out his club and knocked your head off.\nYou died.")
        elif answer == "talk":
            print('You approach the troll, greet him, the troll nods back at you. While drinking tea, you talk for hours about the main goals of the philosophy of the Kassite monks.\nThen you make a bad joke about the trolls family members and he bites your ass off.\nYou died.')
        else:
            print('Not a valid option! You lose') 
    else:
        print('Not a valid option! You lose')

else:
    print('Not a valid option! You lose')

print(f'Thank you for try, {name}')
