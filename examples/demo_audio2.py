# -*- coding:utf-8 -*-
import pyaudio
import random
from maliang.audio import Audio
from maliang import Maliang
from maliang.units import *

app = Maliang(width=500, height=400, double_buffer=True, fps=0)
app.set_trace_log_level(4)

a = Audio()
a.init_audio_device()
s = a.init_audio_stream(44100, 16, 1)


def audio_callback(frames):
    pass
    return b""

s.set_callback(audio_callback, 1)
s.play()

def on_setup():
    # print(raylib.AudioStream)
    pass

def on_draw():
    app.background(255)
    app.point(random.randint(0, app.width), random.randint(0, app.height))

    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        pass
    if app.is_key_clicked(KeyboardKeys.KEY_L):
        print("s: running?", s.playing())

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
