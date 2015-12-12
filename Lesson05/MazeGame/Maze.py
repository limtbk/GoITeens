import time

class Maze(object):
    def __init__(self, map, mx, my):
        self.map = []
        self.width = 0
        self.mx = mx
        self.my = my
        for y in range(0, len(map)):
            s = map[y]
            self.width = max(self.width, len(s))
            ls = list(s)
            if len(ls)>0:
                self.map.append(ls)
        self.height = len(self.map)
        self.players = {}
        for y in range(0, self.height):
            cs = self.map[y]
            for x in range(0, self.width):
                s = cs[x]
                if 'A'<=s and s<='Z':
                    self.players[s] = [x, y]
        self.imgDict = {"#":loadImage("Brick32.png"), "*":loadImage("Chest32.gif")}
        self.plImgDict = {"A":loadImage("Okay32.png"), "B":loadImage("Troll32.png")}
        
        print self.players           
        
    def show(self):
        
        for y in range(0, self.height):
            cs = self.map[y]
            for x in range(0, self.width):
                s = cs[x]
                if s != "#":
                    noStroke()
                    fill(0, 0, 0)
                    rectMode(CORNERS)
                    rect(x*self.mx, y*self.my, x*self.mx+self.mx, y*self.my+self.my)
                img = self.imgDict.get(s, None)
                if img:
                    image(img, x*self.mx, y*self.my, self.mx, self.my)
            for playerName, coord in self.players.iteritems():
                x, y = coord
                img = self.plImgDict.get(playerName, None)
                if img:
                    image(img, x*self.mx, y*self.my, self.mx, self.my)
                    
    def goLeft(self, player):
        return self.go(player, 0)

    def goRight(self, player):
        return self.go(player, 1)

    def goUp(self, player):
        return self.go(player, 2)

    def goDown(self, player):
        return self.go(player, 3)
    
    def go(self, player, d):
        px, py = self.players[player]
        
        dx, dy = 0, 0
        if d == 0:
            dx = -1
        if d == 1:
            dx = 1
        if d == 2:
            dy = -1
        if d == 3:
            dy = 1

        s = self.map[int(py + dy)][int(px + dx)]
        if s == " ":
            for i in range(100):
                self.players[player] = [px + (dx / 100.0) * i, py + (dy / 100.0) * i]
                time.sleep(0.001)
            self.players[player] = [px + dx, py + dy]

            self.map[py][px] = " "
            self.map[int(py + dy)][int(px + dx)] = player
                
#         if player == "A":
#             if s == "*":
#                 textSize(50)
#                 text("OkayMan WIN", 200, 300)
#                 time.sleep(10)
#         
#         if player == "B":
#             if s == "A":
#                 textSize(50)
#                 text("TrollMan WIN", 200, 300)
#                 time.sleep(10)

            return True
        return False    

