from Myro import *
init ("sim")
def squareDraw():
    #contents of functions are indented
    penDown()
    forward(1,1)
    #I tested penUp and wait() in those locations
    #but it didn't seem to do anything
    #penDown()
    #wait(1)
    turnLeft(2.45,.5)
    turnLeft(2.45,.5)
    #penDown()
    wait(1)
    forward(1,1)
    #wait(1)
    turnLeft(2.45,.5)
    turnLeft(2.45,.5)
    wait(1)
    forward(1,1)
    #wait(1)
    turnLeft(2.45,.5)
    turnLeft(2.45,.5)
    wait(1)
    forward(1,1)


squareDraw()
