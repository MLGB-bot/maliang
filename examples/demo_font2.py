# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

import time
import random
import pyray as pr
from maliang import Maliang
from maliang.structs import MImage
from raylib._raylib_cffi import ffi


app = Maliang(width=500, height=400, double_buffer=True, fps=10)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

# font2 = app.load_font("yezigongchangweifengshouji.ttf", )
# image = app.text_image(, font=font2, text_size=20, text_color=(0, 0, 0))


def on_setup():
    text = "hello 你好\n我好大家好\n"
    bytes_text = text.encode()
    # print(text.encode())
    font_size = 20
    font = pr.load_font("yezigongchangweifengshouji.ttf")
    print(font, font.baseSize, font.glyphCount, dir(font))

    t_length = len(text) #pr.text_length(text)
    print(2, t_length)

    scaleFactor = font_size / font.baseSize
    spacing = 3
    x = 0
    y = 0
    offset_x = 0
    offset_y = 0
    for i in range(t_length):
        codepointByteCount = ffi.new("int *")
        codepoint = pr.get_codepoint( text[i], codepointByteCount)
        index = pr.get_glyph_info(font, codepoint)
        print(i, codepoint, codepointByteCount[0], index)
        if codepoint == 63:
            # 0x3f
            # NOTE: Normally we exit the decoding sequence as soon as a bad byte is found (and return 0x3f)
            # but we need to draw all of the bad bytes using the '?' symbol moving one byte
            pass
        else:
            i+=codepointByteCount[0] - 1

        if codepoint != 10: #'\n':
            print(333, font.recs)
            print(3334, font.recs[0])
            print(font.recs[0].width)
            print(555, dir(index), index.value)
            print(3, font.recs[index.value].width)
            glyphWidth = font.recs[index.value].width*scaleFactor if (font.glyphs[index.value].advanceX == 0) \
                else font.glyphs[index.value].advanceX*scaleFactor
            print(66, glyphWidth)
            if (i + 1 < t_length):
                glyphWidth = glyphWidth + spacing
            print(77, glyphWidth)
            pr.draw_text_codepoint(font, codepoint, pr.Vector2(x+offset_x, y+offset_y) , font_size, pr.BLACK)
            offset_x += glyphWidth


def on_draw():
    app.background(255, 10)


app.regist_event('on_setup', on_setup)
# app.regist_event('on_draw', on_draw)

def on_mouse_moved(*args):
    print("on_mouse_moved", args)

app.loop()
# pr.unload_font(font)
