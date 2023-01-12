import pyray as pr
from maliang.structs import MColor, MImage
from maliang.units.modes import WindowFlags


class Window:
    def __init__(self, width=100, height=100, title='',
                 background_color=(235, 235, 235, 255),
                 full_screen=False):

        # self.set_window_state(WindowFlags.FLAG_WINDOW_RESIZABLE)
        self.background_color = MColor(*background_color)
        self.title = title
        self.fullscreen_width = 0
        self.fullscreen_height = 0
        self.init_window(width, height, full_screen)
        self.resized = False    # is window resized

    def init_window(self, width, height, full_screen=False):
        #  way1
        if full_screen:
            pr.set_config_flags(WindowFlags.FLAG_FULLSCREEN_MODE)
            if width and height:
                pr.init_window(width, height, self.title)
                self.fullscreen_width = width
                self.fullscreen_height = height
            else:
                pr.init_window(0, 0, self.title)
                self.fullscreen_width = self.get_screen_width()
                self.fullscreen_height = self.get_screen_height()
        else:
            pr.init_window(width, height, self.title)
        while not pr.is_window_ready():
            pass

    def fullscreen(self, width=0, height=0):
        if not (width and height):
            monitor = Monitor.get_current_monitor()
            width = Monitor.get_monitor_width(monitor)
            height = Monitor.get_monitor_height(monitor)
        # self.toggle_fullscreen()  #全屏下无法正常工作
        # 顺序不能颠倒
        self.set_window_state(WindowFlags.FLAG_FULLSCREEN_MODE)
        self.resize(width, height)

        self.fullscreen_width = width
        self.fullscreen_height = height
        self.resized = True

    def un_fullscreen(self, width=0, height=0):
        self.toggle_fullscreen()
        if width and height:
            self.resize(width, height)
        self.resized = True

    def resize(self, w, h):
        # base api to resize window
        self.set_window_size(w, h)
        # need to update width and height attr in fullscreen mode
        if self.is_window_fullscreen():
            self.fullscreen_width = w
            self.fullscreen_height = h
        # Trig window resize event
        self.resized = True

    @property
    def width(self):
        """
        :return: 视窗宽度 Width of the window
        """
        return self.fullscreen_width if self.is_window_fullscreen() else self.get_screen_width()

    @property
    def height(self):
        """

        :return: 视窗高度 Width of the window
        """
        return self.fullscreen_height if self.is_window_fullscreen() else self.get_screen_height()

    def background(self, *color):
        color = MColor(*color)
        if color.a == 255:
            pr.clear_background(color.to_pyray())
        else:
            pr.draw_rectangle(0, 0, self.width, self.height, color.to_pyray())
        self.background_color = color

    @classmethod
    def window_should_close(self) -> bool:
        return pr.window_should_close()

    @classmethod
    def close_window(self):
        pr.close_window()

    @classmethod
    def is_window_ready(self) -> bool:
        return pr.is_window_ready()

    @classmethod
    def is_window_fullscreen(self) -> bool:
        return pr.is_window_fullscreen()

    @classmethod
    def is_window_hidden(self) -> bool:
        return pr.is_window_hidden()

    @classmethod
    def is_window_minimized(self) -> bool:
        return pr.is_window_minimized()

    @classmethod
    def is_window_maximized(self) -> bool:
        return pr.is_window_maximized()

    @classmethod
    def is_window_focused(self) -> bool:
        return pr.is_window_focused()

    @classmethod
    def is_window_resized(self) -> bool:
        return pr.is_window_resized()

    @classmethod
    def is_window_state(self, flag: int) -> bool:
        return pr.is_window_state(flag)

    @classmethod
    def set_window_state(self, flags: int):
        pr.set_window_state(flags)

    @classmethod
    def clear_window_state(self, flags: int):
        pr.clear_window_state(flags)

    @classmethod
    def toggle_fullscreen(self):
        pr.toggle_fullscreen()

    @classmethod
    def maximize_window(self):
        # Set window state: maximized, if resizable (only PLATFORM_DESKTOP)
        pr.maximize_window()

    @classmethod
    def minimize_window(self):
        # Set window state: minimized, if resizable (only PLATFORM_DESKTOP)
        pr.minimize_window()

    @classmethod
    def restore_window(self):
        # Set window state: not minimized/maximized (only PLATFORM_DESKTOP)
        pr.restore_window()

    @classmethod
    def set_window_icon(self, image: MImage):
        # Set icon for window (only PLATFORM_DESKTOP)
        pr.set_window_icon(image.pr_image)

    @classmethod
    def set_window_title(self, title):
        # Set title for window (only PLATFORM_DESKTOP)
        pr.set_window_title(title)

    @classmethod
    def set_window_position(self, x: int, y: int):
        # Set window position on screen (only PLATFORM_DESKTOP)
        pr.set_window_position(x, y)

    @classmethod
    def set_window_min_size(self, width: int, height: int):
        # Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)
        pr.set_window_min_size(width, height)

    @classmethod
    def set_window_size(self, width: int, height: int):
        # Set window dimensions
        pr.set_window_size(width, height)

    @classmethod
    def set_window_opacity(self, opacity: float):
        # Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)
        pr.set_window_opacity(opacity)

    @classmethod
    def get_window_handle(self):
        # Get native window handle
        handler = pr.get_window_handle()
        return handler

    @classmethod
    def get_screen_width(self) -> int:
        return pr.get_screen_width()

    @classmethod
    def get_screen_height(self) -> int:
        return pr.get_screen_height()

    @classmethod
    def get_render_width(self) -> int:
        return pr.get_render_width()

    @classmethod
    def get_render_height(self) -> int:
        return pr.get_render_height()

    @classmethod
    def get_window_position(self):
        position = pr.get_window_position()
        return position.x, position.y

    @classmethod
    def get_window_scale_dpi(self):
        scale_dpi = pr.get_window_scale_dpi()
        return scale_dpi.x, scale_dpi.y


class Monitor:
    @classmethod
    def get_monitor_count(cls) -> int:
        return pr.get_monitor_count()

    @classmethod
    def get_current_monitor(cls) -> int:
        return pr.get_current_monitor()

    @classmethod
    def set_window_monitor(cls, monitor: int):
        # Set monitor for the current window (fullscreen mode)
        pr.set_window_monitor(monitor)

    @classmethod
    def get_monitor_position(cls, monitor: int):
        position = pr.get_monitor_position(monitor)
        return position.x, position.y

    @classmethod
    def get_monitor_width(cls, monitor: int) -> int:
        return pr.get_monitor_width(monitor)

    @classmethod
    def get_monitor_height(cls, monitor: int) -> int:
        return pr.get_monitor_height(monitor)

    @classmethod
    def get_monitor_physical_width(cls, monitor: int) -> int:
        return pr.get_monitor_physical_width(monitor)

    @classmethod
    def get_monitor_physical_height(cls, monitor: int) -> int:
        return pr.get_monitor_physical_height(monitor)

    @classmethod
    def get_monitor_refresh_rate(cls, monitor: int) -> int:
        return pr.get_monitor_refresh_rate(monitor)

    @classmethod
    def get_monitor_name(cls, monitor: int):
        return pr.get_monitor_name(monitor)
