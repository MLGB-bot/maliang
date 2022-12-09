import time
import random
import pyray as pr
from maliang import Maliang

app = Maliang(width=300, height=200, double_buffer=True, fps=10)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

img1  = None
# img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=3, color2=(0, 0, 250, ), density=0.6)
# img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=4, color2=(0, 0, 250, ), density=0.6)
# img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=6, color2=(0, 0, 250, ), density=0.6)
# img2 = app.load_image('blue.png')
# img3 = app.load_image('img.png')

with open('./resources/img.png', 'rb') as f:
    img_data = f.read()

app.stroke(pr.PINK)
img2 = app.load_image_data(data=img_data, filetype='.png')
# img2 = app.from_text("Hello World", fontsize=12)

colors = img2.load_colors()
print(11111, colors, tuple(colors))

colors2 = img2.load_palette(128, 32)
print(222, colors2, tuple(colors2))

# exit(0)
# img2.export_to_file("../learn/test0.png", mode=0)
# img2.export_to_file("../learn/test1.png", mode=1)

# img3 = app.load_image('test1.png')

# with open('../learn/test1.png', 'rb') as f:
#     img_data = f.read()
# print(img_data)
# img1.release()
# img2.release()
# return

def on_setup():
    global img1
    print("setup")
    # app.background(100, 0, 0, 255)
    app.line(0, 0, app.width, app.height, 1, stroke_color=pr.BLACK)
    # app.stroke(pr.PINK, )
    app.line(0, app.height, app.width, 0, stroke_width=10)
    app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect')
    app.point(5, 5, stroke_width=1, stroke_color=pr.RED)

    # app.tint()
app.regist_event('on_setup', on_setup)

def on_draw():
    app.background(200, 200, 255, 50)
    # app.background(200, 200, 0, 255)
    # print("ondraw")
    if img1:
        # print("image")
        app.image(img1, 0, 0)
        app.background(255, 255, 255, 5)
    else:
        app.background(255, 255, 255, 255)
        pr.draw_text(f"{app.mouse_x}, {app.mouse_y}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
        pr.draw_text(f"{app.delta}", 0, 0, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_frame_time()}", 0, 20, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_time()}", 0, 40, 12, pr.BLACK)
        pr.draw_text(f"{app.frame_count}", 0, 60, 12, pr.BLACK)
    app.image(img2, 100, 50, )
    app.image(img2, 100, 80, )

app.regist_event('on_draw', on_draw)

def on_mouse_moved(*args):
    print("on_mouse_moved", args)

def on_mouse_clicked(*args):
    print("on_mouse_clicked", args)
    global img1
    img1 = app.load_screen()
    # print(img1.pr_img)

app.regist_event('on_mouse_clicked', on_mouse_clicked)

app.loop()
