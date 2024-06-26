from turtle import*

speed(999999999999999999)
width(7)
color("yellow")
forward(250) 
left(90)

forward(300)
left(90)

forward(250)
left(90)

forward(300)
left(90)

forward(100)
color("purple")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(0, 300)
pendown()
color("green")
begin_fill()
left(140)
forward(210)
right(105)
forward(200)
end_fill()
color("red")
penup()
goto(100, 180)
pendown()
begin_fill()
left(55.2)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()

penup()
goto(-600,450)
pendown()
color("blue")
begin_fill()
right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)
end_fill()










exitonclick()