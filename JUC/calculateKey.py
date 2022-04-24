import base64

def calculate(key):
    return sum([ord(char) for char in key])

def getCString(text):
    values = base64.b64decode(text).decode().split('.')
    return values[0], int(values[-1])