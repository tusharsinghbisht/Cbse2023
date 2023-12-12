import random
from string import ascii_letters, digits

def getID():
    s = ascii_letters + digits
    ID = ""
    for i in range(20):
        rand_char = s[random.randint(0, len(s)-1)]
        ID += rand_char

    return ID