from maliang import Maliang

app = Maliang()

def on_draw():
    app.circle(50, 50, 80)

app.regist_event('on_draw', on_draw)
app.run()