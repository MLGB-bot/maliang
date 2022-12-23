# -*- coding:utf-8 -*-
import random
from maliang import Maliang
from maliang.units import *
from maliang.structs import MBoundingBox

app = Maliang(width=800, height=450, double_buffer=True, fps=60)
app.set_trace_log_level(4)

camera = app.camera_3d(
    position=(0, 10, 10),
    target=(0, 0, 0),
    up=(0, 1, 0),
    fovy=45.0,
    projection=CameraProjection.PERSPECTIVE
)

playerPosition = [ 0.0, 1.0, 2.0 ]
playerSize = [ 1.0, 2.0, 1.0 ]
playerColorGreen = (0, 255, 0)
playerColorRed = (255, 0, 0)

enemyBoxPos = [ -4.0, 1.0, 0.0]
enemyBoxSize = [ 2.0, 2.0, 2.0]

enemySpherePos = [ 4.0, 0.0, 0.0]
enemySphereSize = 1.5


def on_setup():
    app.no_stroke()
    pass

def on_draw():
    if (app.is_key_pressed(KeyboardKeys.KEY_A)):
        playerPosition[0] -= 0.2
    if (app.is_key_pressed(KeyboardKeys.KEY_D)):
        playerPosition[0] += 0.2
    if (app.is_key_pressed(KeyboardKeys.KEY_W)):
        playerPosition[2] -= 0.2
    if (app.is_key_pressed(KeyboardKeys.KEY_S)):
        playerPosition[2] += 0.2

    collision = False

    player_boundingbox = MBoundingBox()
    player_boundingbox.init_from_cube(*playerPosition, *playerSize)

    enemybox_boundingbox = MBoundingBox()
    enemybox_boundingbox.init_from_cube(*enemyBoxPos, *enemyBoxSize)
    if app.check_collision_boxes(
        player_boundingbox, enemybox_boundingbox
    ):
        collision = True

    if app.check_collision_box_sphere(
        player_boundingbox,
        enemySpherePos,
        enemySphereSize
    ):
        collision = True

    if (collision):
        playerColor = playerColorRed
    else:
        playerColor = playerColorGreen

    #
    app.background(235, 235, 235)
    app.begin_camera(camera)
    app.cube(
        *enemyBoxPos, *enemyBoxSize, filled_color=(100,), stroke_color=(255, 0, 0 )
    )
    app.sphere(*enemySpherePos, enemySphereSize, filled_color=(100,), stroke_color=(255, 200, 0 ))

    app.cube(*playerPosition, *playerSize, filled_color=playerColor, stroke_color=(200, 0, 0))

    app.grid(10, 1)

    app.end_camera()
    app.text("Move player with cursors to collide", 220, 40, 20, (150,))

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.loop()
