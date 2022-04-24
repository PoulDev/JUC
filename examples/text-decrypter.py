from JUC import *

worker = Juc('Your key :)')

text = input('Text: ')
print(f'Derypted  :  {worker.decrypt(text).decode()}')