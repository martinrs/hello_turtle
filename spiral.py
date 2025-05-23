from turtle import *
from math import cos, sin, radians

# Bonusopgaver
## Leg med linjetykkelse og -farve

speed(100)

alpha = 4
for angle in range(0, 8000, 15):
    rad = radians(angle)
    x = alpha * rad * cos(rad)
    y = alpha * rad * sin(rad)
    goto(x, y)

mainloop()