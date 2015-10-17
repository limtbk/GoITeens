import thread
import time
from Maze import Maze
from random import randint

def setup():
    global maze, lastkey
    lastkey = ''
    mx = 32
    my = 32
    mazearr = []
    mazefile = open("maze.txt")
    mazestring = mazefile.read()
    mazearr = mazestring.split("\n")
    maze = Maze(mazearr, mx, my)
    size(maze.width*mx, maze.height*my)
    background(20)
    patid = thread.start_new_thread(playera_function, ())
    pbtid = thread.start_new_thread(playerb_function, ())
    
def draw():
    maze.show()
    if lastkey == '\n':
        maze.startGame()
    if lastkey == 'q':
        exit()

def playera_function():
    while lastkey != 'q':
        movea()
        time.sleep(0.001)
    
def playerb_function():
    while lastkey != 'q':
        moveb()
        time.sleep(0.001)
        
def keyPressed():
    global lastkey
    lastkey = key

def movea():
    global lastkey
    try:
        if lastkey == 'w':
            maze.goUp("A")
            lastkey = ''
        if lastkey == 'd':
            maze.goRight("A")
            lastkey = ''
        if lastkey == 'a':
            maze.goLeft("A")
            lastkey = ''
        if lastkey == 's':
            maze.goDown("A")
            lastkey = ''
    except NameError:
        print ""
    
def moveb():
    global lastkey
    try:
        if lastkey == 'i':
            maze.goUp("B")
            lastkey = ''
        if lastkey == 'l':
            maze.goRight("B")
            lastkey = ''
        if lastkey == 'j':
            maze.goLeft("B")
            lastkey = ''
        if lastkey == 'k':
            maze.goDown("B")
            lastkey = ''
    except NameError:
        print ""

