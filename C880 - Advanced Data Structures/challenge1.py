import turtle

# Create Marty the turtle
marty = turtle.Turtle()

# Function for Marty to draw a circle and move to the right
def draw_circle_and_move_right():
    marty.circle(50)  # Draw a circle with a radius of 50
    marty.penup()     # Lift the pen so Marty doesn't draw a line while moving
    marty.setheading(0)  # Point Marty to the right
    marty.forward(100)   # Move Marty 100 units to the right
    marty.pendown()  # Put the pen back down to start drawing again

# Example: Make Marty draw a circle and move right 5 times
for _ in range(5):
    draw_circle_and_move_right()

# Keep the window open until clicked
turtle.done()
