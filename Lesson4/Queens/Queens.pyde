
def setup():
    global n, w, r, s
    n = 8
    w = 40
    s = 0
    r = []
    size(n * w + 1, n * w + 1)
    noLoop()

    def solve(i, a):
        if i < n:
            for j in range(0, n):
                a[i] = j
                if check(i, a):
                    solve(i+1, a)
        if i == n:
            r.append(a[:])
        
    def check(i, a):
        for j in range(0, i):
            k = i - j
            if a[i] == a[j] or a[i] == a[j] - k or a[i] == a[j] + k:
                return False
        return True
    
    solve(0, [0] * n)
    
def draw():
    pass
    
def mousePressed():
    global n, w, r, s
    background(0)
    def drawboard():
        stroke(255)
        for i in range(n):
            for j in range(n):
                fill(((i+j)%2)*100+100)
                rect(i * w, j * w, w, w)
    def drawsolve():
        stroke(255)
        for i in range(n):
            fill(0)
            j = r[s][i]
            ellipse((i + 0.5) * w, (j + 0.5) * w, w * 0.8, w * 0.8)
    
    drawboard()
    if len(r)>0:
        drawsolve();
        s = (s + 1) % len(r)
    redraw()
    

