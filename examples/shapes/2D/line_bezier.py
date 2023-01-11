from maliang import Maliang

app = Maliang()

def on_draw():
    app.background(255)
    app.line_bezier(0, 0, 100, 100)

app.regist_event('on_draw', on_draw)
app.run()