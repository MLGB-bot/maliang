from maliang import Maliang, RectMode

app = Maliang(200, 200)

def on_setup():
    app.rect_mode(RectMode.CENTER)

def on_draw():
    app.rect(50, 50, 80, 80, )
    app.rect(150, 50, 80, 80, )
    # specify mode in func
    app.rect(10, 110, 80, 80, mode=RectMode.CORNER)
    app.rect(150, 150, 40, 40, mode=RectMode.RADIUS)
    app.rect(50, 50, 150, 150, mode=RectMode.CORNERS, filled_color=None, stroke_color=(255, 0, 0))


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.run()
