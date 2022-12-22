import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.boundingbox as mod_boundingbox
import maliang.structs.mesh as mod_mesh
import maliang.structs.matrix as mod_matrix

class MRay:
    def __init__(self):
        self.pr_ray = None

    def draw(self, color: mod_color.MColor):
        pr.draw_ray(self.pr_ray, color.to_pyray())

    def get_collision_sphere(self, x, y, z, diam):
        radius = diam  * 0.5
        return pr.get_ray_collision_sphere(self.pr_ray, pr.Vector3(x, y, z), radius)

    def get_collision_box(self, box: mod_boundingbox.MBoundingBox):
        return pr.get_ray_collision_box(self.pr_ray, box.pr_boundingbox)

    def get_collision_mesh(self, mesh: mod_mesh.MMesh, transform: mod_matrix.MMatrix):
        return pr.get_ray_collision_mesh(self.pr_ray, mesh.pr_mesh, transform.pr_matrix)

    def get_collision_triangle(self, point1, point2, point3):
        return pr.get_ray_collision_triangle(
            self.pr_ray, pr.Vector3(*point1), pr.Vector3(*point2), pr.Vector3(*point3)
        )

    def get_collision_quad(self, point1, point2, point3, point4):
        return pr.get_ray_collision_quad(
            self.pr_ray, pr.Vector3(*point1), pr.Vector3(*point2), pr.Vector3(*point3), pr.Vector3(*point4)
        )

