
global x, y, t, vx, vy, f
t = 0
x = 0.0
y = 0.0
vx = 0.0
vy = 0.0
tx = 300.0
ty = 0.0
f = False

def setup():
    size(800, 600)
#     fill(200)
#     background(50)
    colorMode(HSB)

    
def draw():
    global x, y, t, f, vx, vy, tx, ty
    fill(0x11000000)
    noStroke()
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)

    noStroke()
    ellipse(x + 10, height - y - 10, 20, 20)
    ellipse(tx + 10, height - ty - 10, 20, 20)

    t = t + 1
    if not f and mousePressed:
        f = True
        vx = (mouseX - x) / 50.0
        vy = ((height - mouseY) - y) / 50.0
    
    if f:
        x = x + vx
        y = y + vy
        vy = vy - 0.1
    else:
        stroke(255)
        line(x + 10, height - y - 10, mouseX, mouseY)
        
    if x < 0 or x > width or y < 0 or y > height:
        f = False
        x = 0
        y = 0
        textSize(50)
        text("YOU FAIL", 320, 240)
        
    if (sqrt((tx-x)*(tx-x)+(ty-y)*(ty-y)) < 20):
        f = False
        x = 0
        y = 0
        textSize(50)
        text("YOU WIN", 320, 240)
        

    
        
    
    

