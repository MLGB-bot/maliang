import random
import pyray as pr
from maliang import Maliang

def demo():
    app = Maliang(width=300, height=200, double_buffer=True, fps=1)
    app.set_trace_log_level(4)

    def on_setup():
        print("setup")
        app.smooth()
        app.rect_mode('CENTER')
        app.ellipse_mode('CENTER')
        app.circle_mode('CORNER')
        app.background(100, 100, 200, 255)
        app.line(0, 0, app.width, app.height, 1, stroke_color=pr.BLACK)
        app.stroke(pr.PINK, )
        app.line(0, app.height, app.width, 0, stroke_width=10)
        app.point(5, 5, stroke_width=5, stroke_color=pr.PINK, shape='rect')
        app.point(5, 5, stroke_width=1, stroke_color=pr.RED)

    app.regist_event('on_setup', on_setup)

    def on_draw():
        app.background(200, 200, 255, 80)
        # app.background(200, 200, 0, 255)

        pr.draw_text(f"{app.mouse_x}, {app.mouse_y}", app.mouse_x, app.mouse_y, 12, pr.BLACK)
        pr.draw_text(f"{app.delta}", 0, 0, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_frame_time()}", 0, 20, 12, pr.BLACK)
        pr.draw_text(f"{pr.get_time()}", 0, 40, 12, pr.BLACK)
        pr.draw_text(f"{app.frame_count}", 0, 60, 12, pr.BLACK)

    app.regist_event('on_draw', on_draw)

    app.loop()


if __name__ == '__main__':
    demo()