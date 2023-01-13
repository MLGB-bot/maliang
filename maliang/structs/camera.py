import pyray as pr
import maliang.structs.ray as mod_ray

class MCamera:
    def __init__(self, pr_camera):
        self.pr_camera = pr_camera

    def get_ray(self, x, y) -> mod_ray.MRay:
        ray = mod_ray.MRay()
        ray.pr_ray = pr.get_mouse_ray(pr.Vector2(x, y), self.pr_camera)
        return ray

    def set_mode(self, mode):
        # Set camera mode (multiple camera modes available)
        pr.set_camera_mode(self.pr_camera, mode)

    def update(self):
        # Update camera position for selected mode
        pr.update_camera(self.pr_camera)


class MCamera2D(MCamera):
    dimension = 2
    def __init__(self, pr_camera):
        self.pr_camera = pr_camera
        MCamera.__init__(self, pr_camera)

    @property
    def offset(self):
        # 2d
        offset = self.pr_camera.offset
        return offset.x, offset.y

    @offset.setter
    def offset(self, offset: tuple|list):
        self.pr_camera.offset = pr.Vector2(*offset)

    @property
    def target(self):
        # 2d & 3d
        target = self.pr_camera.target
        return target.x, target.y

    @target.setter
    def target(self, value):
        self.pr_camera.target = pr.Vector2(*value)

    @property
    def rotation(self):
        return self.pr_camera.rotation

    @rotation.setter
    def rotation(self, value):
        self.pr_camera.rotation = value

    @property
    def zoom(self):
        return self.pr_camera.zoom

    @zoom.setter
    def zoom(self, value):
        self.pr_camera.zoom = value

    def begin_mode(self):
        pr.begin_mode_2d(self.pr_camera)

    def get_matrix(self):
        return pr.get_camera_matrix_2d(self.pr_camera)

    def get_world_to_screen(self, x, y):
        return pr.get_world_to_screen_2d(pr.Vector2(x, y), self.pr_camera)

    def get_screen_to_world(self, x, y):
        return pr.get_screen_to_world_2d(pr.Vector2(x, y), self.pr_camera)

class MCamera3D(MCamera):
    dimension = 3

    def __init__(self, pr_camera):
        self.pr_camera = pr_camera
        MCamera.__init__(self, pr_camera)

    @property
    def target(self):
        # 2d & 3d
        target = self.pr_camera.target
        return target.x, target.y, target.z

    @target.setter
    def target(self, value):
        self.pr_camera.target = pr.Vector3(*value)

    @property
    def position(self):
        position = self.pr_camera.position
        return position.x, position.y, position.z

    @position.setter
    def position(self, value):
        self.pr_camera.position = pr.Vector3(*value)

    @property
    def up(self):
        up = self.pr_camera.up
        return up.x, up.y, up.z

    @up.setter
    def up(self, value):
        self.pr_camera.up = pr.Vector3(*value)

    @property
    def fovy(self):
        return self.pr_camera.fovy

    @fovy.setter
    def fovy(self, value):
        self.pr_camera.fovy = value

    @property
    def projection(self):
        return self.pr_camera.projection

    @projection.setter
    def projection(self, value):
        self.pr_camera.projection = value

    def begin_mode(self):
        pr.begin_mode_3d(self.pr_camera)

    def get_matrix(self):
        return pr.get_camera_matrix(self.pr_camera)

    def get_world_to_screen(self, x, y, z=0, width=0, height=0):
        if width or height:
            return pr.get_world_to_screen_ex(pr.Vector3(x, y, z), self.pr_camera, width, height)
        else:
            return pr.get_world_to_screen(pr.Vector3(x, y, z), self.pr_camera)

