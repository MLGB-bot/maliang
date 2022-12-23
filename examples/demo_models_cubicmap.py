# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *
from maliang.structs import MMesh, MMaterial
import pyray as pr

app = Maliang(width=800, height=450, double_buffer=True, fps=60)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/model/')

camera = app.camera_3d(
    position=(16, 14, 16),
    target=(0, 0, 0),
    up=(0, 1, 0),
    fovy=45.0,
    projection=CameraProjection.PERSPECTIVE
)
camera.set_mode(CameraMode.CAMERA_ORBITAL)

image = app.load_image("cubicmap.png")
cubicmap = image.load_texture()
mesh = app.gen_mesh_cubicmap(image, 1,1,1)
image.unload()

model = mesh.load_model()
material = model.materials[0]
texture = app.load_texture('cubicmap_atlas.png')
material.set_texture(MMaterial.MATERIAL_MAP_DIFFUSE, texture)

mapPosition = [-16.0, 0.0, -8.0]

def on_setup():
    app.no_stroke()
    pass

def on_draw():
    camera.update()
    app.background(235, 235, 235)
    app.begin_camera(camera)

    model.draw(*mapPosition, scale=1, filled_color=(255, ))
    app.grid(20, 10)

    app.end_camera()
    cubicmap.draw_ex(app.width - cubicmap.width*4.0 - 20, 20.0, )

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()

texture.unload()
cubicmap.unload()
model.unload()
