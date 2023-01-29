import random

from maliang import Maliang, KeyboardKeys

app = Maliang(200, 200, buffer_proxy=True)

cursors_count = 11  # cursor shapes

background_color = (255, 255, 255)
circle_size = 10

def on_setup():
    app.background(*background_color)

def on_draw():
    global circle_size
    if app.is_key_clicked(KeyboardKeys.KEY_ONE):
        app.background(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if app.is_key_released(KeyboardKeys.KEY_TWO):
        app.cursor(random.randint(0, cursors_count))
    if app.is_key_up(KeyboardKeys.KEY_THREE):
        app.circle(*app.mouse, circle_size, stroke_width=None, filled_color=(255, 0, 0, 100))
    elif app.is_key_down(KeyboardKeys.KEY_THREE):
        app.line(*app.pmouse, *app.mouse)

app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)

app.run()