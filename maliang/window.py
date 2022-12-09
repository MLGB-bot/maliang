import pyray as pr
from maliang.structs import MColor
from maliang.environment import Environment
from maliang.shapes2d import Shapes2d
from maliang.transform import Transform
from maliang.mouse import Mouse
from maliang.keyboard import Keyboard
from maliang.events import Events
from maliang.image import Image


class Window(Environment, Shapes2d, Transform, Events, Mouse, Keyboard, Image):
    def __init__(self, width=100, height=100, title='', fps=60,
                 background_color=(235, 235, 235, 255), double_buffer=True):
        Environment.__init__(self, width, height)
        Shapes2d.__init__(self)
        Transform.__init__(self)
        Events.__init__(self)
        Mouse.__init__(self)
        Keyboard.__init__(self)
        Image.__init__(self)

        self.frame_count = 0
        self.double_buffer = double_buffer
        self.background_color = tuple(MColor(*background_color))
        self.title = title
        self.init_fps(fps)
        self.init_window()

        while not pr.is_window_ready():
            pass
        self.buffer_texture = self.load_render_texture()


    def init_fps(self, fps):
        if fps:
            self.fps = fps
            pr.set_target_fps(fps)

    def init_window(self):
        return pr.init_window(self.width, self.height, self.title)

    def load_render_texture(self):
        return pr.load_render_texture(self.width, self.height)

    def unload_render_texture(self):
        if self.buffer_texture:
            pr.unload_render_texture(self.buffer_texture)

    def background(self, *color):
        color = MColor(*color)
        pr.draw_rectangle(0, 0, self.width, self.height, color.to_pyray())

    def on_setup(self):
        pass

    def on_draw(self, ):
        pass

    @staticmethod
    def decorate_by_buffer_value(func):
        def inner(self, *args, **kwargs):
            if self.buffer_texture:
                pr.begin_texture_mode(self.buffer_texture)
                func(self, *args, **kwargs)
                pr.end_texture_mode()
                pr.begin_drawing()
                pr.clear_background(pr.WHITE)
                pr.draw_texture_pro(self.buffer_texture.texture,
                                    pr.Rectangle(0, 0, self.width, -self.height),
                                    pr.Rectangle(0, 0, self.width, self.height),
                                    pr.Vector2(0, 0),
                                    0,
                                    pr.WHITE
                                    )
                pr.end_drawing()
                # single buffer switch to double buffer
                if self.double_buffer and self.frame_count == 2:
                    self.unload_render_texture()
                    self.buffer_texture = None
            else:
                pr.begin_drawing()
                func(self, *args, **kwargs)
                pr.end_drawing()
        return inner

    @decorate_by_buffer_value
    def _on_setup(self):
        # 执行setup中的操作
        self.on_setup()

    @decorate_by_buffer_value
    def _on_draw(self):
        self.on_draw()
        if hasattr(self, 'events_registed') and self.events_registed:
            if hasattr(self, 'keyboard_watcher'):
                self.keyboard_watcher()
            if hasattr(self, 'catpure_events'):
                self.catpure_events()

        self.frame_count += 1

    def on_exit(self):
        self.unload_render_texture()
        pr.close_window()

    def loop(self):
        self._on_setup()
        while not pr.window_should_close():
            self._on_draw()
            self.release_matrix()
        self.on_exit()