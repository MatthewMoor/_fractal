import turtle as tr

def triangle(points, myTurtle):
    # draws a triangle
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])


def getMiddle(p1, p2):
    # find the middle
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    # degree of triangle
    triangle(points, myTurtle)
    if degree > 0:

        sierpinski([points[0], getMiddle(points[0], points[1]), getMiddle(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMiddle(points[0], points[1]), getMiddle(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMiddle(points[2], points[1]), getMiddle(points[0], points[2])], degree-1, myTurtle)


def main():
    myTurtle = tr.Turtle()
    myWin = tr.Screen()
    points = [[0, 0], [-230, -300], [230, -300]]
    # deeper
    degree = 5
    sierpinski(points, degree, myTurtle)
    myWin.exitonclick()
main()
