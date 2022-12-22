import pyray as pr
import maliang.structs.material as mod_material
import maliang.structs.matrix as mod_matrix
import maliang.structs.boundingbox as mod_boundingbox

class MMesh:
    def __init__(self):
        self.pr_mesh = None

    def unload(self):
        pr.unload_mesh(self.pr_mesh)

    def upload(self, dynamic: bool):
        pr.upload_mesh(self.pr_mesh, dynamic)

    def update_buffer(self, index, data, offset=0):
        pr.update_mesh_buffer(self.pr_mesh, index, data, len(data), offset)

    def draw(self, material: mod_material.MMaterial, transform):
        matrix = mod_matrix.MMatrix(*transform)
        pr.draw_mesh(self.pr_mesh, material.pr_material, matrix.pr_matrix)

    def draw_instanced(self, material: mod_material.MMaterial, transform, instances):
        matrix = mod_matrix.MMatrix(*transform)
        pr.draw_mesh_instanced(self.pr_mesh, material.pr_material, matrix.pr_matrix, instances)

    def export(self, filename):
        pr.export_mesh(self.pr_mesh, filename)

    def get_bounding_box(self):
        boundingbox = mod_boundingbox.MBoundingBox()
        boundingbox.pr_boundingbox = pr.get_mesh_bounding_box(self.pr_mesh)
        return boundingbox

    def gen_trngents(self):
        pr.gen_mesh_tangents(self.pr_mesh)
