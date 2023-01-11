from maliang import Maliang

app = Maliang()

def on_draw():
    app.circle_gradient(50, 50, 100, colors=[(255, 0, 0), (0, 255, 0)])

app.regist_event('on_draw', on_draw)
app.run()