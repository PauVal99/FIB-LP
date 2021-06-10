from Turtle3DProfe import Turtle3D

turtle = Turtle3D()

def cercle(mida, costats):
    for i in range(costats):
        turtle.forward(mida).left(360 / costats)

def espiral(cercles):
    if cercles > 0:
        cercle(1, 12)
        turtle.up(5)
        espiral(cercles - 1)

#espiral(5)

turtle.up()
for i in range(8):
    if i % 2 == 0:
        turtle.forward().left()
    else:
        turtle.forward().right()

#turtle.forward().right().forward().up().forward().right().forward()