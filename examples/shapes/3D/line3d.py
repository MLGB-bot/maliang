from maliang import Maliang, CameraProjection

app = Maliang(width=200, height=200, fps=80)


camera = app.camera_3d()

camera.position = (0, 0, 10)
camera.target = (0, 0, 0)
camera.up = (0, 1, 0)
camera.fovy = 45.0
camera.projection = CameraProjection.ORTHOGRAPHIC

# camera.target = (player['x'] + 20.0, player['y'] + 20.0, )
# camera.offset = (app.width/2, app.height/2)
# camera.rotation = 0
# camera.zoom = 1.0

def on_draw():
    app.background(255, )
    app.begin_camera(camera)
    app.line3d(0, 0, 0, app.width, app.height, 1, stroke_color=(255, 0, 0 ))
    app.end_camera()


app.regist_event('on_draw', on_draw)

app.run()