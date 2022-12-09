import pyray as pr

class Transform:
    def __init__(self):
        self.matrix_counter = 0
        # pass

    @staticmethod
    def decorate_matrix_pusher(func):
        def inner(self, *args, **kwargs):
            # return func(self, *args, **kwargs)
            if not self.matrix_counter:
                self.push_matrix()
            return func(self, *args, **kwargs)
        return inner

    def release_matrix(self):
        while self.matrix_counter > 0:
            self.pop_matrix()

    def push_matrix(self):
        pr.rl_push_matrix()
        self.matrix_counter += 1

    def pop_matrix(self):
        pr.rl_pop_matrix()
        self.matrix_counter -= 1

    @decorate_matrix_pusher
    def transtate(self, x, y, z=0):
        pr.rl_translatef(x, y, z)

    @decorate_matrix_pusher
    def rotate(self, angle):
        # pr.matrix_rotate_z(angle)
        pr.rl_rotatef(angle, 0, 0, 1)

    @decorate_matrix_pusher
    def rotate_x(self, angle):
        pr.rl_rotatef(angle, 1, 0, 0)

    @decorate_matrix_pusher
    def rotate_y(self, angle):
        pr.rl_rotatef(angle, 0, 1, 0)

    @decorate_matrix_pusher
    def rotate_z(self, angle):
        pr.rl_rotatef(angle, 0, 0, 1)

    @decorate_matrix_pusher
    def scale(self, *args):
        if len(args) == 1:
            pr.rl_scalef(args[0], args[0], 1)
        elif len(args) == 2:
            pr.rl_scalef(args[0], args[1], 1)
        elif len(args) == 3:
            pr.rl_scalef(args[0], args[1], args[2])
