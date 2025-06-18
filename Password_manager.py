from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

master_pwd = input('What is the master password? ').lower()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print(f'User: {user}, Password: {fer.decrypt(passw.encode()).decode()}')


def create():
    name = input('Account name: ')
    pwd = input('Password: ') 

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {fer.encrypt(pwd.encode()).decode()}' + '\n')


while True:
    mode = int(input('1.Create a new password / 2.View existing ones / 3.To quit '))

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
