import random
from accessify import private, protected

pwd = input('What is the master password? ').lower()

mode = int(input('1.Create a new password / 2.View existing ones / 3.To quit '))

def view():
    pass

def create():
    pass

while True:
    if mode == 3:
        print('Quit from program')
        quit()
    if mode == 2:
        print('Work')
        pass
    elif mode == 1:
        pass
    else:
        print('Incorrect value for mode, use numbers to pick the mode')
        continue
