class Traveller(object):
    def __init__(self, x, y, mx, my):
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
        
    def show(self):
        noStroke()
        fill(0, 255, 0)
        ellipseMode(CORNERS)
        ellipse(self.x*self.mx, self.y*self.my, self.x*self.mx+self.mx, self.y*self.my+self.my)

