import turtle

is_moving = False
score = 0
gravity = 1.5
damping = 0.8

# main screen properties
main_screen = turtle.Screen()
main_screen.title("Soccer Field Game")
main_screen.bgcolor("#48aa51")
main_screen.setup(width=800,height=800)

# press ball
warning_Text = turtle.Turtle()
warning_Text.hideturtle()
warning_Text.penup()
warning_Text.goto(x=-140,y=0)
warning_Text.color("white")
warning_Text.write("Ready? Click the ball to play!", font=("Helvetica", 16, "normal"))

# scoreboard properties
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-110,350)
scoreboard.pensize(0)
scoreboard.color("white")
scoreboard.write(f"Scoreboard: {score}", font=("Helvetica", 25, "normal"))

# restart properties
restart = turtle.Turtle()
restart.hideturtle()
restart.penup()
restart.goto(x=-385,y=355)
restart.pensize(0)
restart.color("red")
restart.write("Press R for Restart", font=("Helvetica", 14, "bold"))

# exit properties
exit_button = turtle.Turtle()
exit_button.hideturtle()
exit_button.penup()
exit_button.goto(x=205,y=355)
exit_button.pensize(0)
exit_button.color("red")
exit_button.write("Press ESC for Exit", font=("Helvetica", 14, "bold"))


# ball properties
ball = turtle.Turtle()
ball.hideturtle()
ball.color("white")
ball.shape("circle")
ball.shapesize(3)
ball.penup()
ball.goto(0,-300)
ball.showturtle()


# settings
dx = 0
dy = 0
screen_width = 350
screen_height= 300


# functions
def restart_button():
   global score, dx, dy, is_moving
   score = 0
   dx = 0
   dy = 0
   is_moving = False
   scoreboard.clear()
   scoreboard.write(f"Scoreboard: {score}", font=("Helvetica", 25, "normal"))
   ball.goto(0, -300)
   ball.showturtle()
   is_moving = False

def update_scoreboard():
   scoreboard.clear()
   scoreboard.write(f"Scoreboard: {score}", font=("Helvetica", 25, "normal"))

def moveball():
   global dx, dy
   x = ball.xcor()
   y = ball.ycor()
   if x >= screen_width or x <= -screen_width:
      dx = -dx
   if y <= -screen_height:
      dy = -dy * damping
      y = -screen_height
   dy -= gravity
   ball.goto(x + dx,  y + dy)
   if is_moving:
      main_screen.ontimer(moveball, 2)


def onclick_ball(x,y):
   global dx, dy
   global is_moving
   global score
   ball_x, ball_y = ball.xcor(), ball.ycor()

   distance = ((ball_x - x) ** 2 + (ball_y - y) ** 2) ** 0.5


   if distance < 40:
      click_vector_x = x - ball_x
      click_vector_y = y - ball_y
      if not is_moving:
         is_moving = True
         moveball()
      score += 1
      update_scoreboard()
      warning_Text.clear()

      # Vektörü normalize et (birim vektör yap)
      if distance != 0:  # Sıfıra bölmeyi önlemek için
         norm_factor = 35 / distance  # Sekme gücünü kontrol eden sabit (10)
         dx = click_vector_x * norm_factor
         dy = click_vector_y * norm_factor
      else:
         # Tam merkeze tıklanırsa, rastgele bir yön ver
         dx = -100
         dy = 0

def exitbtn():
   main_screen.bye()

main_screen.onkey(fun=exitbtn,key="Escape")
main_screen.onkey(fun=restart_button,key="r")
main_screen.listen()
main_screen.onclick(onclick_ball)


main_screen.mainloop()