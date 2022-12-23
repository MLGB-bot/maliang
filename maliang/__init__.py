import pyray as pr
from maliang.structs import MColor
from maliang.window import Window
from maliang.camera import Camera
from maliang.environment import Environment
from maliang.shapes2d import Shapes2d
from maliang.shapes3d import Shapes3d
from maliang.transform import Transform
from maliang.mouse import Mouse
from maliang.model import Model
from maliang.mesh import Mesh
from maliang.material import Material
from maliang.keyboard import Keyboard
from maliang.ray import Ray
from maliang.shader import Shader
from maliang.events import Events
from maliang.image import Image
from maliang.font import Font
from maliang.text import Text
from maliang.texture import Texture
from maliang.units import ResourceLoader


class Maliang(Window, Environment, Shapes2d, Shapes3d, Transform, Events, Mouse, Keyboard,
                Model, Mesh, Material, Ray, Shader, Image, Font, Text, Texture, Camera):
    def __init__(self, width=100, height=100, title='', double_buffer=True, fps=None,
                 background_color=(235, 235, 235, 255), ):
        Environment.__init__(self, fps=fps)
        Shapes2d.__init__(self)
        Shapes3d.__init__(self)
        Transform.__init__(self)
        Events.__init__(self)
        Mouse.__init__(self)
        Keyboard.__init__(self)
        Image.__init__(self)
        Font.__init__(self)
        Text.__init__(self)
        Texture.__init__(self)
        Camera.__init__(self)
        Model.__init__(self)
        Mesh.__init__(self)
        Material.__init__(self)
        Ray.__init__(self)
        Shader.__init__(self)
        Window.__init__(self, width=width, height=height, title=title, background_color=background_color)
        self.frame_count = 0
        self.double_buffer = double_buffer
        self.buffer_texture = self.load_render_texture()

    def load_render_texture(self):
        return pr.load_render_texture(self.width, self.height)

    def unload_render_texture(self):
        if self.buffer_texture:
            pr.unload_render_texture(self.buffer_texture)

    def set_static_relative_dir(self, relative_dir):
        return ResourceLoader.set_static_relative_dir(relative_dir)

    def set_static_absolute_dir(self, absolute_dir):
        return ResourceLoader.set_static_absolute_dir(absolute_dir)

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
                if self.double_buffer and self.frame_count % 2 == 0:
                    self.unload_render_texture()
                    self.buffer_texture = None
            else:
                pr.begin_drawing()
                func(self, *args, **kwargs)
                pr.end_drawing()
        return inner

    def on_setup(self):
        pass

    def on_draw(self, ):
        pass

    @decorate_by_buffer_value
    def _on_setup(self):
        self.background(*self.background_color) # setup defaule background color
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

    def on_lastframe_resize(self):
        # on window resize
        if self.is_window_resized():
            if self.buffer_texture:
                new_buffer_texture = self.load_render_texture()  # create new sized buffer texture
                # copy old texture to new resized texture
                pr.begin_texture_mode(new_buffer_texture)
                self.background(*self.background_color)
                pr.draw_texture_pro(
                    self.buffer_texture.texture,
                    pr.Rectangle(0, 0, self.buffer_texture.texture.width, -self.buffer_texture.texture.height),
                    pr.Rectangle(0, 0, self.buffer_texture.texture.width, self.buffer_texture.texture.height),
                    pr.Vector2(0, 0),
                    0,
                    pr.WHITE
                )
                pr.end_texture_mode()
                self.unload_render_texture()
                self.buffer_texture = new_buffer_texture

    def loop(self):
        self._on_setup()
        while not pr.window_should_close():
            self.on_lastframe_resize()
            self._on_draw()
            self.release_matrix()
            # done: auto clean fonts created in runtime
            ResourceLoader.task_unload_fonts_runtime()
        self.on_exit()

    def run(self):
        self.loop()
