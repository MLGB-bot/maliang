import os
import pyray as pr
from maliang.structs import MMaterial, MModel
from maliang.units import ResourceLoader, ImageMode

class Model():
    def __init__(self):
        pass

    def load_materials(self, filename, count: int):
        image_path = os.path.join(ResourceLoader.static_dir, filename)
        material = MMaterial()
        material.pr_material = pr.load_materials(image_path, count)
        return material

    def load_material_default(self):
        material = MMaterial()
        material.pr_material = pr.load_material_default()
        return material

