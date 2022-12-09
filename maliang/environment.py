import pyray as pr



class Environment():
    def __init__(self, width, height, ):
        self.width = width
        self.height = height

    def resize(self, width, height):
        raise NotImplementedError

    def smooth(self):
        pr.rl_enable_smooth_lines()

    def no_smooth(self):
        pr.rl_disable_smooth_lines()

    def set_trace_log_level(self, log_level):
        pr.set_trace_log_level(log_level)
