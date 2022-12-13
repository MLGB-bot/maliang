# -*- coding:utf-8 -*-


"""
By:
Time:
Intro:

"""
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

import time
import random
import pyray as pr
from maliang import Maliang
from maliang.structs import MImage
from raylib._raylib_cffi import ffi


app = Maliang(width=500, height=400, double_buffer=False, fps=10)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

f1 = app.load_font("yezigongchangweifengshouji.ttf", font_engine=app.FONT_PILLOW)

def on_setup():
    text = "hello 你好\\n我好大家好\\n叫啊叫啊\n" + "FONT, 你好sjf坏大hi我的\n安怀海端是阿汉地\n的赛的话uida"
    # f1 = app.load_font("yezigongchangguojiangti.ttf", font_engine=app.FONT_PILLOW)
    # f1.text_image(text, text_size=12, text_color=(0,0,255, ), )
    app.text(text, 0 , 0 , text_size=24, text_color=(0,0,255, ), font=f1, space=50)
    app.text(text, 0, 200, text_size=24, text_color=(0,0,255, ), font=None, space=10)

def on_draw():
    app.background(255, 10)
    app.text("FONT, 你好sjf坏大hi我的\n安怀海端是阿汉地\n的赛的话uida", random.randint(0, app.width/2), random.randint(0, app.height-12), font=f1, space=0)


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
# pr.unload_font(font)
