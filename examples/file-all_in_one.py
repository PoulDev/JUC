from JUC import *

worker = Juc('Your key :)')

action = '...'

while not (len(action) >= 1 and action[0] in ('c', 'd')):
    action = input('[C]crypt or [D]decrypt ?:').lower()
filePath = input('File path: ')
fileType = filePath.split('.')[-1]

if action[0] == 'c':
    with open(f'result-crypted.{fileType}', 'wb') as f:
        with open(filePath, 'rb') as file:
            content = file.read()
            crypted = worker.crypt(content)
            f.write(crypted.encode())
else:
    with open(filePath, 'r') as file:
        content = file.read()
        with open(f'result-decrypted.{fileType}', 'wb') as f:
            decrypted = worker.decrypt(content, False)
            f.write(decrypted)