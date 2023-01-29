from maliang import Maliang

app = Maliang()

def on_draw():
    app.background(255)
    print(app.delta)

app.regist_event("on_draw", on_draw)

app.run()