from maliang import Maliang

app = Maliang()

def on_draw():
    app.background(255)
    app.point(50, 50)

app.regist_event('on_draw', on_draw)
app.run()