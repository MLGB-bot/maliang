from maliang import Maliang

app = Maliang(200, 200)

def on_draw():
    app.background(255)
    app.ring(50, 50, 60, 80, 0, 360, filled_color=(255, 100, 100, 50), stroke_width=1, stroke_color=(255, 0, 0, 100))
    app.ring(app.width/2, app.height/2, 120, 180, -60, 120, filled_color=(255, 100, 100, 50), stroke_width=2, stroke_color=(255, 0, 0, 100))

app.regist_event('on_draw', on_draw)
app.run()
