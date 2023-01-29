import random

from maliang import Maliang, MouseButtons, MouseCursors

app = Maliang(200, 200, buffer_proxy=True)

cursors_count = 11  # cursor shapes

background_color = (255, 255, 255)
circle_size = 10

def on_setup():
    app.background(*background_color)

def on_draw():
    global circle_size
    if app.is_mouse_clicked(MouseButtons.MOUSE_BUTTON_LEFT):
        app.background(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif app.is_mouse_released(MouseButtons.MOUSE_BUTTON_LEFT):
        app.cursor(random.randint(0, cursors_count))
    if app.is_mouse_up(MouseButtons.MOUSE_BUTTON_LEFT):
        app.circle(*app.mouse, circle_size, stroke_width=None, filled_color=(255, 0, 0, 100))
    elif app.is_mouse_down(MouseButtons.MOUSE_BUTTON_LEFT):
        app.line(*app.pmouse, *app.mouse)

    mouse_wheel = app.is_mouse_wheel()
    if mouse_wheel:
        circle_size += mouse_wheel
        if circle_size < 1:
            circle_size = 1

app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)

app.run()