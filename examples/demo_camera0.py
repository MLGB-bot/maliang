# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *

app = Maliang(width=500, height=400, double_buffer=True, fps=80)
app.set_trace_log_level(4)

camera = app.camera_2d()

player = {
    "x": 250,
    "y": 200,
}

buildings = []

def on_setup():
    # print(raylib.AudioStream)
    pass

def on_draw():
    app.background(255, 50)
    # app.point(random.randint(0, app.width), random.randint(0, app.height))

    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        pass
    if app.is_key_pressed(KeyboardKeys.KEY_LEFT):
        # print("s: running?", )
        player['x'] -= 1
    if app.is_key_pressed(KeyboardKeys.KEY_RIGHT):
        # print("s: running?", )
        player['x'] += 1

    app.begin_camera(camera)
    # x = 0
    # for i in range(100):
    #     y = random.randint(2, 10)
    #     w = random.randint(5, 20)
    #     h = random.randint(50, 100)
    #     x += w
    #     app.rect(x, y, w, h)
    app.circle(player['x'], player['y'], d=10, mode=2)
    app.end_camera()

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
