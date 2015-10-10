import thread
import time
from Maze import Maze
from random import randint

def setup():
    global maze
    mx = 32
    my = 32
    mazearr = []
    mazefile = open("maze.txt")
    mazestring = mazefile.read()
    mazearr = mazestring.split("\n")
    maze = Maze(mazearr, mx, my)
    size(maze.width*mx, maze.height*my)
    background(20)
    thread.start_new_thread(playera_function, ())
    thread.start_new_thread(playerb_function, ())
    
def draw():
    maze.show()

def playera_function():
    while maze:
        movea()
        time.sleep(0.001)

def playerb_function():
    while maze:
        moveb()
        time.sleep(0.001)

def movea():
    r = randint(0,4)
    if r == 0:
        maze.goLeft("A")
    if r == 1:
        maze.goRight("A")
    if r == 2:
        maze.goUp("A")
    if r == 3:
        maze.goDown("A")

def moveb():
    r = randint(0,4)
    if r == 0:
        maze.goLeft("B")
    if r == 1:
        maze.goRight("B")
    if r == 2:
        maze.goUp("B")
    if r == 3:
        maze.goDown("B")

