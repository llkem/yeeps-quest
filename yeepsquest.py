import random
from parse import *
#made by Ryan

#variables
position = [0,0]
currentroom
rooms = {'plains':[0,0],'woods1':[1,0],'shed':[0,1],'creek':[1,1],'dungeonentr':[0,2]}
mode = 0
hp = 4
valids = [[0,0],[1,0],[0,1],[1,1],[0,2]]
inventory = []
nav = {'nx':0,'ny':1,'ex':1,'ey':0,'sx':0,'sy':-1,'wx':-1,'wy':0}
items = {'note'}
sheditems = {'sword', 'key'}
descriptions = {'plains':"""you stand in the middle of windy plains.\n
To the north you see a rusty shed, and to the east you see woods.
\n at your feet you see a note.""",
                'woods1':
                
                
#commands
def uproom(): #TODO this
    curre

#TODO: take, attack, use
#TODO: hangman? other modes? how do you win?
    
    
#main loop
def main():
    print("Welcome to yeep\'s quest! you are yeep, a lone adventurer with flowing golden hair.\n"
    while mode == 0 or mode == 1:
        parse()
        get()
        take()
        go()
    if mode == 2:
          print('GAME OVER\n')
          if input('play again? [Y/N}:').lower() == 'y':
              #TODO: this
    elif mode == 3:
          print('YOU WIN!')
          break
          
return 0
main()
