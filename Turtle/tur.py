import turtle
pen_1 = turtle.Turtle()
pen_1.color("black")
pen_1.penup()
pen_1.goto(-200,45)

#J
pen_1.pendown()
pen_1.right(-45)
pen_1.forward (30)
pen_1.right(135)
pen_1.forward (55)
pen_1.circle(-20,115)

#O
pen_1.penup()
pen_1.goto(-150,-10)
pen_1.pendown()
pen_1.right(-180)
pen_1.circle(25,360)
pen_1.penup()

#S
pen_1.goto(-100,-10)
pen_1.right(-25)
pen_1.pendown()
pen_1.forward (17)
pen_1.circle(12,180)
pen_1.forward (5)
pen_1.right(180)
pen_1.circle(12,-180)
pen_1.forward (-17)

#H
pen_1.penup()
pen_1.goto(-50,-10)
pen_1.right(90)
pen_1.pendown()
pen_1.forward (80)
pen_1.forward (-60)
pen_1.circle(-20,180)
pen_1.forward (20)

#U
pen_1.penup()
pen_1.goto(10,25)
pen_1.pendown()
pen_1.forward (15)
pen_1.circle(20,180)
pen_1.forward (15)

#A
pen_1.penup()
pen_1.right(-90)
pen_1.goto(100,-10)
pen_1.pendown()
pen_1.forward (15)
pen_1.circle(-15,180)
pen_1.forward (15)
pen_1.right(90)
pen_1.forward (30)
pen_1.forward (-30)
pen_1.right (180)
pen_1.circle(15,95)
pen_1.forward (9)

turtle.exitonclick()