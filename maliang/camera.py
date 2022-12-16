import pyray as pr
from maliang.structs import MCamera
from collections import deque


class Camera():
    def __init__(self):
        self.camera_queue = deque()

    def begin_camera(self, camera: MCamera):
        if camera.dimension == 2:
            pr.begin_mode_2d(camera.pr_camera)
        else:
            pr.begin_mode_3d(camera.pr_camera)
        self.camera_queue.append(camera.dimension)

    def end_camera(self, ):
        dimension = self.camera_queue.pop()
        if dimension == 2:
            pr.end_mode_2d()
        else:
            pr.end_mode_3d()

    def set_camera_pan_control(self, keyboard_key: int):
        # Set camera pan key to combine with mouse movement (free camera)
        pr.set_camera_pan_control(keyboard_key)

    def set_camera_alt_control(self, keyboard_key: int):
        # Set camera alt key to combine with mouse movement (free camera)
        pr.set_camera_alt_control(keyboard_key)

    def set_camera_smooth_zoom_control(self, key_smooth_zoom: int):
        pr.set_camera_smooth_zoom_control(key_smooth_zoom)

    def set_camera_move_controls(self, key_up: int = None, key_down: int = None,
                                 key_left: int = None, key_right: int = None,
                                 key_front: int = None, key_back: int = None):
        pr.set_camera_move_controls(key_front, key_back, key_right, key_left, key_up, key_down)
