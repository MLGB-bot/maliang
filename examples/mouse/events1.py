import random

from maliang import Maliang, MouseButtons, MouseCursors

app = Maliang(200, 200, buffer_proxy=True)

cursors_count = 11  # cursor shapes

background_color = (255, 255, 255)
circle_size = 10

def on_setup():
    app.background(*background_color)
    app.double_click_gap = 0.3  # 300ms

def on_draw():
    pass

def on_mouse_clicked(btns):
    # print("on_mouse_clicked", btns)
    if MouseButtons.MOUSE_BUTTON_LEFT in btns:
        app.background(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def on_mouse_released(btns):
    # print("on_mouse_released", btns)
    if MouseButtons.MOUSE_BUTTON_LEFT in btns:
        app.cursor(random.randint(0, cursors_count))

def on_mouse_down(btns):
    # print("on_mouse_down", btns)
    if MouseButtons.MOUSE_BUTTON_LEFT in btns:
        app.line(*app.pmouse, *app.mouse)

def on_mouse_moved(vector):
    # print("on_mouse_moved", vector)
    if app.is_mouse_up(MouseButtons.MOUSE_BUTTON_LEFT):
        app.circle(*app.mouse, circle_size, stroke_width=None, filled_color=(255, 0, 0, 100))

def on_mouse_wheel(val):
    # print("on_mouse_wheel", val)
    global circle_size
    circle_size += val
    if circle_size < 1:
        circle_size = 1

def on_mouse_dragged(value):
    btns, vector = value
    print("on_mouse_dragged", btns, vector)

def on_mouse_double_clicked():
    print("on_mouse_double_clicked")
    app.exit()

app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)
# events
app.regist_event('on_mouse_clicked', on_mouse_clicked)
app.regist_event('on_mouse_released', on_mouse_released)
app.regist_event('on_mouse_down', on_mouse_down)
app.regist_event('on_mouse_moved', on_mouse_moved)
app.regist_event('on_mouse_wheel', on_mouse_wheel)
app.regist_event('on_mouse_dragged', on_mouse_dragged)
app.regist_event('on_mouse_double_clicked', on_mouse_double_clicked)

app.run()