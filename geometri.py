# Forløb i Moodle baseret på https://docs.python.org/3/library/turtle.html

# Tegne trekant, firkant, sekskant
# Farve, størrelse og pen op/ned
# Algoritmisk tegning (generel polygonfunktion)
# Miniprojekter:
# - Funktion til tegning af stjerner med x takker
# - Spiral (Matematisk formel?)
# - Træer (løfte pen og stregtykkelse) https://www.thegrove3d.com/learn/da-vincis-rule-of-trees/

from turtle import *

forward(100)
left(120)
forward(100)

# Hold skærmen åben
mainloop()

"""
turtle.getscreen()
t = turtle.Turtle()

def draw_polygon(sides, side_len):
    t.reset()
    for side in range(sides):
        t.fd(side_len)
        t.rt(360/sides)

for i in range(2, 16):
    draw_polygon(i, 25)

t.screen.mainloop()"""