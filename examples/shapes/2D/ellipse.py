from maliang import Maliang

app = Maliang()

def on_draw():
    app.ellipse(50, 50, 80, 60,)

app.regist_event('on_draw', on_draw)
app.run()