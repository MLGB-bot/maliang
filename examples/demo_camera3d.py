# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *
import pyray as pr

app = Maliang(width=800, height=450, double_buffer=True, fps=80)
app.set_trace_log_level(4)

MAX_BUILDINGS = 1000


camera = app.camera_3d()

camera.position = (0, 10, 10)
# camera.target = (0, 0, 0)
camera.up = (0, 1, 0)
camera.fovy = 45.0
camera.projection = pr.CameraProjection.CAMERA_PERSPECTIVE

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
    app.background(255, 50)
    app.begin_camera(camera)
    pr.draw_cube(pr.Vector3(0, 0, 0), 2,2,2,pr.Color(*pr.RED))
    pr.draw_cube_wires(pr.Vector3(0, 0, 0), 2,2,2,pr.Color(*pr.YELLOW))
    pr.draw_grid(10, 1)
    app.end_camera()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
