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
    "################################"],
    Traveller(1, 1))
    
    size(maze.width*mx, maze.height*my)
    frameRate(30)
    background(20)
    maze.show()
    solveMaze()
             
def solveMaze():
    maze.goRight()
                                  
def draw():
    pass
         
def delay(ms):
    time = millis()
    while (millis() - time <= ms):
        pass

class Maze(object):
    def __init__(self, map, tr):
        self.map = []
        self.height = len(map)
        self.width = 0
        for y in range(0, self.height):
            s = map[y]
            self.width = max(self.width, len(s))
            ls = list(s)
            self.map.append(ls)
        self.tr = tr
        self.map[self.tr.y][self.tr.x] = "."
        
    def show(self):
        for y in range(0, self.height):
            cs = self.map[y]
            for x in range(0, self.width):
                s = cs[x]
                if s == " ":
                    noStroke()
                    fill(0, 0, 0)
                    rectMode(CORNERS)
                    rect(x*mx, y*my, x*mx+mx, y*my+my)
                if s == ".":
                    noStroke()
                    fill(0, 128, 0)
                    rectMode(CORNERS)
                    rect(x*mx, y*my, x*mx+mx, y*my+my)
                if s == "#":
                    noStroke()
                    fill(255, 255, 255)
                    rectMode(CORNERS)
                    rect(x*mx, y*my, x*mx+mx, y*my+my)
                if s == "*":
                    noStroke()
                    fill(255, 0, 255)
                    triangle(x*mx, y*my, x*mx+mx, y*my, x*mx+mx/2, y*my+my)
        self.tr.show()
        
    def goLeft(self):
        return self.go(self.tr.x - 1, self.tr.y)

    def goRight(self):
        return self.go(self.tr.x + 1, self.tr.y)

    def goUp(self):
        return self.go(self.tr.x, self.tr.y - 1)

    def goDown(self):
        return self.go(self.tr.x, self.tr.y + 1)
    
    def go(self, x, y):
        if self.map[y][x] != "#":
            self.tr.x = x
            self.tr.y = y
            self.map[self.tr.y][self.tr.x] = "."
            self.show()
            return True
        return False

class Traveller(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        noStroke()
        fill(0, 255, 0)
        ellipseMode(CORNERS)
        ellipse(self.x*mx, self.y*my, self.x*mx+mx, self.y*my+my)

