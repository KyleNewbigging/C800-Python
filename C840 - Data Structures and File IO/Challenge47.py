import turtle

def drawShape(shape,size,colour):
    window = turtle.Screen()
    marty = turtle.Turtle()
    
    marty.pencolor(colour)
    marty.fillcolor(colour)
    marty.begin_fill()
    if(shape==1):
        print("Printing Square..")
        marty.forward(size)
        marty.left(90)
        marty.forward(size)
        marty.left(90)
        marty.forward(size)
        marty.left(90)
        marty.forward(size) 
        marty.left(90)
    elif(shape==3):
        print("Printing Triangle..")
        marty.forward(size)
        marty.left(120)
        marty.forward(size)
        marty.left(120)
        marty.forward(size)
        marty.left(120)
    elif(shape==2):
        print("Printing Circle..")
        marty.circle(size)
    marty.end_fill()

shape = int(input("What shape would you like to draw?\nEnter 1 for Square\nEnter 2 for a Circle\nEnter 3 for a Triangle\n"))

size = int(input("What is the size pf the shape"))

colour = input("What is the colour of the shape?")

drawShape(shape,size,colour)
