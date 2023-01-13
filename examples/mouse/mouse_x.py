from maliang import Maliang

app = Maliang()


def on_draw():
    app.background(255)

app.regist_event("on_draw", on_draw)

app.run()