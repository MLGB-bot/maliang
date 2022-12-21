import pyray as pr
from maliang.structs import MMesh, MImage


class Model():
    def __init__(self):
        pass

    def gen_mesh_poly(self, sides: int, radius: float):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_poly(sides, radius)
        return mesh

    def gen_mesh_plane(self, len_x: float, len_z: float, res_x: int, res_z: int):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_plane(len_x, len_z, res_x, res_z)
        return mesh

    def gen_mesh_cube(self, len_x: float, len_y: float, len_z: float):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_cube(len_x, len_y, len_z)
        return mesh

    def gen_mesh_sphere(self, radius: float, rings: int=16, slices: int=16):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_sphere(radius, rings, slices)
        return mesh

    def gen_mesh_hemi_sphere(self, radius: float, rings: int=16, slices: int=16):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_hemi_sphere(radius, rings, slices)
        return mesh

    def gen_mesh_cylinder(self, radius: float, height: float, slices: int=16):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_cylinder(radius, height, slices)
        return mesh

    def gen_mesh_cone(self, radius: float, height: float, slices: int=16):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_cone(radius, height, slices)
        return mesh

    def gen_mesh_torus(self, radius: float, size: float, rad_seg: int, sides: int):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_torus(radius, size, rad_seg, sides)
        return mesh

    def gen_mesh_knot(self, radius: float, size: float, rad_seg: int, sides: int):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_knot(radius, size, rad_seg, sides)
        return mesh

    def gen_mesh_heightmap(self, img: MImage, len_x: float, len_y: float, len_z: float):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_heightmap(img.pr_image, pr.Vector3(len_x, len_y, len_z))
        return mesh

    def gen_mesh_cubicmap(self, img: MImage, len_x: float, len_y: float, len_z: float):
        mesh = MMesh()
        mesh.pr_mesh = pr.gen_mesh_cubicmap(img.pr_image, pr.Vector3(len_x, len_y, len_z))
        return mesh