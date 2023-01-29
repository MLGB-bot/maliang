from maliang import Maliang

app = Maliang()

def on_setup():
    app.no_cursor()

def on_draw():
    app.background(255)
    app.circle(*app.mouse, 10, stroke_width=None, filled_color=(255, 0, 0, 100))

app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)

app.run()