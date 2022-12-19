# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *
import pyray as pr

app = Maliang(width=800, height=450, double_buffer=True, fps=80)
app.set_trace_log_level(4)

MAX_BUILDINGS = 1000


camera = app.camera_3d()

camera.position = (10, 10, 10)
camera.target = (0, 0, 0)
camera.up = (0, 1, 0)
camera.fovy = 45.0
camera.projection = app.CAMERA_PROJECTION_PERSPECTIVE

camera.set_mode(CameraMode.CAMERA_FREE)

cube_position = (0, 0, 0)

# camera.target = (player['x'] + 20.0, player['y'] + 20.0, )
# camera.offset = (app.width/2, app.height/2)
# camera.rotation = 0
# camera.zoom = 1.0
RED = (255, 0, 0)
BLACK = (0, 0 ,0)
DARKGRAY = (80, 80, 80)

def on_setup():
    app.no_stroke()
    pass

def on_draw():
    camera.update()
    if app.is_key_pressed(KeyboardKeys.KEY_Z):
        camera.target = (0, 0, 0)

    app.background(*pr.RAYWHITE)


    app.begin_camera(camera)
    for i in range(0, 10, 2):
        app.sphere(x=i, y=0, z=0, diam=1, stroke_color=None, filled_color=(100, 0, 0, 100))
        app.sphere(x=0, y=i, z=0, diam=1, stroke_color=(0, 0,0) , filled_color=(0, 100, 0, 100))
        app.sphere(x=0, y=0, z=i, diam=1, stroke_color=(0, 0,0) , filled_color=(0, 0, 0, 255))


    app.cube(*cube_position, 2, 2, 2, filled_color=RED, stroke_color=BLACK)
    app.grid(10, 1)
    app.end_camera()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
