# -*- coding:utf-8 -*-

import time
import random
import pyray as pr
from maliang import Maliang
from maliang.structs import MImage

app = Maliang(width=500, height=400, double_buffer=False, fps=0)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

# with open('./resources/yezigongchangmengmashouji.ttf', 'rb') as f:
#     font_data1 = f.read()
# print(len(font_data1))

# font = pr.load_font_from_memory(".ttf", font_data1, len(font_data1), 256, 0, 0 )

# exit(0)

# p = ffi.new("unsigned char[]")
# font_data = ffi.new("unsigned char *")
# font_data = raylib.LoadFileData('./resources/yezigongchangmengmashouji.ttf', p)
# print('font_data:', font_data, type(font_data))
# print(111, p, dir(p))
# font = app.default_font()
# font1 = app.load_font("Canterbury.ttf")
# font1 = app.load_font("SourceHanSerifSC-VF.ttf",)
# font2 = app.load_font("yezigongchangmengmashouji.ttf", )
# font2 = app.load_font("yezigongchangguojiangti.ttf", )
from maliang.libs import FontEnginePillow

# font2 = app.load_font("yezigongchangweifengshouji.ttf", font_engine=2, )
# font2 = app.load_font("yezigongchangweifengshouji.ttf", font_engine=10, engine=FontEnginePillow)
font2 = app.load_font("yezigongchangweifengshouji.ttf", font_engine=10, engine=FontEnginePillow)

#
# exit(0)

image = app.text_image("hello 你好我好大家好hsjf坏大hi我的安怀海端是阿汉地的赛的话uida", font=font2, text_size=20, text_color=(0, 0, 0))

def on_setup():
    global img1
    print("setup")
    app.text_size=20
    # app.background(100, 0, 0, 255)
    # app.line(0, 0, app.width, app.height, 1, stroke_color=pr.BLACK)
    # app.stroke(pr.PINK, )
    # app.line(0, app.height, app.width, 0, stroke_width=10)
    # app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect')
    # app.point(5, 5, stroke_width=1, stroke_color=pr.RED)
    #
    # # app.tint
    # app.textColor(200, 100)
    # app.text("Hello MaLiang, 你好! !", 0, 0, )
    # app.textSize(104)
    # app.text("WORD", 40, 100)
    # app.textSize(56)
    # app.textColor(200, 200, 255)
    # app.text("WORD", 40, 180)

    # #
    # app.text("FONT, 你好", 40, 250, font=font1, text_color=(255, 200, 200), text_size=30)
    # app.text("FONT, 你好", 40, 300, font=font2, text_color=(255, 200, 200), text_size=80, space=5)
    app.image(image, 10, 10)
    app.text("FONT, 你好", random.randint(0, app.width / 2), random.randint(0, app.height / 2), font=font2, )
    app.text("FONT, 你好sjf坏大hi我的\n安怀海端是阿汉地\n的赛的话uida", random.randint(0, app.width/2), random.randint(0, app.height-12), font=font2,)

def on_draw():
    # app.background(200, 200, 255, 50)
    # app.background(200, 200, 255, 255)
    app.background(255, 10)
    # app.image(img2, 100, 50, )
    # app.image(img2, 100, 80, )
    app.textSize(random.randint(12, 100))
    app.textColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    app.text("FONT, 你好sjf坏大hi我的\n安怀海端是阿汉地\n的赛的话uida", random.randint(0, app.width/2), random.randint(0, app.height-12), font=font2, )
    app.image(image, 20, 10)


app.regist_event('on_setup', on_setup)
# app.regist_event('on_draw', on_draw)

def on_mouse_moved(*args):
    print("on_mouse_moved", args)

app.loop()
