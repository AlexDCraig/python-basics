import turtle
window = turtle.Screen();
my_turtle = turtle.Turtle();
my_turtle.pensize(10);
my_turtle.pencolor("blue");

def Alex(x, y):
	my_turtle.penup();
	# Make A
	my_turtle.setpos(-300, 0);
	my_turtle.pendown();
	my_turtle.setpos(-275, 100);
	my_turtle.setpos(-250, 0);
	my_turtle.penup();
	my_turtle.setpos(-285, 50);
	my_turtle.pendown();
	my_turtle.setpos(-260, 50);
	my_turtle.penup();
	# Make L
	my_turtle.setpos(-230 , 0);
	my_turtle.pendown();
	my_turtle.setpos(-230, 100);
	my_turtle.penup();
	my_turtle.setpos(-230, 0);
	my_turtle.pendown();
	my_turtle.setpos(-195 , 0);
	# Make E
	my_turtle.penup();
	my_turtle.setpos(-180, 0);
	my_turtle.pendown();
	my_turtle.setpos(-180 , 100);
	my_turtle.setpos(-150, 100);
	my_turtle.penup();
	my_turtle.setpos(-180, 50);
	my_turtle.pendown();
	my_turtle.setpos(-150, 50);
	my_turtle.penup();
	my_turtle.setpos(-180, 0);
	my_turtle.pendown();
	my_turtle.setpos(-150, 0);
	# Make X
	my_turtle.penup();
	my_turtle.setpos(-120, 0);
	my_turtle.pendown();
	my_turtle.setpos(-90, 100);
	my_turtle.penup();
	my_turtle.setpos(-120, 100);
	my_turtle.pendown();
	my_turtle.setpos(-90, 0);
	my_turtle.penup();
	my_turtle.clear();

my_turtle.onclick(Alex);

window.mainloop();

