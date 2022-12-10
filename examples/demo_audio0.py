# -*- coding:utf-8 -*-

import time
import random
import pyray as pr

from maliang.audio import Audio

from maliang import Maliang
from maliang.units import *


app = Maliang(width=500, height=400, double_buffer=True, fps=0)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')


a = Audio()
a.init_audio_device()
s1 = a.load_sound('target.ogg')
s2 = a.load_sound('weird.wav')
s3 = a.load_music_stream('country.mp3')
# s3 = a.load_music_stream('weird.wav')
# time.sleep(10)

s4 = a.init_audio_stream(44100, 16, 1)

def on_setup():
    # s1.play()
    s2.play()
    # s3.play()

def on_draw():
    # global a,s1, s2
    # app.background(200, 200, 255, 50)
    # app.background(200, 200, 255, 255)
    s3.update()
    app.background(255)
    app.point(random.randint(0, app.width), random.randint(0, app.height))
    if app.is_key_clicked(KeyboardKeys.KEY_A):
        s1.play()
    if app.is_key_clicked(KeyboardKeys.KEY_B):
        s2.play()
    if app.is_key_clicked(KeyboardKeys.KEY_C):
        s1.play_multi()
    if app.is_key_clicked(KeyboardKeys.KEY_D):
        s2.play_multi()
    #
    if app.is_key_clicked(KeyboardKeys.KEY_H):
        s3.play()
    if app.is_key_clicked(KeyboardKeys.KEY_I):
        s3.pause()
    if app.is_key_clicked(KeyboardKeys.KEY_J):
        s3.resume()
    if app.is_key_clicked(KeyboardKeys.KEY_K):
        s3.stop()
    if app.is_key_clicked(KeyboardKeys.KEY_L):
        print("S3: running?", s3.playing())

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
