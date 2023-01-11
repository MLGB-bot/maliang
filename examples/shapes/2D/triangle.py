from maliang import Maliang

app = Maliang()

def on_draw():
    app.triangle(10, 90, 50, 9, 80, 50)

app.regist_event('on_draw', on_draw)
app.run()