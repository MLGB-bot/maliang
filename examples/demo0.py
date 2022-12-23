import time


import pyray as pr
from maliang import Maliang

def demo():
    import random
    app = Maliang(width=300, height=200, double_buffer=False, fps=10)
    app.set_trace_log_level(4)
    app.set_static_relative_dir('../learn')
    img1  = None
    # img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=3, color2=(0, 0, 250, ), density=0.6)
    # img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=4, color2=(0, 0, 250, ), density=0.6)
    # img1 = app.create_image(100, 100, color=(255, 255, 100, 100), style=6, color2=(0, 0, 250, ), density=0.6)
    # img2 = app.load_image('blue.png')
    # img3 = app.load_image('img.png')

    # img1.release()
    # img2.release()
    # return

    def on_setup():
        nonlocal img1
        print("setup")
        # app.smooth()
        # app.rect_mode('CENTER')
        # app.ellipse_mode('CENTER')
        # app.circle_mode('CORNER')
        # app.background(100, 0, 0, 255)
        # app.line(0, 0, app.width, app.height, 1, stroke_color=pr.BLACK)
        # app.stroke(pr.PINK, )
        # app.line(0, app.height, app.width, 0, stroke_width=10)
        # #
        app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect')
        app.point(5, 5, stroke_width=1, stroke_color=pr.RED)
        # app.circle(int(app.width / 2), int(app.height / 2), 10, stroke_width=1, stroke_color=pr.RED)
        # # app.no_fill()
        # app.ellipse(int(app.width / 2), int(app.height / 2), 20, 10, stroke_width=1, stroke_color=pr.RED, )
        # app.ring(int(app.width / 2), int(app.height / 2), 80, 60, stroke_width=1, stroke_color=pr.RED, )
        # app.ring(int(app.width / 2), int(app.height / 2), 40, 45, stroke_width=1, stroke_color=pr.RED, )
        # app.triangle(0, 0, int(app.width / 2), int(app.height / 2), 40, app.height-10, stroke_width=2, stroke_color=pr.RED, )
        # # app.poly(int(app.width / 2), int(app.height / 2), r=50, sides=6, stroke_width=1, stroke_color=pr.RED, )
        # # app.ray(10, int(app.height / 2), 10, 20, stroke_color=pr.RED, )
        # pr.draw_text('i', int(app.width / 2), int(app.height / 2), 12,pr.BLACK)
        # app.arc(int(app.width / 2), int(app.height / 2), 50, 50, 0, 90)
        # # app.push_matrix()
        # app.rect(0, 0, 20, 20, filled_color=pr.LIGHTGRAY)
        # # app.transtate(10, 10)
        # # app.rotate(45)
        # app.rect(0, 0, 20, 20, filled_color=pr.LIGHTGRAY)
        # # app.rotate(-30)
        # # app.rect(0, 0, 20, 20, filled_color=pr.DARKGRAY)
        # # app.rotate(20)
        # # app.scale(0.5, 2)
        # # # app.scale(1, 0.5)
        # app.rect(0, 0, 20, 20, filled_color=pr.BLACK)
        #
        # # app.ellipse(int(app.width / 2), int(app.height / 2), 50, 50, stroke_width=1, stroke_color=pr.RED, )
        # app.circle(int(app.width / 2), int(app.height / 2), 50, stroke_width=1, stroke_color=pr.RED, )

        # app.begin_shape(0)
        # app.vertex(1, 1)
        # app.vertex(21, 50)
        # app.vertex(10, 51)
        # app.vertex(71, 11)
        # app.vertex(91, 50)
        # app.vertex(25, 98)
        # app.end_shape()
        # app.shapedemo()
        # app.circle(int(app.width / 2), int(app.height / 2), 50, stroke_width=1, stroke_color=pr.RED, )
        # app.no_cursor()
        # app.cursor(5)
        # app.mouse_position(50, 50)
        # app.mouse_scale(2, 2)
        # app.mouse_offset(10, 10)
        # img1 = app.load_screen()

    # app.regist_event('on_setup', on_setup)

    def on_draw():
        nonlocal img1
        app.background(200, 200, 255, 50)
        # app.background(200, 200, 0, 255)
        # print("ondraw")
        # if img1:
        #     # print("image")
        #     app.image(img1, 0, 0)
        #     app.background(255, 255, 255, 5)
        # else:
        #     app.background(255, 255, 255, 255)
        #
        # pr.draw_text(f"{app.mouse}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
        pr.draw_text(f"{app.mouse_x}, {app.mouse_y}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
        # pr.draw_text(f"{app.pmouse_x}, {app.pmouse_y}", 0, 20, 12, pr.BLACK)
        pr.draw_text(f"{app.delta}", 0, 0, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_frame_time()}", 0, 20, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_time()}", 0, 40, 12, pr.BLACK)
        pr.draw_text(f"{app.frame_count}", 0, 60, 12, pr.BLACK)
        # pr.draw_text(f"{app.mouse_x},{app.mouse_y}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
        # app.point(random.randint(0, app.width),
        #               random.randint(0, app.height),
        #               stroke_width=5,
        #               stroke_color=pr.BLACK
        #              )
        app.line(0.1, 0.1, app.width-10.4, app.height-10.7, 1, stroke_color=pr.BLACK)
        app.line(0.1, 0.1, app.width-10.4, app.height-10.7, stroke_width=0, stroke_color=pr.BLACK, )
        # app.stroke(pr.PINK, )
        # app.line(0, app.height, app.width, 0, stroke_width=10)
        #
        # app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect' )
        # app.point(5, 5, stroke_width=1, stroke_color=pr.RED )
        # app.circle( int(app.width/2), int(app.height/2), r=10, stroke_width=1, stroke_color=pr.RED )
        # # app.no_fill()
        # app.ellipse( int(app.width/2), int(app.height/2), 20, 10, stroke_width=1, stroke_color=pr.RED, )
        # app.image(img1, 0, 0)
        # app.image(img2, 50, 10, 30, 60)
        # app.no_tint()
        # app.image(img3, 0, 0)
        # app.tint(0, 153, 204)
        # app.image(img3, 50, 0)

    #     app.background(127)
    #     app.no_stroke()
    #     for i in range(0, app.height, 20):
    #         app.fill(129, 206, 15)
    #         app.rect(0, i, app.width, 10)
    #         app.fill(255)
    #         app.rect(i, 0, 10, app.height)

    app.regist_event('on_draw', on_draw)

    def on_mouse_moved(*args):
        print("on_mouse_moved", args)

    def on_mouse_pressed(*args):
        print("on_mouse_pressed", args)

    def on_mouse_released(*args):
        print("on_mouse_released", args)

    def on_mouse_clicked(*args):
        print("on_mouse_clicked", args)
        nonlocal img1
        # img1 = app.load_screen()
        # print(img1.pr_img)
        app.no_fill()
        app.circle(app.mouse_x, app.mouse_y, 20.5, stroke_color=pr.RED)

    def on_mouse_wheel(*args):
        print("on_mouse_wheel", args)

    def on_mouse_dragged(*args):
        print("on_mouse_dragged", args)

    def on_mouse_double_clicked(*args):
        print("on_mouse_double_clicked", args)

    # app.regist_event('on_mouse_moved', on_mouse_moved)
    # app.regist_event('on_mouse_pressed', on_mouse_pressed)
    # app.regist_event('on_mouse_released', on_mouse_released)
    app.regist_event('on_mouse_clicked', on_mouse_clicked)
    # app.regist_event('on_mouse_wheel', on_mouse_wheel)
    # app.regist_event('on_mouse_dragged', on_mouse_dragged)
    app.regist_event('on_mouse_double_clicked', on_mouse_double_clicked)

    def on_key_pressed(*args):
        print("on_key_pressed", args)


    def on_char_pressed(*args):
        print("on_char_pressed", args)

    def on_key_clicked(*args):
        print("on_key_clicked", args)

    def on_key_released(*args):
        print("on_key_released", args)

    # app.regist_event('on_key_clicked', on_key_clicked)
    # app.regist_event('on_key_released', on_key_released)
    # app.regist_event('on_key_pressed', on_key_pressed)
    app.regist_event('on_char_pressed', on_char_pressed)
    app.loop()


if __name__ == '__main__':
    demo()