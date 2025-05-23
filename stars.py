from turtle import *
from math import pi

def draw_star(points, side_len):
    winds = 2 # eller tre for nogle antal takker. WTF?

    for point in range(points):
        forward(side_len)
        left(360 / (points / winds))

    #if position() != origin:
    #    goto(origin)

if __name__ == '__main__':
    draw_star(9, 100)
    mainloop()