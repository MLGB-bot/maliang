from maliang import Maliang

app = Maliang(buffer_proxy=True)


def on_draw():
    app.line(*app.mouse, *app.pmouse)
    print(app.pmouse)

app.regist_event("on_draw", on_draw)

app.run()