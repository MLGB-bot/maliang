import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.boundingbox as mod_boundingbox
import maliang.structs.mesh as mod_mesh
import maliang.structs.matrix as mod_matrix


class MRayCollision:
    def __init__(self, pr_raycollision):
        self.pr_raycollision = pr_raycollision

    @property
    def hit(self):
        return self.pr_raycollision.hit

    @hit.setter
    def hit(self, value):
        self.pr_raycollision.hit = value

    @property
    def distance(self):
        return self.pr_raycollision.distance

    @distance.setter
    def distance(self, value):
        self.pr_raycollision.distance = value

    @property
    def point(self):
        return self.pr_raycollision.point

    @point.setter
    def point(self, value):
        self.pr_raycollision.point = value

    @property
    def normal(self):
        return self.pr_raycollision.normal

    @normal.setter
    def normal(self, value):
        self.pr_raycollision.normal = value

class MRay:
    def __init__(self):
        self.pr_ray = None

    def draw(self, color: mod_color.MColor):
        pr.draw_ray(self.pr_ray, color.to_pyray())

    def get_collision_sphere(self, x, y, z, diam):
        radius = diam  * 0.5
        return MRayCollision(pr.get_ray_collision_sphere(self.pr_ray, pr.Vector3(x, y, z), radius))

    def get_collision_box(self, box: mod_boundingbox.MBoundingBox):
        return MRayCollision(pr.get_ray_collision_box(self.pr_ray, box.pr_boundingbox))

    def get_collision_mesh(self, mesh: mod_mesh.MMesh, transform: mod_matrix.MMatrix):
        return MRayCollision(pr.get_ray_collision_mesh(self.pr_ray, mesh.pr_mesh, transform.pr_matrix))

    def get_collision_triangle(self, point1, point2, point3):
        return MRayCollision(pr.get_ray_collision_triangle(
            self.pr_ray, pr.Vector3(*point1), pr.Vector3(*point2), pr.Vector3(*point3)
        ))

    def get_collision_quad(self, point1, point2, point3, point4):
        return MRayCollision(pr.get_ray_collision_quad(
            self.pr_ray, pr.Vector3(*point1), pr.Vector3(*point2), pr.Vector3(*point3), pr.Vector3(*point4)
        ))

