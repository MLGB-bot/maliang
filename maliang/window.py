import pyray as pr
from maliang.structs import MColor, MImage
from maliang.units.modes import WindowFlags

class Window():
    def __init__(self, width=100, height=100, title='',
                 background_color=(235, 235, 235, 255),
                 full_screen=False):

        # self.set_window_state(WindowFlags.FLAG_WINDOW_RESIZABLE)
        self.background_color = tuple(MColor(*background_color))
        self.title = title
        self.init_window(width, height, full_screen)

    def init_window(self, width, height, full_screen=False):
        pr.init_window(width, height, self.title)
        while not pr.is_window_ready():
            pass
        if full_screen:
            self.full_screen()

    @property
    def width(self):
        if self.is_window_fullscreen():
            return self.get_monitor_width(self.get_current_monitor())
        return self.get_screen_width()

    @property
    def height(self):
        if self.is_window_fullscreen():
            return self.get_monitor_height(self.get_current_monitor())
        return self.get_screen_height()

    def background(self, *color):
        color = MColor(*color)
        if color.a == 255:
            pr.clear_background(color.to_pyray())
        else:
            pr.draw_rectangle(0, 0, self.width, self.height, color.to_pyray())
        self.background_color = tuple(color)

    def window_should_close(self) -> bool:
        return pr.window_should_close()

    def close_window(self):
        pr.close_window()

    def is_window_ready(self) -> bool:
        return pr.is_window_ready()

    def is_window_fullscreen(self) -> bool:
        return pr.is_window_fullscreen()

    def is_window_hidden(self) -> bool:
        return pr.is_window_hidden()

    def is_window_minimized(self) -> bool:
        return pr.is_window_minimized()

    def is_window_maximized(self) -> bool:
        return pr.is_window_maximized()

    def is_window_focused(self) -> bool:
        return pr.is_window_focused()

    def is_window_resized(self) -> bool:
        return pr.is_window_resized()

    def is_window_state(self, flag: int) -> bool:
        return pr.is_window_state(flag)

    def set_window_state(self, flags: int):
        pr.set_window_state(flags)

    def clear_window_state(self, flags: int):
        pr.clear_window_state(flags)

    def toggle_fullscreen(self):
        pr.toggle_fullscreen()

    def maximize_window(self):
        # Set window state: maximized, if resizable (only PLATFORM_DESKTOP)
        pr.maximize_window()

    def minimize_window(self):
        # Set window state: minimized, if resizable (only PLATFORM_DESKTOP)
        pr.minimize_window()

    def restore_window(self):
        # Set window state: not minimized/maximized (only PLATFORM_DESKTOP)
        pr.restore_window()

    def set_window_icon(self, image: MImage):
        # Set icon for window (only PLATFORM_DESKTOP)
        pr.set_window_icon(image.pr_image)

    def set_window_title(self, title):
        # Set title for window (only PLATFORM_DESKTOP)
        pr.set_window_title(title)

    def set_window_position(self, x: int, y: int):
        # Set window position on screen (only PLATFORM_DESKTOP)
        pr.set_window_position(x, y)

    def set_window_min_size(self, width: int, height: int):
        # Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)
        pr.set_window_min_size(width, height)

    def set_window_size(self, width: int, height: int):
        # Set window dimensions
        pr.set_window_size(width, height)

    def set_window_opacity(self, opacity: float):
        # Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)
        pr.set_window_opacity(opacity)

    def get_window_handle(self):
        # Get native window handle
        handler = pr.get_window_handle()
        return handler

    def get_screen_width(self) -> int:
        return pr.get_screen_width()

    def get_screen_height(self) -> int:
        return pr.get_screen_height()

    def get_render_width(self) -> int:
        return pr.get_render_width()

    def get_render_height(self) -> int:
        return pr.get_render_height()

    def get_window_position(self):
        position = pr.get_window_position()
        return position.x, position.y

    def get_window_scale_dpi(self):
        scale_dpi = pr.get_window_scale_dpi()
        return scale_dpi.x, scale_dpi.y

    def get_monitor_count(self) -> int:
        return pr.get_monitor_count()

    def get_current_monitor(self) -> int:
        return pr.get_current_monitor()

    def set_window_monitor(self, monitor: int):
        # Set monitor for the current window (fullscreen mode)
        pr.set_window_monitor(monitor)

    def get_monotor_position(self, monitor: int):
        position = pr.get_monitor_position(monitor)
        return position.x, position.y

    def get_monitor_width(self, monitor: int) -> int:
        return pr.get_monitor_width(monitor)

    def get_monitor_height(self, monitor: int) -> int:
        return pr.get_monitor_height(monitor)

    def get_monitor_physical_width(self, monitor: int) -> int:
        return pr.get_monitor_physical_width(monitor)

    def get_monitor_physical_height(self, monitor: int) -> int:
        return pr.get_monitor_physical_height(monitor)

    def get_monitor_refresh_rate(self, monitor: int) -> int:
        return pr.get_monitor_refresh_rate(monitor)

    def get_monitor_name(self, monitor: int):
        return pr.get_monitor_name(monitor)

    def full_screen(self, monitor=None):
        if monitor == None:
            monitor = self.get_current_monitor()
        monitor_width = self.get_monitor_width(monitor)
        monitor_height = self.get_monitor_height(monitor)
        self.set_window_state(WindowFlags.FLAG_FULLSCREEN_MODE)
        self.size(monitor_width, monitor_height)

    def unfull_screen(self, flag=None):
        if flag is None:
            flag = WindowFlags.FLAG_VSYNC_HINT
        self.set_window_state(flag)

    def size(self, x, y):
        pr.set_window_size(x, y)
