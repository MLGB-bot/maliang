from maliang import Maliang

app = Maliang()

def on_draw():
    app.background(255)
    app.line_bezier_quad(0, 0, 100, 100, app.mouse_x, app.mouse_y)
    app.point(app.mouse_x, app.mouse_y, stroke_width=5, stroke_color=(255, 0, 0))

app.regist_event('on_draw', on_draw)
app.run()