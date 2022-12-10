# -*- coding:utf-8 -*-

import time
import random
import pyray as pr

from maliang.audio import Audio

from maliang import Maliang
from maliang.units import *


app = Maliang(width=500, height=400, double_buffer=True, fps=10)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')


a = Audio()
a.init_audio_device()
s1 = a.load_sound('target.ogg')
s2 = a.load_sound('weird.wav')

# time.sleep(10)

def on_setup():
    s1.play()
    s2.play()


def on_draw():
    # global a,s1, s2
    # app.background(200, 200, 255, 50)
    # app.background(200, 200, 255, 255)
    app.background(255)
    if app.is_key_clicked(KeyboardKeys.KEY_A):
        s1.play()
    if app.is_key_clicked(KeyboardKeys.KEY_B):
        s2.play()
    if app.is_key_clicked(KeyboardKeys.KEY_C):
        s1.play_multi()
    if app.is_key_clicked(KeyboardKeys.KEY_D):
        s2.play_multi()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
