import os
import pyray as pr
from maliang.units import ResourceLoader
from maliang.structs import MModel, MMesh, MBoundingBox, MColor

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

    def draw_boundingbox(self, boundingbox: MBoundingBox, color=(0,0,0)):
        boundingbox.draw(MColor(*color))

    # def draw_billboard(self, camera, ):
