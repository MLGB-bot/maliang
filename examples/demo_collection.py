# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *

app = Maliang(width=800, height=450, double_buffer=True, fps=80)
app.set_trace_log_level(4)


def on_setup():
    # app.line(*(0, 0), *(app.width/10, app.height/10))
    # app.line(*(0, app.height), *(app.width, 0))
    # point = app.check_collision_lines(
    #     (0, 0), (app.width, app.height),
    #     (0, app.height), (app.width, 0)
    # )
    # if point:
    #     app.circle(*point, 5.5,)

    # app.line(*(0, app.height), *(app.width, 0))
    # result = app.check_collision_point_line(app.width/2, app.height/2 + 2, *(0, app.height), *(app.width, 0), 3)
    # print(result)

    app.no_fill()
    app.rect_mode(RectMode.RADIUS)
    rec1 = (400, 250, 199, 149,)
    rec2 = (300, 200, 149, 179,)
    app.rect(*rec1)
    app.rect(*rec2)
    rect = app.get_collision_rec(
        *rec1,
        *rec2,
    )
    print(rect)
    app.fill(250, 200, 0, 255)
    app.rect(*rect)

def on_draw():
    # app.background(255, 50)
    pass

app.regist_event('on_setup', on_setup)
# app.regist_event('on_draw', on_draw)

app.loop()
