import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# List of colors for hearts
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

# Function to draw a heart
def draw_heart(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Draw colorful hearts
for _ in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    color = random.choice(colors)
    draw_heart(x, y, color)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is closed manually
screen.mainloop()
