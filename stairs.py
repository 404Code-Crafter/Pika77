import turtle 
t = turtle.Turtle()
t.shape('circle')
t.shapesize(0.79)
t.pencolor('white')
Screen = turtle.Screen()
Screen.bgcolor('Orange')

t.speed(2)
t.pensize(6)
t.penup()

t.penup()
t.goto(-500, -300)
t.pendown()

for _ in range(7):
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(90)

t.penup()
t.goto(0, 0)

turtle.done()
