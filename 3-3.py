import turtle
import tk
turtle.speed(0)
T = turtle.Turtle()

# i have made a chnage
# code to draw polygon
def drawPolygon(t, sides, size):
	T.pencolor("red")
	T.speed(0)
	# we need to return a list of vertices
	vertices = []

	angle = 360.0/sides # play around with this
	for i in range(sides):
		vertices.append(  t.pos()  )
		t.forward(size)
		t.left(angle)
	# loop ends

	return vertices

def drawEpicycloid(T, multiplier):
	T.speed(0)
	T.pencolor("blue")
	numVertices = 200 # number of vertices or sides
	sideSize    = 4
	v = drawPolygon(T, numVertices, sideSize)

	#==========================

	used = [False]*numVertices

	#do this for all values of current from 1 to 199
	for current in range(1, 100):
		T.penup()
		T.setposition( v[current] )
		T.pendown()

		while used[current] == False:
			T.speed(0)
			used[current] = True # marking this place as used
			nextVertex = (current * multiplier) % numVertices
			# draws a line from current position to v[nextVertex]
			T.setposition( v[nextVertex] )
			current = nextVertex
			
#==================================================

# background setting
T.pensize(2)
turtle.bgcolor("blue")
turtle.tracer(0,0) # turn off animation
T.hideturtle()


#==============================================


x= -329.00
y = 100.00
T.penup()
T.setposition(x, y)
x=T.position()
print(x)
T.pendown()
T.pencolor("black")
T.color('black')
T.begin_fill()
#=======================================================================
# begin to start 2D car figure
T.speed(0)
T.left(60)
T.forward(200)
T.right(60)
T.forward(593.6)
T.right(60)
T.forward(200)
T.left(60)
T.forward(150)
#shape change from bottom
T.right(90)
T.forward(200)
T.left(90)
T.backward(200)
T.left(90)
#===================================================================
# rear tyre code
T.circle(135, 180)

T.left(90)
T.penup()
T.forward(263)
T.left(90)
T.down()
T.speed(0)
drawEpicycloid(T, 41)
#==================================================================

T.up()
T.pencolor("black")
T.setposition(144.00,-100.00)
T.end_fill()
x=T.position()
print(x)
T.left(180)
T.down()
T.color('black')
T.begin_fill()
T.right(90)
T.forward(300)
T.right(90)

#===================================================================
# front tyre code

T.circle(135, 180)
T.left(90)
T.penup()
T.forward(263)
T.left(90)
T.down()
drawEpicycloid(T, 41)
#==================================================================
# code for front bonet
T.up()
T.pencolor("black")
T.goto(-425,-100)
T.down()
T.left(90)
T.forward(120)
T.right(90)
T.forward(200)
T.right(90)
T.forward(216)
T.end_fill()
#skeleton complete

#================================================================
# code for front side window
T.up()
T.speed(0)
T.color('white')
T.begin_fill()
T.forward(20)
T.pendown()
T.left(60)
T.forward(180)
T.right(60)
T.forward(276)
T.right(100)
T.forward(158)
T.right(80)
T.forward(320)
T.end_fill()

#==============================================================================
# code for rear side window complete
T.penup()
T.backward(735)
T.down()
T.color('white')
T.begin_fill()
T.right(60)
T.forward(180)
T.left(60)
T.forward(276)
T.speed(0)
T.left(80)
T.forward(158)
T.left(100)
T.forward(380)
T.end_fill()
T.end_fill()


#finally complete terrible 2D car figure/shape
#==============================================
turtle.update()
turtle.mainloop()
turtle.done()
turtle.exitonclick()
