import turtle
#draw my first initial (g) with the turtle!
'''draw a capital g, starting with the line from the center'''

def draw_G(the_turtle):
  #line of the G
  the_turtle.forward(50)
  the_turtle.right(90)
  the_turtle.forward(40)
  #right half of bottom curve
  for x in range(3):
    the_turtle.right(30)
    the_turtle.forward(20)
  #left half of bottom curve
  for x in range(3):
    the_turtle.forward(20)
    the_turtle.right(30)
  the_turtle.forward(90)
  for x in range(3):
    the_turtle.right(30)
    the_turtle.forward(20)
  for x in range(3):
    the_turtle.forward(20)
    the_turtle.right(30)

my_turtle = turtle.Turtle()

#draw_G(my_turtle)

second_turtle = turtle.Turtle()
second_turtle.penup()
second_turtle.setpos(150,0)
second_turtle.pendown()
#draw_G(second_turtle)

#turtle1.setpos(-50, -50)
x_coordinate = 0
y_coordinate = 0

def draw_G(the_turtle, size):
    '''Turtle2 draws the initial "G" '''
    
    the_turtle.pensize(size)

    the_turtle.penup()
   
    the_turtle.goto(x_coordinate + 200, y_coordinate)

    the_turtle.right(180)

    the_turtle.pendown()

    the_turtle.circle(100,270)

    the_turtle.left(90)

    the_turtle.forward(50)

    the_turtle.backward(60)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.right(180)

    the_turtle.penup()

    the_turtle.forward(200)

    the_turtle.left(90)

    the_turtle.forward(110)

    the_turtle.left(90)

    the_turtle.pendown()

    the_turtle.forward(20)

turtleG = turtle.Turtle() # Create a second new Turtle object

draw_G(turtleG, 5)      # make the new turtle draw the letter "G"