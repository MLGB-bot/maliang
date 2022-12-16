import pyray as pr


class MCamera():
    def __init__(self, dimension: int=3, pr_camera=None):
        self.dimension = dimension
        self.pr_camera = pr_camera

    def get_coordinate_ray(self, x, y):
        return pr.get_mouse_ray(pr.Vector2(x, y), self.pr_camera)

    def get_matrix(self):
        if self.dimension == 3:
            return pr.get_camera_matrix(self.pr_camera)
        else:
            return pr.get_camera_matrix_2d(self.pr_camera)

    def get_world_to_screen(self, x, y, z=0, width=0, height=0):
        if self.dimension == 3:
            if width or height:
                return pr.get_world_to_screen_ex(pr.Vector3(x, y, z), self.pr_camera, width, height)
            else:
                return pr.get_world_to_screen(pr.Vector3(x, y, z), self.pr_camera)
        else:
            return pr.get_world_to_screen_2d(pr.Vector2(x, y), self.pr_camera)

    def get_screen_to_world(self, x, y):
        if self.dimension == 2:
            return pr.get_screen_to_world_2d(pr.Vector2(x, y), self.pr_camera)

    def set_mode(self, mode):
        # Set camera mode (multiple camera modes available)
        pr.set_camera_mode(self.pr_camera, mode)

    def update(self):
        # Update camera position for selected mode
        pr.update_camera(self.pr_camera)

