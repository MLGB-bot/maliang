import time
import random
import pyray as pr
from maliang import Maliang

app = Maliang(width=500, height=400, double_buffer=True, fps=10)
app.set_trace_log_level(4)
app.set_static_relative_dir('./resources/')

tx = app.load_texture('img.png')


print(tx.pr_texture.width)
print(tx.pr_texture.height)
# print(tx.pr_texture.format)
# print(tx.pr_texture.mipmaps)
# print(tx.pr_texture.id)
# print(dir(tx.pr_texture))

def on_setup():
    print("setup")
    # app.background(100, 0, 0, 255)
    app.stroke(pr.PINK)
    app.line(0, 0, app.width, app.height, 1, stroke_color=pr.BLACK)
    app.line(0, app.height, app.width, 0, stroke_width=10)
    app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect')
    app.point(5, 5, stroke_width=1, stroke_color=pr.RED)

    # app.tint()

app.regist_event('on_setup', on_setup)


def on_draw():
    # app.background(200, 200, 255, 50)
    app.background(255)
    # print("ondraw")
    # app.text(f"{app.mouse_x}, {app.mouse_y}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
    # app.text(f"{app.delta}", 0, 0, 12, pr.BLACK)
    # app.text(f"{pr.get_frame_time()}", 0, 20, 12, pr.BLACK)
    # app.text(f"{pr.get_time()}", 0, 40, 12, pr.BLACK)
    # app.text(f"{app.frame_count}", 0, 60, 12, pr.BLACK)

    pr.draw_texture(tx.pr_texture, 0, 0, pr.WHITE)
    app.background(255, 200)
    # pr.draw_texture_ex(tx.pr_texture, pr.Vector2(10, 10), 30, 0.5, pr.WHITE)
    # pr.draw_texture_pro(tx.pr_texture, pr.Rectangle(0, 0, tx.width, tx.height), pr.Rectangle(10, 10, 150, 260), pr.Vector2(0, 0), -30, pr.WHITE)
    # tx.draw_pro(10, 10, 150, 260, rotation=-30)
    # app.texture(tx).draw_pro(10, 10, 150, 260, rotation=-30)
    # pr.draw_texture_rec(tx.pr_texture, pr.Rectangle(100, 300, 50, 50), pr.Vector2(100, 300,), pr.WHITE)
    # app.texture(tx).draw_ex(100, 300, src_x=100, src_y=300, src_w=50, src_h=50, )
    # pr.draw_texture_quad(tx.pr_texture, pr.Vector2(10, 10), pr.Vector2(20, 10), pr.Rectangle(0, 80, app.width, 300),  pr.WHITE)
    # app.texture(tx).draw_pro(10, 10, 150, 260, rotation=0)
    # app.texture(tx).draw_tiled(10, 10, 150, 260, scale=1, rotation=0)
    # app.texture(tx).draw_quad(0, 0, app.width, 300, 10, 10, offset_x=0.1, offset_y=0.8)
    # app.texture(tx).draw_npatch(0, 0, tx.width, tx.height, 0,0,0,0, 12, 40, 12, 12, layout=0 )
    # app.texture(tx).draw_npatch(0, 0, tx.width, tx.height, 0,0,0,0, 12, 40, 12, 12, layout=0 )
    # points = [(66.22415924072266, -126.86355590820312), (-61.756343841552734, -129.0974578857422),
    #           (-127.98050689697266, -2.23390793800354), (-129.0974578857422, 61.756343841552734),
    #           (-66.22415924072266, 126.86355590820312), (-33.67055892944336, 95.4269027709961),
    #           (30.3196964263916, 96.54386138916016), (61.756343841552734, 129.0974578857422),
    #           (126.86355590820312, 66.22415924072266), (127.98050689697266, 2.23390793800354),
    #           (66.22415924072266, -126.86355590820312)]
    points = [
        (30, 30), (30, 360), (250, 300), (300, 189), (380, 50),  (30, 30)
    ]
    # points.reverse()
    app.texture(tx).draw_poly(points, )

    app.textColor( 255, 0, 0)
    app.textSize(25)
    for i, point in enumerate(points):
        print(i, point)
        app.text(str(i), *point)
    app.text('1', app.mouse_x, app.mouse_y)



app.regist_event('on_draw', on_draw)


def on_mouse_moved(*args):
    print("on_mouse_moved", args)


def on_mouse_clicked(*args):
    print("on_mouse_clicked", args)


app.regist_event('on_mouse_clicked', on_mouse_clicked)

app.loop()
tx.unload()
