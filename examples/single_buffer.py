# -*- coding:utf-8 -*-


"""
By:
Time:
Intro:

"""
import pyray as pr
import random

WIDTH, HEIGHT=100, 100

pr.init_window(WIDTH, HEIGHT, "Hello")
pr.set_target_fps(10)

texture2d = pr.load_render_texture(WIDTH, HEIGHT)
pr.begin_texture_mode(texture2d)
pr.clear_background(pr.WHITE)
pr.clear_background((100, 0, 0, 100))
pr.end_texture_mode()
while not pr.window_should_close():
    pr.begin_texture_mode(texture2d)
    pr.draw_pixel(random.randint(0, WIDTH), random.randint(0, HEIGHT), pr.RED)
    pr.end_texture_mode()

    pr.begin_drawing()
    pr.draw_texture(texture2d.texture, 0, 0, pr.WHITE)
    pr.end_drawing()

pr.unload_render_texture(texture2d)
pr.close_window()