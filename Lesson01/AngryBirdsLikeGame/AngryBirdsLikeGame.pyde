x = 0.0
y = 0.0
vx = 0.0
vy = 0.0
fl = False
tx = 300
ty = 0

def setup():
    size(600, 600)
    colorMode(HSB)
    noStroke()


def draw():
    global x, y, vx, vy, fl, tx, ty
    fill(0x11000000)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    ellipse(x + 10, height - y - 10, 20, 20)
    fill(frameCount % 255, 255, 255)
    ellipse(tx + 10, height - ty - 10, 20, 20)
    if fl:
        x = x + vx/100.0
        y = y + vy/100.0
        vy = vy - 1
    if (sqrt((x-tx)*(x-tx) + (y - ty)*(y - ty))<=20):
        textSize(50)
        text("YOU WIN", 200, 300)
        x=0
        y=0
        vx=100 
        vy=100
        fl=False
    
    if  x<0 or x>width or y<0 or y>height:
        x=0
        y=0
        vx=100 
        vy=100
        fl=False
        textSize(50)
        text("YOU FAIL", 200, 300)
        
    if mousePressed:
        vx = 100.0
        vy = 100.0
        fl = True
    
    
