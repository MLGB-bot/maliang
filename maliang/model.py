import os
import pyray as pr
from maliang.units import ResourceLoader
from maliang.structs import MModel, MMesh, MBoundingBox, MColor, MCamera3D, MTexture


class Model():
    def __init__(self):
        pass

    def load_model(self, filename):
        file_path = os.path.join(ResourceLoader.static_dir, filename)
        model = MModel()
        model.pr_model = pr.load_model(file_path)
        return model

    def load_model_from_mesh(self, mesh: MMesh):
        model = MModel()
        model.pr_model = pr.load_model_from_mesh(mesh.pr_mesh)
        return model

    def unload_model(self, model: MModel):
        pr.unload_model(model.pr_model)

    def unload_model_keep_meshes(self, model: MModel):
        pr.unload_model_keep_meshes(model.pr_model)

    def draw_boundingbox(self, boundingbox: MBoundingBox, color=(0, 0, 0)):
        boundingbox.draw(MColor(*color))

    def draw_billboard(self, camera: MCamera3D, texture: MTexture, x, y, z, size: tuple | list, tint=None, up=(0, 1, 0),
                       origin=(0, 0), rotation: float = 0.0, source=None):
        if not source:
            source = pr.Rectangle(0, 0, texture.width, texture.height)
        pr.draw_billboard_pro(camera.pr_camera, texture.pr_texture, source, pr.Vector3(x, y, z), pr.Vector3(*up),
                              pr.Vector2(*size), pr.Vector2(*origin), rotation, MColor(*(tint or pr.WHITE)).to_pyray())

    def set_model_mesh_material(self, model: MModel, mesh_id: int, material_id: int):
        model.set_mesh_matrrial(mesh_id, material_id)