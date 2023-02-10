from maliang import Maliang, CameraProjection, MouseButtons, CameraMode

app = Maliang(width=300, height=300)


camera = app.camera_3d()

camera.position = (10, 10, 10)
camera.target = (0, 0, 0)
camera.up = (1, 1, 0)
camera.fovy = 45.0
camera.projection = CameraProjection.PERSPECTIVE


def on_draw():
    app.background(255, )
    app.begin_camera(camera)

    app.grid(10, 1)

    app.line3d(0, 0, 0, 10, 0, 0, stroke_color=(255, 0, 0))
    app.line3d(0, 0, 0, 0, 10, 0, stroke_color=(0, 255, 0))
    app.line3d(0, 0, 0, 0, 0, 10, stroke_color=(0, 0, 255))

    wheel = app.is_mouse_wheel()
    if wheel:
        camera.fovy -= wheel
        if camera.fovy < 1:
            camera.fovy = 1

    delta = app.delta
    if app.is_mouse_down(MouseButtons.MOUSE_BUTTON_LEFT) and delta != (0, 0):
        # if delta[0] < 0:
        #     camera.up.x -= 0.1
        # elif delta[0] > 0:
        #     camera.up.x += 0.1

        if delta[1] < 0:
            camera.up.y -= 0.1
        elif delta[1] > 0:
            camera.up.y += 0.1
        # print(camera.up.value)

    app.end_camera()


app.regist_event('on_draw', on_draw)

app.run()