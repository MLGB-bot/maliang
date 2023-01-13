from maliang import Maliang, KeyboardKeys

app = Maliang()

def on_draw():
    app.background(235)
    if app.is_key_clicked(KeyboardKeys.KEY_F):
        if app.is_window_fullscreen():
            app.un_fullscreen()
        else:
            app.fullscreen()

app.regist_event("on_draw", on_draw)

app.run()