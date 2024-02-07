import random
from string import ascii_letters, digits
import message

def getID():
    s = ascii_letters + digits
    ID = ""
    for i in range(20):
        rand_char = s[random.randint(0, len(s)-1)]
        ID += rand_char

    return ID


def inpval(isInt=False, promt="->"):
    while True:
        i = input(promt)
        if i.strip() == "":
            message.red("Please enter something")
            continue
        else:
            if isInt:
                try:
                    i = int(i)
                except ValueError:
                    message.red("Invalid input x_x")
                    continue

            break
    return i
