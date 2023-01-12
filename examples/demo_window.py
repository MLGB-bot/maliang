from maliang import Maliang, WindowFlags, RectMode, KeyboardKeys
import pyray as pr



# app = Maliang(1920, 1080, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=True)
# app = Maliang(400, 300, "MaLiang", double_buffer=False, fps=30, background_color=(255, 255, 255), full_screen=True)
# app = Maliang(800, 600, "MaLiang", double_buffer=False, fps=30, background_color=(255, 255, 255), full_screen=False)
# app = Maliang(1024, 768, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=True)
# app = Maliang(1280, 960, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=True)
# app = Maliang(1600, 900, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=True)
app = Maliang(1920, 1080, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=True)
# app = Maliang(1920, 1080, "MaLiang", double_buffer=True, fps=30, background_color=(255, 255, 255), full_screen=False)

app.set_window_state(WindowFlags.FLAG_WINDOW_RESIZABLE)

def on_setup():
    app.background(255, )
    # print(app.width, app.height)
    app.text(str(app.width), 0, 0, text_size=18)
    app.text(str(app.height), 0, 20, text_size=18)
    # app.no_cursor()
    app.rect_mode(RectMode.CENTER)

def on_draw():
    # print(app.width, app.height)
    app.background(235)
    # pr.clear_background(pr.BLANK)
    app.line(0, 0, app.width, app.height, stroke_color=(0, 0, 0, 100))
    app.line(0, app.height, app.width, 0, stroke_color=(0, 0, 0, 100))
    app.text(str(app.width), 0, 0, text_size=18)
    app.text(str(app.height), 0, 20, text_size=18)
    app.text(str(app.get_screen_width()), 0, 40, text_size=18)
    app.text(str(app.get_screen_height()), 0, 60, text_size=18)
    try:
        render_w = app.get_render_width()
    except:
        render_w = '-'
    try:
        render_h = app.get_render_height()
    except:
        render_h = '-'
    app.text(str(render_w), 0, 80, text_size=18)
    app.text(str(render_h), 0, 100, text_size=18)

    app.text(str(app.get_window_position()), 0, 120, text_size=18)


    app.rect(app.mouse_x, app.mouse_y, 10, 10, filled_color=(255, 0, 0, 100), stoke_width=0)
    app.circle(app.width/2, app.height/2, 10, filled_color=(255, 0, 0, 100), stoke_width=0)
    app.text(f"{app.mouse_x}, {app.mouse_y}", app.width/2, app.height/2)


    if app.is_mouse_clicked():
        if app.is_window_fullscreen():
            app.un_fullscreen()
        else:
            # app.fullscreen(1600, 900)
            # app.fullscreen(1024, 768)
            # app.fullscreen(0, 0)
            app.fullscreen(app.width, app.height)

    if app.is_mouse_clicked(1):
        app.set_window_position(app.mouse_x, app.mouse_y)
    if app.is_mouse_clicked(2):
        app.set_window_position(0, 0)

    if app.is_key_clicked(KeyboardKeys.KEY_ONE):
        app.resize(1024, 768)
    elif app.is_key_clicked(KeyboardKeys.KEY_TWO):
        app.resize(1280, 960)
    elif app.is_key_clicked(KeyboardKeys.KEY_THREE):
        app.resize(1600, 900)
    elif app.is_key_clicked(KeyboardKeys.KEY_FOUR):
        # app.resize(1920, 1080, fullscreen_force_from_window=True)
        app.resize(1920, 1080)

app.regist_event("on_setup", on_setup)
app.regist_event("on_draw", on_draw)

app.run()
