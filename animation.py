import time,sys, random

def animate(txt):
    for i in txt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.randint(1, 10)/100)
    print("")



def loading():
    x = 0.01
    for i in "........":
        sys.stdout.write(i)
        sys.stdout.flush()
        x = x + 0.05
        time.sleep(x)
    print("")

