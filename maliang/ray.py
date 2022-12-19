import pyray as pr
from maliang.structs import MRay, MColor, MCamera2D, MCamera3D


class Ray():
    def __init__(self):
        pass

    def get_ray(self, x, y, camera: MCamera2D|MCamera3D) -> MRay:
        ray = MRay()
        ray.pr_ray = pr.get_mouse_ray(pr.Vector2(x, y), camera.pr_camera)
        return ray

    def draw_ray(self, ray: MRay, color):
        pr.draw_ray(ray.pr_ray, MColor(*color).to_pyray())

