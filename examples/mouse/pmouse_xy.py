from maliang import Maliang

app = Maliang(buffer_proxy=True)


def on_draw():
    app.line(app.mouse_x, app.mouse_y, app.pmouse_x, app.pmouse_y)

app.regist_event("on_draw", on_draw)

app.run()