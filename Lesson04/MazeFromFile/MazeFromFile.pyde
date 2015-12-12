from Traveller import Traveller
from Maze import Maze

def setup():
    global maze, mx, my, tr
    mx = 15
    my = 15
    mazearr = []
    with open("maze.txt") as f:
        for line in f:
            mazearr.append(line)
            print line
            
    if len(mazearr)>0:
        maze = Maze(mazearr, Traveller(1, 1, mx, my), mx, my)
    else:
        maze = Maze([
        "################################",
        "#    #   #       #          #  #",
        "#### # # # ##### # ### #### #  #",
        "#      #   #     # #   #    # ##",
        "## ########### ### ### ######  #",
        "#  #        #          #    ## #",
        "# ## ### ## ######## #    #    #",
        "#  #  #   # #   #  # ###########",
        "## #### # # # #    # #         #",
        "#  #    # ### # #### # # ## ## #",
        "# ## ####   # #      # # #   # #",
        "# #     # # # ######## # ##### #",
        "# # ##  # # #    #   # #       #",
        "# # #  ## # #### # # # # #######",
        "#   #  #  #        #   #      *#",
        "################################"],
        Traveller(1, 1, mx, my), mx, my)
        
    size(maze.width*mx, maze.height*my)
    background(20)
    maze.show()
    noLoop()
             
def solveMaze():
    if maze.lookDown() != "#" and maze.lookDown() != "." and maze.lookDown() != "," and maze.marksymbol != maze.path:
        maze.goDown()
        solveMaze()
        maze.goUp()
    if maze.lookLeft() != "#" and maze.lookLeft() != "." and maze.lookLeft() != "," and maze.marksymbol != maze.path:
        maze.goLeft()
        solveMaze()
        maze.goRight()
    if maze.lookRight() != "#" and maze.lookRight() != "." and maze.lookRight() != "," and maze.marksymbol != maze.path:
        maze.goRight()
        solveMaze()
        maze.goLeft()
    if maze.lookUp() != "#" and maze.lookUp() != "." and maze.lookUp() != "," and maze.marksymbol != maze.path:
        maze.goUp()
        solveMaze()
        maze.goDown()
                                  
def draw():
    pass
    
def mousePressed():
    solveMaze()
         
def delay(ms):
    time = millis()
    while (millis() - time <= ms):
        pass



