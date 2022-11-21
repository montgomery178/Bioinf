import turtle as tl
import math

def draw_square(size):
    for i in range(4):
        tl.forward(size)
        tl.right(90)
        
def draw_fractal(size):
    if size>5:
        tl.pensize(max(size / 120, 1))
        draw_square(size)
        tl.forward(size/7)
        tl.right(math.degrees(math.atan(1/6)))
        size=((6/7*size)**2+(1/7*size)**2)**0.5
        draw_fractal(size)
    
size = 600

tl.delay(1)  
tl.penup() 
tl.color('red')
tl.goto(-size/2, -size/2) 
tl.setheading(90) 
tl.pendown() 

draw_fractal(size)
tl.done()
