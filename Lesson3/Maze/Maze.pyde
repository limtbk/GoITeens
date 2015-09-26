def setup():
    global maze, mx, my, tr
    mx = 20
    my = 20
    maze = Maze([
    "################################",
    "#    #   #       #          #  #",
    "#### # # # ##### # ### #### #  #",
    "#      #   #     # # # #    # ##",
    "## ########### ### ### ######  #",
    "#  #        #          #    ## #",
    "# ## ###### ######## #    #    #",
    "#  #  #   # #   #  # ###########",
    "## #### # # # #    # #         #",
    "#  #    # ### # #### # # ##### #",
    "# ## ####   # #      # # #   # #",
    "# #     # # # ######## # ##### #",
    "# # ##  # # #    #   # #       #",
    "# # #  ## # #### # # # # #######",
    "#   #  #  #    #   #   #      *#",
    "################################"])
    tr = Traveller(1, 1, maze)
    size(maze.width*mx, maze.height*my)
    frameRate(30)
    background(20)
    maze.show()
    tr.show()
                    
def draw():
    pass
         
def delay(ms):
    time = millis()
    while (millis() - time <= ms):
        pass

class Maze(object):
    def __init__(self, map):
        self.map = map
        self.height = len(map)
        self.width = len(map[0])
        
    def show(self):
        for y in range(0, self.height):
            cs = self.map[y]
            for x in range(0, self.width):
                s = cs[x]
                if s == "#":
                    noStroke()
                    fill(255, 255, 255)
                    rectMode(CORNERS)
                    rect(x*mx, y*my, x*mx+mx, y*my+my)
                if s == "*":
                    noStroke()
                    fill(255, 0, 255)
                    triangle(x*mx, y*my, x*mx+mx, y*my, x*mx+mx/2, y*my+my)

class Traveller(object):
    def __init__(self, x, y, maze):
        self.x = x
        self.y = y
        self.maze = maze
        
    def show(self):
        noStroke()
        fill(0, 255, 0)
        ellipseMode(CORNERS)
        ellipse(self.x*mx, self.y*my, self.x*mx+mx, self.y*my+my)

