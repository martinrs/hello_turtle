# Forløb i Moodle baseret på https://docs.python.org/3/library/turtle.html

# Tegne trekant, firkant, sekskant
# Farve, størrelse og pen op/ned
# Algoritmisk tegning (generel polygonfunktion)
# Miniprojekter:
# - Funktion til tegning af stjerner med x takker
# - Spiral (Matematisk formel?)
# - Træer (løfte pen og stregtykkelse) https://www.thegrove3d.com/learn/da-vincis-rule-of-trees/

from turtle import *

def draw_polygon(sides, side_len):
    reset()
    for side in range(sides):
        fd(side_len)
        rt(360/sides)


draw_polygon(5, 100)
mainloop()