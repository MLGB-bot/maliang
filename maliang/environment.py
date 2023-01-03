import pyray as pr

class Environment():
    def __init__(self, fps=0):
        self.set_trace_log_level(7)
        self.fps = fps
        self.init_fps(fps)

    def init_fps(self, fps):
        if isinstance(fps, int):
            self.fps = fps
            pr.set_target_fps(fps)

    def smooth(self):
        pr.rl_enable_smooth_lines()

    def no_smooth(self):
        pr.rl_disable_smooth_lines()

    def set_trace_log_level(self, log_level):
        pr.set_trace_log_level(log_level)

    def set_clipboard_text(self, text):
        pr.set_clipboard_text(text)

    def get_clipboard_text(self, ):
        return pr.get_clipboard_text()

    def enable_event_waiting(self):
        pr.enable_event_waiting()

    def disable_event_waiting(self):
        pr.disable_event_waiting()
