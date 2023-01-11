from maliang import Maliang, CircleMode

app = Maliang(200, 200)


def on_setup():
    app.circle_mode(CircleMode.CENTER)


def on_draw():
    app.circle(50, 50, 80)  # CENTER
    app.circle(150, 50, 80)  # CENTER
    # specify mode in func
    app.circle(10, 110, 80, 80, mode=CircleMode.CORNER)  # CORNER
    app.circle(150, 150, 40, 40, mode=CircleMode.RADIUS)  # RADIUS


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.run()
