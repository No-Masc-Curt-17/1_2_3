#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
def draw_an_A():
  drawer.penup()
  drawer.goto(0,-200)
  drawer.pendown()
  drawer.color("blue")
  drawer.write("A", font=("Arial", 55, "bold")) 

def drop():
  apple.penup()
  apple.goto(0,-200)
  apple.pendown()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
#-----function calls-----

draw_apple(apple)
wn.bgpic("background.gif")
drawer.penup()
drawer.goto(-22,-45)
drawer.pendown()
drawer.color("white")
drawer.write("A", font=("Arial", 55, "bold")) 
wn.onkeypress(drop, "a")
wn.listen()
wn.mainloop()