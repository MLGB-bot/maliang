from maliang import Maliang, EllipseMode

app = Maliang(200, 200)


def on_setup():
    app.ellipse_mode(EllipseMode.CENTER)


def on_draw():
    app.ellipse(50, 50, 80, 60)  # CENTER
    app.ellipse(110, 10, 60, 80, mode=EllipseMode.CORNER)  # CORNER
    # specify mode in func
    app.ellipse(50, 150, 40, 30, mode=EllipseMode.RADIUS)  # RADIUS
    app.ellipse(110, 110, 170, 190, mode=EllipseMode.CORNERS)  # CORNERS


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.run()
