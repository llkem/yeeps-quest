import random
#made by Ryan

#variables
position = [0,0]
rooms = {'plains':[0,0],'woods1':[1,0],'shed':[0,1],'creek':[1,1],'dungeonentr':[0,2]}
mode = 0
hp = 4
valids = [[0,0],[1,0],[0,1],[1,1],[0,2]]
inventory = []
nav = {'nx':0,'ny':1,'ex':1,'ey':0,'sx':0,'sy':-1,'wx':-1,'wy':0}

#commands
def go(dir):
    if uinput == "go".lower() + 'N'.lower() or "go".lower() + 'E'.lower() or "go".lower() + 'S'.lower() or "go".lower() + 'W'.lower():
        dir = uinput.split()[1]
        position[0] += nav['{}x'.format(dir.lower())]
        position[1] += nav['{}x'.format(dir.lower())]
def get():
    uinput = input('what do?\n:')
#TODO: take, attack, use
#TODO: hangman? other modes? how do you win?
    
#parse
def parse(eee): #TODO: this makes no sense
    get()
    
#main loop
def main():
    print("Welcome to yeep\'s quest! you are yeep, a lone adventurer with flowing golden hair.\n"
    if mode == 0 or mode == 1:
        parse()
    elif mode == 2:
          print('GAME OVER\n')
          if input('play again? [Y/N}:').lower() == 'y':
              #TODO: this
    elif mode == 3:
          print('YOU WIN!')
          break
          
return 0
