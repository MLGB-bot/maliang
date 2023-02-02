import pyray as pr
import maliang.structs.ray as mod_ray
import maliang.structs.vector as mod_vector
from functools import partial

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
        MCamera.__init__(self, pr_camera)
        self.__offset = None
        self.__target = None

    def on_mvector_change(self, value, attr):
        setattr(self.pr_camera, attr, pr.Vector2(*value))

    @property
    def offset(self):
        if not self.__offset:
            pr_vector = self.pr_camera.offset
            self.__offset = mod_vector.MVector(pr_vector.x, pr_vector.y, pr_vector.z)
            callback = partial(self.on_mvector_change, attr='offset')
            self.__offset.bind(callback=callback)
        return self.__offset

    @offset.setter
    def offset(self, value: tuple|list):
        if not self.__offset:
            self.__offset = mod_vector.MVector(*value)
            callback = partial(self.on_mvector_change, attr='offset')
            self.__offset.bind(callback=callback)
            self.__offset.bind_update()
        else:
            self.__offset.value = value

    @property
    def target(self):
        if not self.__target:
            pr_vector = self.pr_camera.target
            self.__target = mod_vector.MVector(pr_vector.x, pr_vector.y, pr_vector.z)
            callback = partial(self.on_mvector_change, attr='target')
            self.__target.bind(callback=callback)
        return self.__target

    @target.setter
    def target(self, value):
        if not self.__target:
            self.__target = mod_vector.MVector(*value)
            callback = partial(self.on_mvector_change, attr='target')
            self.__target.bind(callback=callback)
            self.__target.bind_update()
        else:
            self.__target.value = value

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
        MCamera.__init__(self, pr_camera)
        self.__target = None
        self.__position = None
        self.__up = None

    def on_mvector_change(self, value, attr):
        setattr(self.pr_camera, attr, pr.Vector3(*value))

    @property
    def target(self):
        # 2d & 3d
        if not self.__target:
            pr_vector = self.pr_camera.target
            self.__target = mod_vector.MVector(pr_vector.x, pr_vector.y, pr_vector.z)
            callback = partial(self.on_mvector_change, attr='target')
            self.__target.bind(callback=callback)
        return self.__target

    @target.setter
    def target(self, value):
        if not self.__target:
            self.__target = mod_vector.MVector(*value)
            callback = partial(self.on_mvector_change, attr='target')
            self.__target.bind(callback=callback)
            self.__target.bind_update()
        else:
            self.__target.value = value

    @property
    def position(self):
        if not self.__position:
            pr_vector = self.pr_camera.position
            self.__position = mod_vector.MVector(pr_vector.x, pr_vector.y, pr_vector.z)
            callback = partial(self.on_mvector_change, attr='position')
            self.__position.bind(callback=callback)
        return self.__position

    @position.setter
    def position(self, value):
        if not self.__position:
            self.__position = mod_vector.MVector(*value)
            callback = partial(self.on_mvector_change, attr='position')
            self.__position.bind(callback=callback)
            self.__position.bind_update()
        else:
            self.__position.value = value

    @property
    def up(self):
        if not self.__up:
            pr_vector = self.pr_camera.up
            self.__up = mod_vector.MVector(pr_vector.x, pr_vector.y, pr_vector.z)
            callback = partial(self.on_mvector_change, attr='up')
            self.__up.bind(callback=callback)
        return self.__up

    @up.setter
    def up(self, value):
        if not self.__up:
            self.__up = mod_vector.MVector(*value)
            callback = partial(self.on_mvector_change, attr='up')
            self.__up.bind(callback=callback)
            self.__up.bind_update()
        else:
            self.__up.value = value

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

