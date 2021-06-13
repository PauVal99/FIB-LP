from vpython import *


class Turtle3D:
    """
    This class guides a turtle that leaves a wake.

    Methods
    -------
    left :: (degrees) -> Turtle3D
        Turns the turtle *degrees* left.
    right :: (degrees) -> Turtle3D
        Turns the turtle *degrees* right.
    up :: (degrees) -> Turtle3D
        Turns the turtle *degrees* up.
    down :: (degrees) -> Turtle3D
        Turns the turtle *degrees* down.

    forward :: (units) -> Turtle3D
        Move the turtle *units* forward.
    backward :: (units) -> Turtle3D
        Move the turtle *units* backward.

    color :: (degrees) -> Turtle3D
        Changes the turtle wake color.
    hide :: (degrees) -> Turtle3D
        Hides the turtle.
    show :: (degrees) -> Turtle3D
        Shows the turtle.
    home :: (degrees) -> Turtle3D
        The turtle returns to its origin and direction.

    Example
    -------
    from Turtle3D import Turtle3D

    turtle = Turtle3D

    turtle.forward()
    turtle.right()
    turtle.forward()

    Same as
    turtle.forward().right().forward()
    turtle.forward(1).right(90).forward(1)
    turtle.backward(-1).left(-90).backward(-1)

    """

    def left(self, degrees=90):
        """
        Turns the turtle *degrees* left, by default 90. Accepts negative values.
        This method does not print any wake, just turns the turtle.

        Parameters
        ----------
        degrees : float
            Amount of degrees, 90 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__alpha += radians(degrees)
        self.__direction__()
        return self

    def right(self, degrees=90):
        """
        Turns the turtle *degrees* right, by default 90. Accepts negative values.
        This method does not print any wake, just turns the turtle.

        Parameters
        ----------
        degrees : float
            Amount of degrees, 90 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__alpha -= radians(degrees)
        self.__direction__()
        return self

    def up(self, degrees=90):
        """
        Turns the turtle *degrees* up, by default 90. Accepts negative values.
        This method does not print any wake, just turns the turtle.

        Parameters
        ----------
        degrees : float
            Amount of degrees, 90 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__beta += radians(degrees)
        self.__direction__()
        return self

    def down(self, degrees=90):
        """
        Turns the turtle *degrees* down, by default 90. Accepts negative values.
        This method does not print any wake, just turns the turtle.

        Parameters
        ----------
        degrees : float
            Amount of degrees, 90 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__beta -= radians(degrees)
        self.__direction__()
        return self

    def forward(self, units=1):
        """
        Move the turtle *units* forward, by default 1. Accepts negative values.
        This method prints a wake, wake color can be modified in color method.

        Parameters
        ----------
        units : float
            Amount of units, 1 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__wake__(units)
        self.__position += self.__direction * units
        return self

    def backward(self, units=1):
        """
        Move the turtle *units* backward, by default 1. Accepts negative values.
        This method prints a wake, wake color can be modified in color method.

        Parameters
        ----------
        units : float
            Amount of units, 1 by default.

        Returns
        -------
        Self instance after the changes.
        """
        self.__position -= self.__direction * units
        self.__wake__(units)
        return self

    def color(self, red, green, blue):
        """
        Changes wake color in RGB format.

        Parameters
        ----------
        red : float
            Amount of red, from 0 to 1.
        green : float
            Amount of green, from 0 to 1.
        blue : float
            Amount of blue, from 0 to 1.

        Returns
        -------
        Self instance after the changes.
        """
        self.__color = vector(red, green, blue)
        return self

    def hide(self):
        """
        Hides the turtle. It can be still moved while hidden but will not print the wake.

        Returns
        -------
        Self instance after the changes.
        """
        self.__hidden = True
        return self

    def show(self):
        """
        Shows the turtle.

        Returns
        -------
        Self instance after the changes.
        """
        self.__hidden = False
        return self

    def home(self):
        """
        The turtle resets its position and direction.

        Returns
        -------
        Self instance after the changes.
        """
        self.__position = self.__HOME_POSITION
        self.__direction = self.__HOME_DIRECTION
        return self

    """Default wake radius, for easy programming prupouses. Can not be modified."""
    __RADIUS = 0.2
    """Starting position, for easy programming prupouses. Can not be modified."""
    __HOME_POSITION = vector(0, 0, 0)
    """Starting direction, for easy programming prupouses. Can not be modified."""
    __HOME_DIRECTION = vector(1, 0, 0)

    def __init__(self):
        """
        Constructs all the necessary attributes and vpython config.

        Returns
        -------
        New Turtle3D instance.
        """
        self.__position = self.__HOME_POSITION
        self.__direction = self.__HOME_DIRECTION
        self.__alpha = 0
        self.__beta = 0

        self.__color = color.red
        self.__hidden = False

        scene.width, scene.height = 1280, 720
        scene.camera.rotate(angle=radians(45), axis=vector(0, 1, 0))
        scene.autocenter = True
        scene.caption = """\n
            To rotate drag with right button.\n
            To zoom use scroll wheel.
            """

    def __wake__(self, length):
        """
        Internal method.
        Prints a cylinder wake with spheres in the ends.

        Parameters
        ----------
        length : float
            Length of the cylinder.
        """
        if not self.__hidden and length != 0:
            sphere(pos=self.__position, radius=self.__RADIUS, color=self.__color)
            cylinder(pos=self.__position, axis=self.__direction *
                     length, radius=self.__RADIUS, color=self.__color)
            sphere(pos=self.__position + self.__direction *
                   length, radius=self.__RADIUS, color=self.__color)

    def __direction__(self):
        """
        Internal method.
        Updates turtle direction with current alpha and beta angles.
        """
        self.__direction = norm(vector(cos(self.__alpha) * cos(self.__beta),
                                       sin(self.__alpha) * cos(self.__beta),
                                       sin(self.__beta)))
