from Myro import *
init ("sim")
def squareDraw():
    squareSize = float(input("Input a number (1= small square, 4 = big square, max = 4 on given field)"))
    #identifying what to input, whether that is a float, string boolean, etc.
    penDown()
    forward(1,squareSize)
    turnBy(90)
    wait(1)
    forward(1,squareSize)
    turnBy(90)
    wait(1)
    forward(1,squareSize)
    turnBy(90)
    wait(1)
    forward(1,squareSize)
squareDraw()