import math
import time
import random
import pyray as pr
from maliang import Maliang

app = Maliang(width=410, height=398, double_buffer=True, fps=20)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

texture = app.load_texture('img.png')
print(texture.width, texture.height)
angle = 0.0
MAX_POINTS = 11
texcoords = [
    (0.75, 0.0),
    (0.25, 0.0),
    (0.0, 0.5),
    (0.0, 0.75),
    (0.25, 1.0),
    (0.375, 0.875),
    (0.625, 0.875),
    (0.75, 1.0),
    (1.0, 0.75),
    (1.0, 0.5),
    (0.75, 0.0)  #  Close the poly
]

points = []
for i in range(MAX_POINTS):
    points.append(
        (
            (texcoords[i][0] - 0.5) * 256.0,
            (texcoords[i][1] - 0.5) * 256.0
        )
    )

positions = points.copy()

def on_setup():
    print("setup")

app.regist_event('on_setup', on_setup)

def do_poly(texture, center, points, texcoords, pointCount, tint):
    pr.rl_set_texture(texture.pr_texture.id)
    pr.rl_begin(7)
    pr.rl_color4ub(*tint)

    for i in range(len(texcoords) - 1):
        pr.rl_tex_coord2f(0.5, 0.5)
        pr.rl_vertex2f(*center)

        pr.rl_tex_coord2f(*texcoords[i])
        pr.rl_vertex2f(points[i][0] + center[0], points[i][1] + center[1])

        pr.rl_tex_coord2f(*texcoords[i+1])
        pr.rl_vertex2f(points[i + 1][0] + center[0], points[i + 1][1] + center[1])

        pr.rl_tex_coord2f(*texcoords[i + 1])
        pr.rl_vertex2f(points[i + 1][0] + center[0], points[i + 1][1] + center[1])

    pr.rl_end()
    pr.rl_set_texture(0)

def on_draw():
    global angle, points, positions
    # app.background(200, 200, 255, 50)
    angle += 1
    for i in range(MAX_POINTS):
        pos_vec = pr.vector2_rotate( pr.Vector2(*points[i]), angle * math.pi/180)
        positions[i] = (pos_vec.x, pos_vec.y)

    print(positions)

    app.background(255, )
    pr.draw_text("textured polygon", 20, 20, 20, pr.DARKGRAY)
    do_poly(texture, (app.width/2, app.height/2), positions, texcoords, MAX_POINTS, pr.WHITE)


app.regist_event('on_draw', on_draw)

def on_mouse_moved(*args):
    print("on_mouse_moved", args)

def on_mouse_clicked(*args):
    print("on_mouse_clicked", args)

app.regist_event('on_mouse_clicked', on_mouse_clicked)

app.loop()
texture.unload()