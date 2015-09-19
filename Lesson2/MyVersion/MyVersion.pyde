
def setup():
    global gobjects, dt, mp
    size(800, 600)
    frameRate(30)
    background(50)
    colorMode(HSB)
    dt = 1.0
    gobjects = []
    mp = False
    gobjects.append(Square(64, 100.0, 100.0, 1.0, 1.5, 0.0, 0.1, 1.0, 20.0))
    gobjects.append(Ellipse(100, 120.0, 120.0, 0.5, 1.5, 0.0, 0.03, 1.0, 10.0, 20.0))
    gobjects.append(PhysicObject(128, 0.0, 0.0, 1.1, 1.5, 0.0, 0.0, 1.0))
    
def draw():
    global mp
    fill(0x11000000)
    noStroke()
    rectMode(CORNERS)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    
    stroke(255)
    line(0, height, mouseX, mouseY)

    if mousePressed:
        if not mp: # Prevent creating more than 1 object on mouse press
            mp = True
            gobjects.append(Circle(frameCount % 255, 0.0, 0.0, (mouseX) / 50.0, (height - mouseY) / 50.0, 0.0, 0.0, 1.0, 10.0))
    else:
        mp = False        
    
    # Recalculate and redraw all objects
    for g in gobjects:
        g.display()
    
    for g in gobjects:
        g.update()

    # Collision detection between circles            
    for i in range(len(gobjects)):
        for j in range(i+1, len(gobjects)):
            g1 = gobjects[i]
            g2 = gobjects[j]
            if g1 != g2:
                d = sqrt((g1.x - g2.x) * (g1.x - g2.x) + (g1.y - g2.y) * (g1.y - g2.y))
                if hasattr(g1, 'r') and hasattr(g2, 'r'):
                    if d < g1.r + g2.r:
                        tx = g1.vx
                        g1.vx = g2.vx
                        g2.vx = tx
                        ty = g1.vy
                        g1.vy = g2.vy
                        g2.vy = ty
                        d = sqrt((g1.x - g2.x) * (g1.x - g2.x) + (g1.y - g2.y) * (g1.y - g2.y))
                        g1.display()
                        g2.display()
                        g1.update()
                        g2.update()
                        
class PhysicObject(object):
    def __init__(self, c, x, y, vx, vy, a, va, m):
        self.c = c #color
        self.x = x #coordinates, pixels
        self.y = y
        self.vx = vx #speed vector, pixels per frame
        self.vy = vy
        self.a = a #rotation angle, rad
        self.va = va #rotation speed, rad per frame
        self.m = m #mass
    
    def update(self):
        global dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.a += self.va * dt
        self.vy += -0.1 * dt
        if self.x < 0 or self.x > width:
            self.vx = -self.vx
            self.x += 2 * self.vx
        if self.y < 0 or self.y > height:
            self.vy = -self.vy
            self.y += 2 * self.vy
    
    def display(self):
        with pushMatrix():
            translate(self.x, height - self.y)
            rotate(self.a)
            self.draw()
        
    def draw(self):
        stroke(self.c, 255, 255)
        point(0, 0)
        
class Circle(PhysicObject):
    def __init__(self, c, x, y, vx, vy, a, va, m, r):
        super(Circle, self).__init__(c, x, y, vx, vy, a, va, m)
        self.r = r #radius
    
    def draw(self):
        noStroke()
        fill(self.c, 255, 255)
        ellipseMode(CENTER)
        ellipse(0, 0, 2 * self.r, 2 * self.r)
        
class Square(PhysicObject):
    def __init__(self, c, x, y, vx, vy, a, va, m, l):
        super(Square, self).__init__(c, x, y, vx, vy, a, va, m)
        self.l = l #width and height
    
    def draw(self):
        noStroke()
        fill(self.c, 255, 255)
        rectMode(CENTER)
        rect(0, 0, self.l, self.l)

class Ellipse(PhysicObject):
    def __init__(self, c, x, y, vx, vy, a, va, m, rx, ry):
        super(Ellipse, self).__init__(c, x, y, vx, vy, a, va, m)
        self.rx = rx #radius
        self.ry = ry
    
    def draw(self):
        noStroke()
        fill(self.c, 255, 255)
        ellipseMode(CENTER)
        ellipse(0, 0, 2 * self.rx, 2 * self.ry)
        
class Rect(PhysicObject):
    def __init__(self, c, x, y, vx, vy, a, va, m, w, h):
        super(Rect, self).__init__(c, x, y, vx, vy, a, va, m)
        self.w = w #width and height
        self.h = h #width and height
    
    def draw(self):
        noStroke()
        fill(self.c, 255, 255)
        rectMode(CENTER)
        rect(0, 0, self.w, self.h)

        

        
    
    

