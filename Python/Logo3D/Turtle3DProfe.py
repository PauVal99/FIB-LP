from vpython import *


class Turtle3D:
    RADIUS = 0.2

    def __init__(self):
        self.__position = vector(0, 0, 0)
        self.__alpha = 0
        self.__beta = 0
        self.__direction = vector(1, 0, 0)
        self.__color = color.red
        self.hidden = False

        scene.width, scene.height = 1280, 720
        scene.camera.rotate(angle=radians(45), axis=vector(0, 1, 0))
        scene.autocenter = True
        scene.caption = """\n
            To rotate drag with right button.\n
            To zoom use scroll wheel.
            """
        cylinder(pos=vector(0,0,0), axis=vector(10,0,0), radius=0.1, color=color.white)
        cylinder(pos=vector(0,0,0), axis=vector(0,10,0), radius=0.1, color=color.white)
        cylinder(pos=vector(0,0,0), axis=vector(0,0,10), radius=0.1, color=color.white)

    def __tail__(self, length):
        if not self.hidden:
            sphere(pos=self.__position, radius=self.RADIUS, color=self.__color)
            cylinder(pos=self.__position, axis=self.__direction *
                     length, radius=self.RADIUS, color=self.__color)
            sphere(pos=self.__position + self.__direction *
                   length, radius=self.RADIUS, color=self.__color)

    def __direction__(self):
        self.__direction = norm(vector(cos(self.__alpha) * cos(self.__beta),
                                       sin(self.__alpha) * cos(self.__beta),
                                       sin(self.__beta)))

    def left(self, amount=90):
        self.__alpha += radians(amount)
        self.__direction__()
        return self

    def right(self, amount=90):
        self.__alpha -= radians(amount)
        self.__direction__()
        return self

    def up(self, amount=90):
        self.__beta += radians(amount)
        self.__direction__()
        return self

    def down(self, amount=90):
        self.__beta -= radians(amount)
        self.__direction__()
        return self

    def forward(self, amount=1):
        self.__tail__(amount)
        self.__position += self.__direction * amount
        return self

    def backward(self, amount=1):
        self.__position -= self.__direction * amount
        self.__tail__(amount)
        return self

    def color(self, red, green, blue):
        self.__color = vector(red, green, blue)
        return self

    def hide(self):
        self.hidden = True
        return self

    def show(self):
        self.hidden = False
        return self

    def home(self):
        self.__position = vector(0, 0, 0)
        self.__direction = vector(1, 0, 0)
        return self
