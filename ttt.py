import turtle
t = turtle.Turtle()
t.shape("classic")
t.pencolor("black")
t.penup()
t.goto(-150,-50)
t.pendown()
t.forward(300)
t.penup()
t.goto(-150,50)
t.pendown()
t.forward(300)
t.penup()
t.goto(-50,150)
t.pendown()
t.right(90)
t.forward(300)
t.penup()
t.goto(50,150)
t.pendown()
t.forward(300)
t.setheading(0)

def goto():
    place = int(input("Which place do you want to play?(1-9)"))
    if place ==1:
        t.penup()
        t.goto(-130,100)
        t.pendown()
    elif place ==2:
        t.penup()
        t.goto(-25,100)
        t.pendown()
    elif place ==3:
        t.penup()
        t.goto(75,100)
        t.pendown()
    elif place ==4:
        t.penup()
        t.goto(-130,0)
        t.pendown()
    elif place ==5:
        t.penup()
        t.goto(-25,0)
        t.pendown()
    elif place ==6:
        t.penup()
        t.goto(75,0)
        t.pendown()

    elif place ==7:
        t.penup()
        t.goto(-130,-100)
        t.pendown()
    elif place ==8:
        t.penup()
        t.goto(-25,-100)
        t.pendown()
    elif place ==9:
        t.penup()
        t.goto(75,-100)
        t.pendown()
    else:
        goto()

def cross():
        
    t.pendown()
    t.setheading(0)
    t.right(45)
    t.forward(20)
    t.backward(40)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.backward(40)
    t.forward(20)
    t.right(90)
    t.penup()

def cir():
    t.setheading(0)
    t.pendown()
    t.circle(25)
    t.penup()


#main code
turn = 1
while turn <= 9:
    if turn %2!=0:
        goto()
        cir()
    else:
        goto()
        cross()
    turn+=1
