from maliang import Maliang, ArcShape


app = Maliang(300, 300)

def on_setup():
    app.fill(0, 255, 0, 100)
    app.stroke(color=(255, 0, 0, 100))

def on_draw():
    app.background(255,)
    app.arc(150, 150, 240, 200, 0,   45,  stroke_width=1, shape=ArcShape.PIE)
    app.arc(150, 150, 240, 200, 90,  180, stroke_width=2, shape=ArcShape.OPEN_PIE)
    app.arc(150, 150, 240, 200, 180, 270, stroke_width=4, shape=ArcShape.CHORD)
    app.arc(150, 150, 240, 200, 270, 360, stroke_width=8, shape=ArcShape.OPEN_CHORD)

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.run()