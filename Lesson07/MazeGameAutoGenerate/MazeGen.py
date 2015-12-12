from random import randint


def getmazedimensions(maze):
    wx = len(maze)
    wy = len(maze[0])
    for x in range(1, wx):
        wy = min(wy, len(maze[x]))
    return wx, wy


def printmaze(maze):
    wx, wy = getmazedimensions(maze)
    for y in range(wy):
        a = []
        for x in range(wx):
            s = maze[x][y]
            a.append(s)
        print "".join(a)


def strmaze(maze):
    wx, wy = getmazedimensions(maze)
    st = []
    for y in range(wy):
        a = []
        for x in range(wx):
            s = maze[x][y]
            a.append(s)
        st.append("".join(a))
    return st


def fillmaze(maze):
    wx, wy = getmazedimensions(maze)
    ch = True
    while ch:
        ch = False
        for x in range(1, wx - 1):
            for y in range(1, wy - 1):
                mchr = maze[x][y]
                if mchr != "#" and mchr != " ":
                    if maze[x - 1][y] == " ":
                        maze[x - 1][y] = mchr
                        ch = True
                    if maze[x + 1][y] == " ":
                        maze[x + 1][y] = mchr
                        ch = True
                    if maze[x][y - 1] == " ":
                        maze[x][y - 1] = mchr
                        ch = True
                    if maze[x][y + 1] == " ":
                        maze[x][y + 1] = mchr
                        ch = True


def cleanmaze(maze):
    wx, wy = getmazedimensions(maze)
    for x in range(wx):
        for y in range(wy):
            mchr = maze[x][y]
            if mchr != "#" and mchr != " ":
                maze[x][y] = " "


def framemaze(maze):
    wx, wy = getmazedimensions(maze)
    for x in range(wx):
        maze[x][0] = "#"
        maze[x][wy - 1] = "#"
    for y in range(wy):
        maze[0][y] = "#"
        maze[wx - 1][y] = "#"


def fillmazecorners(maze):
    wx, wy = getmazedimensions(maze)
    for x in range(2, wx - 1, 2):
        for y in range(2, wy - 1, 2):
            c = (maze[x][y - 1] == "#") + (maze[x][y + 1] == "#") + (maze[x - 1][y] == "#") + (maze[x + 1][y] == "#")
            if c > 1:
                maze[x][y] = "#"


def randomfillmaze(maze, km, k):
    wx, wy = getmazedimensions(maze)
    for x in range(1, wx - 1, 2):
        for y in range(2, wy - 1, 2):
            r = randint(0, km)
            if r >= k:
                maze[x][y] = "#"
    for y in range(1, wy - 1, 2):
        for x in range(2, wx - 1, 2):
            r = randint(0, km)
            if r >= k:
                maze[x][y] = "#"


def checkmazereachability(maze, reachpoints):
    wx, wy = getmazedimensions(maze)
    xs, ys = reachpoints[0]
    maze[xs][ys] = "."
    fillmaze(maze)
    reach = False
    for i in range(1, len(reachpoints)):
        xi, yi = reachpoints[i]
        reach = reach or (maze[xi][yi] != ".")
    return reach


def checkaddnewmazepath(maze, rx, ry):
    newpath = ("." == maze[rx - 1][ry] and " " == maze[rx + 1][ry]) or\
              (" " == maze[rx - 1][ry] and "." == maze[rx + 1][ry]) or\
              ("." == maze[rx][ry - 1] and " " == maze[rx][ry + 1]) or\
              (" " == maze[rx][ry - 1] and "." == maze[rx][ry + 1])
    return newpath


def addmazereachability(maze, reachpoints):
    wx, wy = getmazedimensions(maze)
    nrd = checkmazereachability(maze, reachpoints)
    while nrd:
        rx = randint(1, wx - 2)
        ry = randint(1, wy - 2)
        if checkaddnewmazepath(maze, rx, ry):
            maze[rx][ry] = "."
            fillmaze(maze)
        nrd = checkmazereachability(maze, reachpoints)


def genmaze(wx, wy, km, k, reachpoints):
    maze = [[" "] * wy for i in range(wx)]
    framemaze(maze)
    randomfillmaze(maze, km, k)
    fillmazecorners(maze)
    addmazereachability(maze, reachpoints)
    cleanmaze(maze)
    ax, ay = reachpoints[0]
    bx, by = reachpoints[3]
    cx, cy = reachpoints[1]
    maze[ax][ay] = "A"
    maze[bx][by] = "B"
    maze[cx][cy] = "*"
    return strmaze(maze)

