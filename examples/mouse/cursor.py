import random

from maliang import MouseCursors, Maliang

app = Maliang(400, 200)

cursors_count = 11
cursor_area_w = app.width/cursors_count
bg_colors = []

for i in range(cursors_count + 1):
    bg_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def on_draw():
    app.background(255)
    for i in range(cursors_count+1):
        app.rect(i * cursor_area_w, 0, (i + 1) * cursor_area_w, app.height, filled_color= bg_colors[i], stroke_width=0)
        if i * cursor_area_w < app.mouse_x < (i+1) * cursor_area_w:
            app.cursor(i)   # different cursor shapes
            app.text(str(i), i * cursor_area_w + 10, app.height / 2, font_size=30, text_color=(255,))
            app.rect(i * cursor_area_w, 0, (i + 1) * cursor_area_w, app.height, filled_color= None, stroke_width=3, stroke_color=(255, ))


app.regist_event("on_draw", on_draw)

app.run()