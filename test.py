import turtle
win = turtle.Screen()
win.setup(800, 600)
# Screen
#win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
#ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center",
          font=("courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # top and bottom

    #left and Right
    if ball.xcor() > 350:
        score_a += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.dx *= -1

    # paddle and ball collisions
    if ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
