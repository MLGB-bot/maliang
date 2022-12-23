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
    position=(0.2, 0.4, 0.2),
    target=(0, 0, 0),
    up=(0, 1, 0),
    fovy=45.0,
    projection=CameraProjection.PERSPECTIVE
)
camera.set_mode(CameraMode.CAMERA_FIRST_PERSON)

image = app.load_image("cubicmap.png")
cubicmap = image.load_texture()
mesh = app.gen_mesh_cubicmap(image, 1,1,1)

mapPixels = image.load_colors()
image.unload()

model = mesh.load_model()
material = model.materials[0]
texture = app.load_texture('cubicmap_atlas.png')
material.set_texture(MMaterial.MATERIAL_MAP_DIFFUSE, texture)

mapPosition = [-16.0, 0.0, -8.0]

def on_setup():
    app.rect_mode(RectMode.CORNER)
    app.circle_mode(CircleMode.RADIUS)
    pass

def on_draw():
    oldCamPos = camera.position
    camera.update()
    newCamPos = camera.position
    player_position = (newCamPos[0], newCamPos[2])
    player_radius = 0.1
    player_cell_x = int(player_position[0] - mapPosition[0] + 0.5)
    player_cell_y = int(player_position[1] - mapPosition[2] + 0.5)
    if (player_cell_x < 0):
        player_cell_x = 0
    elif (player_cell_x >= cubicmap.width):
        player_cell_x = cubicmap.width - 1

    if (player_cell_y < 0):
        player_cell_y = 0
    elif (player_cell_y >= cubicmap.height):
        player_cell_y = cubicmap.height - 1

    # Check map collisions using image data and player position
    # Improvement: Just check player surrounding cells for collision

    # print(player_position, player_radius)

    for y in range(cubicmap.height):
        for x in range(cubicmap.width):
            # Collision: white pixel, only check R channel

            if mapPixels[y*cubicmap.width + x].r == 255 and \
                app.check_collision_circle_rec(
                    *player_position, player_radius,
                    mapPosition[0] - 0.5 + x*1.0,
                    mapPosition[2] - 0.5 + y*1.0,
                    1.0,
                    1.0
                ):
                # // Collision detected, reset camera position
                camera.position = oldCamPos

    app.background(235, 235, 235)
    app.begin_camera(camera)
    model.draw(*mapPosition, scale=1, filled_color=(255, ))
    # app.grid(20, 10)
    app.end_camera()
    cubicmap.draw_ex(app.width - cubicmap.width*4.0 - 20, 20.0, scale=4)
    # print(app.width - cubicmap.width * 4 - 20 + player_cell_x * 4, 20 + player_cell_y * 4)
    app.rect(app.width - cubicmap.width * 4 - 20 + player_cell_x * 4, 20 + player_cell_y * 4, 4, 4, filled_color=(255, 0,0))

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()

texture.unload()
cubicmap.unload()
model.unload()
