from maliang import Maliang

app = Maliang(200, 200)

def on_draw():
    app.rect_gradient(0, 0, 100, 100, direction='xy', colors=(
        (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0),
    ))
    app.rect_gradient(100, 0, 100, 100, direction='x', colors=(
        (255, 0, 0), (0, 255, 0)
    ))
    app.rect_gradient(0, 100, 100, 100, direction='y', colors=(
        (255, 0, 0), (0, 255, 0)
    ))

app.regist_event('on_draw', on_draw)
app.run()
