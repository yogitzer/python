import turtle
import random

class Shape:
    myTurtle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')

    def setPen(self):
        r = random.random()
        g = random.random.r()
        b = random.random()
        self.myTurtle.pencolor((r,g,b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)

        def drawShape(self):
            pass
    
    class Rectangle(Shape) : 
        width, height = [0] * 2
        def __init__(self,x,y):
            Shape.__init__(self)
            self.cx = x
            self.cy = y
            self.width = random.randrange(20,100)
            self.height = random.randrange(20, 100)

        def drawShape(self):
            sx1, sy1, sx2, sy2 = [0] * 4