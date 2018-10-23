def go(dir):
    if uinput == "go".lower() + 'N'.lower() or "go".lower() + 'E'.lower() or "go".lower() + 'S'.lower() or "go".lower() + 'W'.lower():
        dir = uinput.split()[1]
        position[0] += nav['{}x'.format(dir.lower())]
        position[1] += nav['{}x'.format(dir.lower())]

def get():
    uinput = input('what do?\n:')

def parse(eee): #TODO: this makes no sense
    get()
    
