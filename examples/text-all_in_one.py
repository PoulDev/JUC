from JUC import *

worker = Juc('Your key :)')

action = '...'

while not (len(action) >= 1 and action[0] in ('c', 'd')):
    action = input('[C]crypt or [D]decrypt ?:').lower()
text = input('text: ')

if action[0] == 'c':
    print(f'Crypted: {worker.crypt(text.encode())}')
else:
    print(f'Decrypted: {worker.decrypt(text).decode()}')