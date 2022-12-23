import os
import pyray as pr
from maliang.structs import MMaterial
from maliang.units import ResourceLoader

class Material():
    def __init__(self):
        pass

    def load_materials(self, filename, count: int):
        filepath = os.path.join(ResourceLoader.static_dir, filename)
        data_list = []
        for pr_matetial in pr.load_materials(filepath, count):
            material = MMaterial()
            material.pr_material = pr_matetial
            data_list.append(material)
        return data_list

    def load_material_default(self):
        material = MMaterial()
        material.pr_material = pr.load_material_default()
        return material

