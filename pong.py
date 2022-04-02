import time
import turtle as t

def main():
    start()

def start():
    name_playerA = input("Quel est votre nom, 'joueur n°1' ? ")
    name_playerB = input("Quel est votre nom, 'joueur n°2' ? ")

    if __name__ == "__main__":
        #creating the platform
        window = t.Screen()
        window.title("Pong Game")
        window.bgcolor('black')
        window.setup(width=800, height = 600)
        window.tracer(0)

        pen = t.Turtle()
        pen.speed(0)
        pen.color("White")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,250)
        pen.write("player1 : {}     player2 : {}".format(name_playerA, name_playerB), align = 'center', font = ('Arial', 24, 'normal'))
        pen.goto(0,75)
        pen.write("The ball leaves randomly at the beginning", align = 'center', font = ('Arial', 24, 'normal'))
        pen.goto(0,25)
        pen.write("but will then leave on the winner of the point.", align = 'center', font = ('Arial', 24, 'normal'))
        pen.color("Red")
        pen.goto(0, -25)
        pen.write("First to 5, win", align = 'center', font = ('Arial', 24, 'normal'))

        time.sleep(5)
        window.clear()
        play(name_playerA, name_playerB)

def play(name_playerA, name_playerB):
    playerAscore=0
    playerBscore=0

    window = t.Screen()
    window.title("Pong Game")
    window.bgcolor('black')
    window.setup(width=800, height = 600)
    window.tracer(0)

    #creating left paddle
    leftpaddle = t.Turtle()
    leftpaddle.speed(0)
    leftpaddle.shape("square")
    leftpaddle.color("white")
    leftpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
    leftpaddle.penup()
    leftpaddle.goto(-350,0)

    #creating right paddle
    rightpaddle = t.Turtle()
    rightpaddle.speed(0)
    rightpaddle.shape("square")
    rightpaddle.color("white")
    rightpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
    rightpaddle.penup()
    rightpaddle.goto(350,0)

    #creating ball
    ball = t.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(5,5)
    ballxdirection = 0.075
    ballydirection = 0.075

    #creating pen for scorecard update
    pen = t.Turtle()
    pen.speed(0)
    pen.color("Blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("score", align = "center", font =('Arial', 24, 'normal'))

    #moving the paddle
    def leftpaddleup():
        y = leftpaddle.ycor()
        y += 40
        leftpaddle.sety(y)

    def leftpaddledown():
        y = leftpaddle.ycor()
        y -= 40
        leftpaddle.sety(y)

    def rightpaddleup():
        y = rightpaddle.ycor()
        y += 40
        rightpaddle.sety(y)

    def rightpaddledown():
        y = rightpaddle.ycor()
        y -= 40
        rightpaddle.sety(y)

    window.listen()
    window.onkeypress(leftpaddleup, 'a')
    window.onkeypress(leftpaddledown, 'q')
    window.onkeypress(rightpaddleup, 'Up')
    window.onkeypress(rightpaddledown, 'Down')

    while True:
        
        window.update()
        endgame(playerAscore, playerBscore, name_playerA, name_playerB)

        #moving the ball
        ball.setx(ball.xcor()+ballxdirection)
        ball.sety(ball.ycor()+ballydirection)

        #setting up border
        if ball.ycor() > 290:
            ball.sety(290)
            ballydirection = ballydirection * -1
        
        if ball.ycor() < -290:
            ball.sety(-290)
            ballydirection = ballydirection * -1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ballxdirection *= -1
            playerAscore += 1
            pen.clear()
            pen.write("{} : {}     {} : {}".format(name_playerA, playerAscore, name_playerB, playerBscore), align = 'center', font = ('Arial', 24, 'normal'))
        
        if ball.xcor() < -390:
            ball.goto(0,0)
            ballxdirection *= - 1
            playerBscore += 1
            pen.clear()
            pen.write("{} : {}     {} : {}".format(name_playerA, playerAscore, name_playerB, playerBscore), align = 'center', font = ('Arial', 24, 'normal'))

        # Handling the collisions
        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
            ball.setx(340)
            ballxdirection *= -1

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
            ball.setx(-340)
            ballxdirection *= -1    

def endgame(playerAscore, playerBscore, name_playerA, name_playerB):
    window = t.Screen()
    if playerAscore == 5:
        window.clear()
        scoreboard(name_playerA, name_playerB, playerAscore, playerBscore)
    if playerBscore == 5:
        window.clear()
        scoreboard(name_playerA, name_playerB, playerAscore, playerBscore)

def scoreboard(name_playerA, name_playerB, playerAscore, playerBscore):
    window = t.Screen()
    window.title("Scoreboard")
    window.bgcolor('black')
    window.setup(width=800, height = 600)
    window.tracer(0)

    pen = t.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,0)
    if playerAscore > playerBscore:
        pen.write("{} win {} to {} against {}".format(name_playerA, playerAscore, playerBscore, name_playerB), align = 'center', font = ('Arial', 24, 'normal'))
        time.sleep(10)
        window.bye()
    if playerAscore < playerBscore:
        pen.write("{} win {} to {} against {}".format(name_playerB, playerBscore, playerAscore, name_playerA), align = 'center', font = ('Arial', 24, 'normal'))
        time.sleep(10)
        window.bye()

main()
