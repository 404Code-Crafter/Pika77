import turtle
t = turtle.Turtle()
t.pencolor("#718ce3")

screen = turtle.Screen( )
screen.bgcolor('#42f5c8')

t.speed(1)
t.pensize(6)

for _ in range(5):
    t.forward(100)
    t.right(144)
turtle.done()