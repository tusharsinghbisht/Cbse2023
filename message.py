from animation import animate

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
PINK = '\033[95m'
CYAN = '\033[96m'


def blue(s):
    animate(BLUE+s+ENDC) 
    
def cyan(s):
    animate(CYAN+s+ENDC) 

def green(s):
    animate(GREEN+s+ENDC)

def yellow(s):
    animate(YELLOW+s+ENDC)


def red(s):
    animate(RED+s+ENDC)

def bold(s):
    animate(BOLD+s+ENDC)


def pink(s):
    animate(PINK+s+ENDC)

def color(s, col, anm=True):
    COL = ""
    if col == "blue":
        COL=BLUE
    elif col == "cyan":
        COL=CYAN
    elif col == "green":
        COL=GREEN
    elif col == "yellow":
        COL=YELLOW
    elif col == "red":
        COL=RED
    elif col == "pink":
        COL=PINK
    else:
        if anm:
            animate(s)
        else:
            print(s)
        return None

    if anm:
        animate(COL+s+ENDC)
    else:
        print(COL+s+ENDC)