from JUC import *

worker = Juc('Your key :)')

text = input('Text: ').encode()
print(f'Crypted  :  {worker.crypt(text)}')