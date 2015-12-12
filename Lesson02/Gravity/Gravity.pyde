
def setup():
    global gobjects, dt, mp
    size(800, 600)
    frameRate(30)
    background(50)
    colorMode(HSB)
    dt = 1.0
    gobjects = []

    mp = False
    
def draw():
    global mp
    fill(0x11000000)
    noStroke()
    rectMode(CORNERS)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    
    stroke(255)
    line(200, height-300, mouseX, mouseY)

    if mousePressed:
        if not mp:
            mp = True
            gobjects.append(Circle(frameCount % 255, 200.0, 300.0, (mouseX-200) / 50.0, (height - mouseY-300) / 50.0, 0.0, 0.0, 1.0, 10.0))
    else:
        mp = False        
    
    for g in gobjects:
        g.display()
    
    for gi in gobjects:
        for gj in gobjects:
            if gi != gj:
                d2 = (gi.x-gj.x)*(gi.x-gj.x)+(gi.y-gj.y)*(gi.y-gj.y)
                d = sqrt(d2)
                gi.vx += 5*(gj.x-gi.x)*gi.m*gj.m/d2
                gi.vy += 5*(gj.y-gi.y)*gi.m*gj.m/d2
    
    for g in gobjects:
        g.update()
        
    for i in range(len(gobjects)):
        for j in range(i+1, len(gobjects)):
            g1 = gobjects[i]
            g2 = gobjects[j]
            if g1 != g2:
                d = sqrt((g1.x - g2.x) * (g1.x - g2.x) + (g1.y - g2.y) * (g1.y - g2.y))
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
                    d = sqrt((g1.x - g2.x) * (g1.x - g2.x) + (g1.y - g2.y) * (g1.y - g2.y))
    
    
        
                        
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

