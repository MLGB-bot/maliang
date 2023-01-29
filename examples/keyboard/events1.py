import random

from maliang import Maliang, KeyboardKeys

app = Maliang(200, 200, buffer_proxy=True)

cursors_count = 11  # cursor shapes

background_color = (255, 255, 255)

def on_setup():
    app.background(*background_color)

def on_draw():
    if app.is_key_up(KeyboardKeys.KEY_THREE):
        app.circle(*app.mouse, 10, stroke_width=None, filled_color=(255, 0, 0, 100))

def on_key_clicked(keys):
    # print("on_key_clicked", keys)
    if KeyboardKeys.KEY_ONE in keys:
        app.background(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def on_key_released(keys):
    # print("on_key_released", keys)
    if KeyboardKeys.KEY_TWO in keys:
        app.cursor(random.randint(0, cursors_count))

def on_key_down(keys):
    # print("on_key_down", keys)
    if KeyboardKeys.KEY_THREE in keys:
        app.line(*app.pmouse, *app.mouse)

def on_char_down(char):
    print("on_char_down", char, chr(char))


app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)
# events
app.regist_event('on_key_clicked', on_key_clicked)
app.regist_event('on_key_released', on_key_released)
app.regist_event('on_key_down', on_key_down)
app.regist_event('on_char_down', on_char_down)

app.run()