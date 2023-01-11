from maliang import Maliang

app = Maliang()

def on_draw():
    app.background(255)
    app.poly(50, 50, 30, 5, rotation=0)

app.regist_event('on_draw', on_draw)
app.run()