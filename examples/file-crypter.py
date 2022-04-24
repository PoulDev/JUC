from JUC import *

worker = Juc('Your key :)')

filePath = input('File path: ')
fileType = filePath.split('.')[-1]

with open(f'result-crypted.{fileType}', 'wb') as f:
    with open(filePath, 'rb') as file:
        content = file.read()
        crypted = worker.crypt(content)
        f.write(crypted.encode())