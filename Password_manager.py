master_pwd = input('What is the master password? ').lower()

mode = int(input('1.Create a new password / 2.View existing ones / 3.To quit '))

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print(f'User: {user}, Password: {passw}')


def create():
    name = input('Account name: ')
    pwd = input('Password: ') 

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {pwd}' + '\n')


while True:
    if mode == 3:
        print('Quit from program')
        quit()
    if mode == 2:
        view()
        break
    elif mode == 1:
        create()
    else:
        print('Incorrect value for mode, use numbers to pick the mode')
        continue
