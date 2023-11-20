import random, string

def generateRandomVariable(length=6):
    return ''.join(random.choice([*string.ascii_lowercase, '_']) for i in range(length))
