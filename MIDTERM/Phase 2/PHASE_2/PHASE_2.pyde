def setup():
    size(150, 150) # Set the size of canvas
    noStroke() # Disable drawing the stroke

def draw():
    fill(0) # Fill in with black color
    triangle(30, 60, 60, 30, 90, 60) # Draw triagnle
    ellipse(30, 60, 30, 20) # Draw ellipses
    ellipse(90, 60, 30, 20)
