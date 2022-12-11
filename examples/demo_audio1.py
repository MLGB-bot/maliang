# -*- coding:utf-8 -*-

import time, math
import random
import pyray as pr

from raylib._raylib_cffi import lib, ffi

from maliang.audio import Audio

from maliang import Maliang
from maliang.units import *

app = Maliang(width=500, height=400, double_buffer=True, fps=0)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

MAX_SAMPLES_PER_UPDATE  = 4096
MAX_SAMPLES         =      512
frequency = 440.0
audioFrequency = 440.0
oldFrequency = 1.0
sineIdx = 0.0

a = Audio()
a.init_audio_device()

pr.set_audio_stream_buffer_size_default(4096)

s = a.init_audio_stream(44100, 16, 1)

# def audio_callback(*args, **kwargs):
# @ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)

handle = ffi.new_handle('abac')
_handle = handle

@ffi.callback("void(*)(void *, unsigned int)")
def audio_callback(buffer, frames):
    print("callback: ", buffer , frames)
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
    # print(data)
    # print(len(data), frames, len(data)/ frames,)
    buf = ffi.buffer(buffer , frames*2)
    # print(buf, dir(buf))
    buf[:] = data


pr.set_audio_stream_callback(s.pr_stream, audio_callback)

# // Frame buffer, describing the waveform when repeated over the course of a frame
waveLength = 1
position = ( 0, 0 )
s.play()

def on_setup():
    # print(raylib.AudioStream)
    pass

def on_draw():
    # s.update([125], frame_count=441)
    global frequency, oldFrequency, waveLength
    app.background(255)
    app.point(random.randint(0, app.width), random.randint(0, app.height))
    # if app.is_key_clicked(KeyboardKeys.KEY_A):
    #     s.play()
    # if app.is_key_clicked(KeyboardKeys.KEY_B):
    #     s.play_multi()

    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        fp = app.mouse_y
        frequency = 40.0 + fp
        pan = app.mouse_x / app.width
        s.set_pan(pan)

    if frequency != oldFrequency:
        # // Compute wavelength. Limit size in both directions.
        # //int oldWavelength = waveLength;
        waveLength = int(22050/frequency)
        if (waveLength > MAX_SAMPLES/2): waveLength = MAX_SAMPLES/2
        if (waveLength < 1): waveLength = 1

        # // Scale read cursor's position to minimize transition artifacts
        # //readCursor = (int)(readCursor * ((float)waveLength / (float)oldWavelength));
        oldFrequency = frequency
    if app.is_key_clicked(KeyboardKeys.KEY_L):
        print("s: running?", s.playing())

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
