import turtle as tr

tree = tr.Turtle()
tree.left(90)
tree.speed(100)
myWin = tr.Screen()

# recursion
def draw(num):
	if (num < 10):
		return
	else:
		tree.forward(num)
		tree.left(30)
		draw(4 * num/5)
		tree.right(60)
		draw(4 * num/5)
		tree.left(30)
		tree.backward(num)

draw(100)
myWin.exitonclick()
