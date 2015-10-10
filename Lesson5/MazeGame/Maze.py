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
        
        print self.players           
        
    def show(self):
        brickImg = loadImage("Brick32.png");
        okaymanImg = loadImage("Okay32.png");
        trollmanImg = loadImage("Troll32.png");
        chestImg = loadImage("Chest32.gif");
        imgs = {"A":okaymanImg, "B":trollmanImg, "#":brickImg, "*":chestImg}
        
        for y in range(0, self.height):
            cs = self.map[y]
            for x in range(0, self.width):
                s = cs[x]
                if s == " ":
                    noStroke()
                    fill(0, 0, 0)
                    rectMode(CORNERS)
                    rect(x*self.mx, y*self.my, x*self.mx+self.mx, y*self.my+self.my)
                img = imgs.get(s, None)
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
        
        x, y = px, py
        if d == 0:
            x = x - 1
        if d == 1:
            x = x + 1
        if d == 2:
            y = y - 1
        if d == 3:
            y = y + 1

        s = self.map[y][x]

        if s == " ":
            self.map[py][px] = " "
            self.map[y][x] = player
            
            self.players[player] = [x, y]
                
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

