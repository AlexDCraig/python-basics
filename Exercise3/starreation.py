import turtle
window = turtle.Screen();
my_turtle = turtle.Turtle();
my_turtle.pensize(5);
my_turtle.pencolor("red");


def star(x, y):
	my_turtle.penup();
	my_turtle.setpos(0,60);
	my_turtle.pendown();
	my_turtle.setpos(-50, -50);
	my_turtle.setpos(65, 20);
	my_turtle.setpos(-65, 20);
	my_turtle.setpos(50, -50);
	my_turtle.setpos(0, 60);
	my_turtle.clear();

my_turtle.onclick(star);

window.mainloop();

