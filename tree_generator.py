from turtle import *
import random

# https://www.thegrove3d.com/learn/da-vincis-rule-of-trees/
# https://www.thegrove3d.com/learn/the-golden-angle-in-trees/

start_width = 100
start_len = 200

branch_angle = 35 # 42,5
angle_variance = 20
width_ratio = 1.6
length_ratio = 1.5
length_variance = 15

def draw_branches(start_pos, old_width, old_heading, old_length):
    # Beregn ny tykkelse og længde. Stop når den bliver tynd
    width(old_width // width_ratio)
    if width() <= 0.5:
        return

    length = old_length // length_ratio
    teleport(start_pos[0], start_pos[1])  # Reset
    angles = [old_heading + branch_angle, old_heading - branch_angle]
    branch_nodes = {}

    for angle in angles:
        teleport(start_pos[0], start_pos[1]) # Reset position
        angle_variation = random.randint(-angle_variance, angle_variance)
        length_variation = random.randint(100-length_variance, 100+length_variance) / 100
        setheading(angle + angle_variation)
        forward(length * length_variation)
        branch_nodes[position()] = heading()

    for pos in branch_nodes:
        draw_branches(pos, width(), branch_nodes[pos], length)
        width(old_width // width_ratio)
        length = old_length // length_ratio
        setheading(old_heading)

if __name__ == '__main__':
    hideturtle()
    speed(10)
    start_pos = (0, -window_height()//2+15)
    teleport(start_pos[0], start_pos[1])
    setheading(90)
    width(start_width)
    forward(start_len)
    draw_branches(position(), start_width, heading(), start_len)
    mainloop()