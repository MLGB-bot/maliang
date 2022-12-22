# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *

app = Maliang(width=100, height=100, double_buffer=False, fps=30)
app.set_trace_log_level(4)


def on_setup():
    # app.set_window_opacity(0.5)
    app.circle_mode(CircleMode.CENTER)
    app.stroke((255, 0,0), 2)
    app.background(255)
    pass

def on_draw():
    # app.minimize_window()   # no
    # app.background(255)

    # print(app.width, app.height)
    new_width = random.randint(100, 300)
    new_height = random.randint(100, 300)

    # app.set_window_size(new_width, new_height)    # resized
    # print("new: ", new_width, new_height)
    # print(app.frame_count, "resized: ", app.is_window_resized())
    # app.maximize_window()   # resized
    print(app.frame_count, "resized: ", app.is_window_resized())
    app.rect(0, 0, 50, 50, filled_color=(255, 200, 100, 255))
    app.point(random.randint(0, app.width), random.randint(0, app.height))
    app.line(app.width, 0, app.width, app.height)
    app.line(0, app.height, app.width, app.height)
    app.line(0, 0, app.width, app.height)
    app.line(0, app.height, app.width, 0)
    app.circle(app.width, app.height, 10)
    app.point(app.width, app.height, stroke_width=2)
    app.circle(0, 0, 10)
    app.point(0, 0, stroke_width=2)

    print("screen: ", app.get_screen_width(), app.get_screen_height())
    print("app: ", app.width, app.height)
    print()
    if app.is_window_resized():
        pass
        # app.background(255, 0, 0)
        # app.set_window_size(app.width, app.height)  # resized
        # app.circle(app.width, app.height, 20, filled_color=(255, 200, 100, 255))
        # app.close_window()
        # app.init_window(app.width, app.height)


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
