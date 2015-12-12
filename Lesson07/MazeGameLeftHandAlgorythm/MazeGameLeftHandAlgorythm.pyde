
import thread
import time
from Maze import Maze
from random import randint

def setup():
    global maze, lastkey, gameon, dira, dirb, success
    dira = 0 # init direction - right
    dirb = 0 # init direction - right
    success = False
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
        if maze.win == ' ':
            movea()
        time.sleep(0.001)
    
def playerb_function():
    while lastkey != 'q':
        if maze.win == ' ':
            moveb()
        time.sleep(0.001)
        
def keyPressed():
    global lastkey
    lastkey = key

def dirleft(dir):
    return (dir+3) % 4

def dirright(dir):
    return (dir+1) % 4

def dirback(dir):
    return (dir+2) % 4

def dirnexta(dir):
    return dirright(dir)

def dirnextb(dir):
    return dirleft(dir)

def lookaround(player, dir, dirnextf):
    forward = maze.look(player, dir) != "#"
    oneside = maze.look(player, dirnextf(dir)) != "#"
    back = maze.look(player, dirnextf(dirnextf(dir))) != "#"
    otherside = maze.look(player, dirnextf(dirnextf(dirnextf(dir)))) != "#"
    return forward, oneside, back, otherside

def movea():
    global dira
    lforw, lside, lback, losid = lookaround("A", dira, dirnexta)

    if lforw:
        if lside:
            dira = dirnexta(dira) #go to one side
        else:
            dira = dira # just go the same direction
    elif lside:
        dira = dirnexta(dira) #go to one side
    elif losid:
        dira = dirnexta(dirnexta(dirnexta(dira))) # go to other side
    else:
        dira = dirnexta(dirnexta(dira)) # go back
    success = maze.go("A", dira)
    
def moveb():
    global dirb

    lforw, lside, lback, losid = lookaround("B", dirb, dirnextb)

    if lforw:
        if lside:
            dirb = dirnextb(dirb) #go to one side
        else:
            dirb = dirb # just go the same direction
    elif lside:
        dirb = dirnextb(dirb) #go to one side
    elif losid:
        dirb = dirnextb(dirnextb(dirnextb(dirb))) # go to other side
    else:
        dirb = dirnextb(dirnextb(dirb)) # go back
    success = maze.go("B", dirb)

