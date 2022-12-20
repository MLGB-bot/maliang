import pyray as pr
from maliang.structs import MCamera2D, MCamera3D
from collections import deque


class Camera():

    def __init__(self):
        self.camera_queue = deque()

    def camera_2d(self, offset=(0, 0), target=(0, 0), rotation=0.0, zoom=1.0):
        return MCamera2D(pr.Camera2D( pr.Vector2(*offset), pr.Vector2(*target), rotation, zoom))

    def camera_3d(self, position=(0, 0, 0), target=(0, 0, 0), up=(0, 0, 0), fovy=1.0, projection=0):
        return MCamera3D(pr.Camera3D( pr.Vector3(*position), pr.Vector3(*target), pr.Vector3(*up), fovy, projection))

    def begin_camera(self, camera: MCamera2D|MCamera2D):
        camera.begin_mode()
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
