#chr
#ord
import base64, time
from .calculateKey import *
from .exceptions import *

class Juc:
    def __init__(self, key):
        if key == '':
            raise InvalidKey('Cannot use an empty key')
        self.key = key
        self.keyCode = calculate(key)

    def crypt(self, text) -> str:
        now = int(time.time() * 1000000)
        return base64.b64encode((''.join(
            str(hex(ord(code) * int(now / self.keyCode))) for code \
                in text
        ) + f'.{now}').encode()).decode()

    def decrypt(self, text) -> str:
        string, now = getCString(text)
        return ''.join(
            chr(int(hexValue, 16) // int(now / self.keyCode)) for hexValue \
                in string.split('0x')[1:]
        )
