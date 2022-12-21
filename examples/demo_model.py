# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *

app = Maliang(width=800, height=450, double_buffer=True, fps=80)
app.set_trace_log_level(4)

camera = app.camera_3d()

def on_setup():
    app.no_stroke()
    pass

def on_draw():
    app.background(255, 50)
    app.begin_camera(camera)

    app.end_camera()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
