def setup():
    size(400, 400)
    background(255) 
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    noFill()
    fill(0) # Fill in with black color
    triangle(30, 60, 60, 30, 90, 60) # Draw triagnle
    ellipse(30, 60, 30, 20) # Draw ellipses
    ellipse(90, 60, 30, 20)
    pop()

def draw():
    for x in range (0, 381,20):
        drawObject (x, 0, .2)
        for y in range (0, 381,20):
            drawObject (x, y, .2)
