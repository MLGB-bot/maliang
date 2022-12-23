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
    position=(50, 50, 50),
    target=(0, 10, 0),
    up=(0, 1, 0),
    fovy=45.0,
    projection=CameraProjection.PERSPECTIVE
)

model = app.load_model("obj/castle.obj")
texture = app.load_texture("obj/castle_diffuse.png")

materials = model.materials
meshes = model.meshes

material = materials[0]
mesh = meshes[0]

material.set_texture(MMaterial.MATERIAL_MAP_DIFFUSE, texture)
bounds = mesh.get_bounding_box()

camera.set_mode(CameraMode.CAMERA_FREE)

position = [ 0.0, 0.0, 0.0]

# model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture;

selected = False

def on_setup():
    app.no_stroke()
    pass

def on_draw():
    global selected
    camera.update()
    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        ray = app.get_ray(app.mouse_x, app.mouse_y, camera)
        collision = ray.get_collision_box(bounds)
        # print(collision)
        if collision.hit:
            selected = not selected
        else:
            selected = False

    app.background(235, 235, 235)
    app.begin_camera(camera)

    model.draw(*position, scale=1, filled_color=(255, ))
    if (selected):
        app.draw_boundingbox(bounds, (0, 255, 0))
    app.grid(20, 10)

    app.end_camera()

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
