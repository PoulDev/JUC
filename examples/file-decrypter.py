from JUC import *

worker = Juc('Your key :)')

filePath = input('File path: ')
fileType = filePath.split('.')[-1]

with open(filePath, 'r') as file:
    content = file.read()
    with open(f'result-decrypted.{fileType}', 'wb') as f:
        decrypted = worker.decrypt(content, False)
        f.write(decrypted)