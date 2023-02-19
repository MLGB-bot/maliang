import pyray as pr
import raylib as rl
from maliang.structs import MColor, MImage
from maliang.units.modes import WindowFlags


class Window:
    def __init__(self, width=100, height=100, title='',
                 background_color=(235, 235, 235, 255),
                 fullscreen=False):

        # self.set_window_state(WindowFlags.FLAG_WINDOW_RESIZABLE)
        self.background_color = MColor(*background_color)
        self.title = title
        self.fullscreen_width = 0
        self.fullscreen_height = 0
        self.init_window(width, height, fullscreen)
        self.resized = False  # is window resized

    def init_window(self, width, height, fullscreen: bool = False):
        """
        create a window in the begining of program

        :param width: window width
        :param height: window height
        :param fullscreen: whether window is fullscreen
        :return: None
        """
        if fullscreen:
            rl.SetConfigFlags(WindowFlags.FLAG_FULLSCREEN_MODE)
            if width and height:
                pr.init_window(width, height, self.title)
                self.fullscreen_width = width
                self.fullscreen_height = height
            else:
                pr.init_window(0, 0, self.title)
                monitor = self.get_current_monitor()
                self.fullscreen_width = self.get_monitor_width(monitor)
                self.fullscreen_height = self.get_monitor_height(monitor)
        else:
            pr.init_window(width, height, self.title)
        while not Window.is_window_ready():
            pass

    def fullscreen(self, width=0, height=0):
        """

        set window fullscreen

        :param width: fullscreen window width
        :param height: fullscreen window height
        :return:
        """
        if not (width and height):
            monitor = self.get_current_monitor()
            width = self.get_monitor_width(monitor)
            height = self.get_monitor_height(monitor)
        self.toggle_fullscreen()
        self.resize(width, height)
        # # 顺序不能颠倒
        # self.set_window_state(WindowFlags.FLAG_FULLSCREEN_MODE)
        # self.resize(width, height)
        self.fullscreen_width = width
        self.fullscreen_height = height
        self.resized = True

    def un_fullscreen(self, width=0, height=0):
        """

        from fullscreen to window

        :param width: window width
        :param height: window height
        :return:
        """
        self.toggle_fullscreen()
        if width and height:
            self.resize(width, height)
        self.resized = True

    def resize(self, width, height):
        """
        reset window size to (width, height)

        :param width:
        :param height:
        :return:
        """
        self.set_window_size(width, height)
        if self.is_window_fullscreen():
            self.fullscreen_width = width
            self.fullscreen_height = height
        # Trig window on_resize event
        self.resized = True

    @property
    def width(self):
        """
        :return: Width of the window
        """
        return self.fullscreen_width if self.is_window_fullscreen() else self.get_screen_width()

    @property
    def height(self):
        """

        :return: Width of the window
        """
        return self.fullscreen_height if self.is_window_fullscreen() else self.get_screen_height()

    def background(self, *color):
        """
        set window background color( RGBA Mode).

        :param color:
            background(i)          #  (i, i, i, 255) \n
            background(i, a)       #  (i, i, i, a) \n
            background(r, g, b)    #  (r, g, b, 255) \n
            background(r, g, b, a) #  (r, g, b, a) \n
        :return:
        """
        color = MColor(*color)
        if color.a == 255:
            rl.ClearBackground(color.to_pyray())
        else:
            rl.DrawRectangle(0, 0, self.width, self.height, color.to_pyray())
        self.background_color = color

    @classmethod
    def window_should_close(self) -> bool:
        """Check if <ExitKey> pressed or Close icon pressed """
        return rl.WindowShouldClose()

    @classmethod
    def close_window(self):
        """Close window and unload OpenGL context"""
        rl.CloseWindow()

    @classmethod
    def is_window_ready(self) -> bool:
        """Check if window has been initialized successfully"""
        return rl.IsWindowReady()

    @classmethod
    def is_window_fullscreen(self) -> bool:
        """Check if window is currently fullscreen"""
        return rl.IsWindowFullscreen()

    @classmethod
    def is_window_hidden(self) -> bool:
        """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
        return rl.IsWindowHidden()

    @classmethod
    def is_window_minimized(self) -> bool:
        """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
        return rl.IsWindowMinimized()

    @classmethod
    def is_window_maximized(self) -> bool:
        """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
        return rl.IsWindowMaximized()

    @classmethod
    def is_window_focused(self) -> bool:
        """Check if window is currently focused (only PLATFORM_DESKTOP)"""
        return rl.IsWindowFocused()

    @classmethod
    def is_window_resized(self) -> bool:
        """Check if window has been resized last frame"""
        return rl.IsWindowResized()

    @classmethod
    def is_window_state(self, flag: int) -> bool:
        """Check if one specific window flag is enabled"""
        return rl.IsWindowState(flag)

    @classmethod
    def set_window_state(self, flags: int):
        """Set window configuration state using flags (only PLATFORM_DESKTOP)"""
        rl.SetWindowState(flags)

    @classmethod
    def clear_window_state(self, flags: int):
        """Clear window configuration state flags"""
        rl.ClearWindowState(flags)

    @classmethod
    def toggle_fullscreen(self):
        """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
        rl.ToggleFullscreen()

    @classmethod
    def maximize_window(self):
        """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
        rl.MaximizeWindow()

    @classmethod
    def minimize_window(self):
        """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
        rl.MinimizeWindow()

    @classmethod
    def restore_window(self):
        """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
        rl.RestoreWindow()

    @classmethod
    def set_window_icon(self, image: MImage):
        """Set icon for window (only PLATFORM_DESKTOP)"""
        rl.SetWindowIcon(image.pr_image)

    @classmethod
    def set_window_title(self, title):
        """Set title for window (only PLATFORM_DESKTOP)"""
        # rl.SetWindowTitle(title)
        pr.set_window_title(title)

    @classmethod
    def set_window_position(self, x: int, y: int):
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        rl.SetWindowPosition(x, y)

    @classmethod
    def set_window_min_size(self, width: int, height: int):
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        rl.SetWindowMinSize(width, height)

    @classmethod
    def set_window_size(self, width: int, height: int):
        """Set window dimensions"""
        rl.SetWindowSize(width, height)

    @classmethod
    def set_window_opacity(self, opacity: float):
        """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
        rl.SetWindowOpacity(opacity)

    @classmethod
    def get_window_handle(self):
        """Get native window handle"""
        handler = rl.GetWindowHandle()
        return handler

    @classmethod
    def get_screen_width(self) -> int:
        """Get current screen width"""
        return rl.GetScreenWidth()

    @classmethod
    def get_screen_height(self) -> int:
        """Get current screen height"""
        return rl.GetScreenHeight()

    @classmethod
    def get_render_width(self) -> int:
        """Get current render width (it considers HiDPI)"""
        return rl.GetRenderWidth()

    @classmethod
    def get_render_height(self) -> int:
        """Get current render height (it considers HiDPI)"""
        return rl.GetRenderHeight()

    @classmethod
    def get_window_position(self):
        """Get window position XY on monitor"""
        position = rl.GetWindowPosition()
        return position.x, position.y

    @classmethod
    def get_window_scale_dpi(self):
        """Get window scale DPI factor"""
        scale_dpi = rl.GetWindowScaleDPI()
        return scale_dpi.x, scale_dpi.y


    # Monitor
    @classmethod
    def get_monitor_count(cls) -> int:
        """Get number of connected monitors"""
        return rl.GetMonitorCount()

    @classmethod
    def get_current_monitor(cls) -> int:
        """Get current connected monitor"""
        return rl.GetCurrentMonitor()

    @classmethod
    def set_window_monitor(cls, monitor: int):
        """Set monitor for the current window (fullscreen mode)"""
        rl.SetWindowMonitor(monitor)

    @classmethod
    def get_monitor_position(cls, monitor: int):
        """Get specified monitor position"""
        position = rl.GetMonitorPosition(monitor)
        return position.x, position.y

    @classmethod
    def get_monitor_width(cls, monitor: int) -> int:
        """Get specified monitor width (current video mode used by monitor)"""
        return rl.GetMonitorWidth(monitor)

    @classmethod
    def get_monitor_height(cls, monitor: int) -> int:
        """Get specified monitor height (current video mode used by monitor)"""
        return rl.GetMonitorHeight(monitor)

    @classmethod
    def get_monitor_physical_width(cls, monitor: int) -> int:
        """Get specified monitor physical width in millimetres"""
        return rl.GetMonitorPhysicalWidth(monitor)

    @classmethod
    def get_monitor_physical_height(cls, monitor: int) -> int:
        """Get specified monitor physical height in millimetres"""
        return rl.GetMonitorPhysicalHeight(monitor)

    @classmethod
    def get_monitor_refresh_rate(cls, monitor: int) -> int:
        """Get specified monitor refresh rate"""
        return rl.GetMonitorRefreshRate(monitor)

    @classmethod
    def get_monitor_name(cls, monitor: int) -> str:
        """Get the human-readable, UTF-8 encoded name of the primary monitor"""
        return pr.get_monitor_name(monitor)
