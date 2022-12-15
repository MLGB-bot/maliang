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
from maliang.libs import FontEnginePillow
from maliang.libs.font.engine_freetype import FontEngineFreetype

app = Maliang(width=500, height=400, double_buffer=False, fps=0)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

# f1 = app.load_font("yezigongchangweifengshouji.ttf", engine_id=0, engine=FontEnginePillow)
# f1 = app.load_font("yezigongchangweifengshouji.ttf", engine_id=app.FONT_PILLOW)
# f1 = app.load_font("yezigongchangweifengshouji.ttf", engine_id=0, engine=FontEnginePillow)
f1 = app.load_font("yezigongchangweifengshouji.ttf", engine_id=0, engine=FontEngineFreetype)

text = "hello Fontf 你好\n我好大家好\n叫啊叫啊\n" + "FONT, 你好sjf坏大hi我的\n安怀海端是阿汉地\n的赛的话uida"
text = "hello \n\n Fontf"

image = app.text_image(text, font=f1)

def on_setup():
    # text = "hello Fontf你好"
    # text = "Fontfontga阿瓦达多"
    # text = "Font"
    # text = "1asdad"
    # f1 = app.load_font("yezigongchangguojiangti.ttf", font_engine=app.FONT_PILLOW)
    # f1.text_image(text, text_size=12, text_color=(0,0,255, ), )
    app.text(text, 0 , 0 , text_size=12, text_color=(0,0,255, ), font=f1)
    # app.text(text, 0 , 50 , text_size=18, text_color=(0,0,255, ), font=f1)
    # app.text(text, 0 , 100 , text_size=24, text_color=(0,0,255, ), font=f1)
    # app.text(text, 0 , 150 , text_size=36, text_color=(0,0,255, ), font=f1)
    app.text(text, 0 , 200 , text_size=48, text_color=(0,0,255, ), font=f1)
    # app.text(text, 0 , 200 , text_size=48, text_color=(0, 255, 0, 100), font=f1)
    app.line(0, app.height/2, app.width, app.height/2)
    # app.text(text, 0, 200, text_size=24, text_color=(0,0,255, ), font=None, space=10)

def on_draw():
    # app.background(255, 10)
    app.background(255)
    # print('sa')
    # app.text("FONT 你好", random.randint(0, app.width/2), random.randint(0, app.height-12), font=f1)

    app.text(text, random.randint(0, app.width/2), random.randint(0, app.height-12), text_size=24, font=f1)
    app.image(image, random.randint(0, app.width/2), random.randint(0, app.height-12), )


    pr.draw_fps(20, app.height-30)

app.regist_event('on_setup', on_setup)
# app.regist_event('on_draw', on_draw)

app.loop()
# pr.unload_font(font)
