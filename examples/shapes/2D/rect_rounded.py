from maliang import Maliang

app = Maliang()


def on_draw():
    app.rect_rounded(10, 10, 80, 80, roundness=0.5, filled_color=None)
    app.rect_rounded(10, 10, 80, 80, roundness=1, stroke_color=(255, 0, 0))


app.regist_event('on_draw', on_draw)
app.run()
