from maliang import Maliang

app = Maliang()

def on_draw():
    app.rect(10, 20, 80, 60)

app.regist_event('on_draw', on_draw)
app.run()