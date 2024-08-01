#first we import turtle
import turtle

wind = turtle.Screen()#make screen
# wind.title("ping pong by die Gewinners")set title of the window
wind.bgcolor("black")#set the bg color to black
wind.setup(width = 800, height =600)#set the measurements of the screen
wind.tracer(0)#stop the win from updating automaticly




    
# madrab1

madrab1 = turtle.Turtle()# makes turtle object
madrab1.speed(0)#set the speed
madrab1.shape("square")#set el shape
madrab1.shapesize(stretch_wid=5, stretch_len= 1)#strech el madrab 
madrab1.color("blue")#set el color
madrab1.penup()#stops the drawing lines 
madrab1.goto(-350, 0)#set the position

# madrab2
madrab2 = turtle.Turtle()# makes turtle object
madrab2.speed(0)#set the speed
madrab2.shape("square")#set el shape
madrab2.shapesize(stretch_wid=5, stretch_len= 1)#strech el madrab 
madrab2.color("red")#set el color
madrab2.penup()#stops the drawing lines 
madrab2.goto(350, 0)#set the position


#ball
ball = turtle.Turtle()# makes turtle object
ball.speed(0)#set the speed
ball.shape("circle")#set el shape

ball.color("white")#set el color
ball.penup()#stops the drawing lines 
ball.goto(0, 0)#set the position

while True:
    wind.update()#updates the screen when we run the code
