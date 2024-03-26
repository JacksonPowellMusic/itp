def setup():
    size(400, 400)
    noStroke() 
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) # Fill in with black color
    triangle(30, 60, 60, 30, 90, 60) # Draw triagnle
    ellipse(30, 60, 30, 20) # Draw ellipses
    ellipse(90, 60, 30, 20)
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
