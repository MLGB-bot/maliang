# -*- coding:utf-8 -*-
import random
from maliang.audio import Audio
from maliang import Maliang
from maliang.units import *
import pyray as pr
import math

app = Maliang(width=500, height=400, double_buffer=True, fps=0)
app.set_trace_log_level(4)


pr.set_audio_stream_buffer_size_default(4096)
a = Audio()
a.init_audio_device()
s = a.init_audio_stream(44100, 16, 1)


MAX_SAMPLES_PER_UPDATE  = 4096
MAX_SAMPLES         =      512
frequency = 440.0
audioFrequency = 440.0
oldFrequency = 1.0
sineIdx = 0.0


def get_data(frames = 200):
    global audioFrequency, sineIdx
    audioFrequency = frequency + (audioFrequency - frequency)*0.95
    audioFrequency += 1.0
    audioFrequency -= 1.0
    incr = audioFrequency/44100.0
    data = b""
    for i in range(frames):
        # ass[i] = 32000.0*math.sin(2*math.pi*sineIdx)
        data += int(32000.0*math.sin(2*math.pi*sineIdx)).to_bytes(2, byteorder='little', signed=True)
        sineIdx += incr
        if (sineIdx > 1.0):
            sineIdx -= 1.0
    return data, frames

s.play()

def on_setup():
    app.background(255)
    # print(raylib.AudioStream)
    pass

def on_draw():
    data, frames = get_data(4096)
    print(len(data), frames)
    print(s.is_processed())
    if s.is_processed():
        s.update(data, int(frames))

    # app.background(255)
    app.point(random.randint(0, app.width), random.randint(0, app.height))

    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        pass
    if app.is_key_clicked(KeyboardKeys.KEY_L):
        print("s: running?", s.playing())

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
