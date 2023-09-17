import turtle as t
t.title("draw")
t.hideturtle()
player = t.Turtle(shape="turtle")
player.up()
def left():
    player.left(30)
def right():
    player.right(30)
def fd():
    player.forward(5)

t.listen()
t.onkeypress(left, "a")
t.onkeypress(right, "d")
t.onkeypress(fd, "w")

t.onkey(player.up, "q")
t.onkey(player.down, "e")

while True:
    t.fd(0)
    

