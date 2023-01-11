from maliang import Maliang

app = Maliang(200, 200, title="Line")

def on_draw():
    app.background(255)
    app.line(50, 50, 150, 50)
    app.line(150, 50, 150, 150, stroke_width=2, stroke_color=(255, 0, 0))   # width=4 color=red
    app.line(150, 150, 50, 150, stroke_width=4)

app.regist_event('on_draw', on_draw)
app.run()