import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.boundingbox as mod_boundingbox
import maliang.structs.mesh as mod_mesh
import maliang.structs.material as mod_material


class MModel:
    def __init__(self):
        self.pr_model = None

    @property
    def transform(self):
        return self.pr_model.transform

    @transform.setter
    def transform(self, value):
        self.pr_model.transform = value

    @property
    def material_count(self):
        return self.pr_model.materialCount

    @material_count.setter
    def material_count(self, value):
        self.pr_model.materialCount = value

    @property
    def materials(self):
        raw_materials = self.pr_model.materials
        data_list = []
        for i in range(self.material_count):
            mmaterial = mod_material.MMaterial()
            mmaterial.pr_material = raw_materials[i]
            data_list.append(mmaterial)
        return data_list

    @property
    def mesh_count(self):
        return self.pr_model.meshCount

    @mesh_count.setter
    def mesh_count(self, value):
        self.pr_model.meshCount = value

    @property
    def meshes(self):
        raw_meshs = self.pr_model.meshes
        data_list = []
        for i in range(self.mesh_count):
            mmesh = mod_mesh.MMesh()
            mmesh.pr_mesh = raw_meshs[i]
            data_list.append(mmesh)
        return data_list

    @property
    def mesh_material(self):
        return self.pr_model.meshMaterial

    @mesh_material.setter
    def mesh_material(self, value):
        self.pr_model.meshMaterial = value

    @property
    def bone_count(self):
        return self.pr_model.boneCount

    @bone_count.setter
    def bone_count(self, value):
        self.pr_model.boneCount = value

    @property
    def bones(self):
        return self.pr_model.bones

    @bones.setter
    def bones(self, value):
        self.pr_model.bones = value

    @property
    def bind_pose(self):
        return self.pr_model.bindPose

    @bind_pose.setter
    def bind_pose(self, value):
        self.pr_model.bindPose = value

    def draw(self, x, y, z, scale=1, filled_color=(255, 255, 255, 255), stroke_color: mod_color.MColor = None):
        if filled_color:
            pr.draw_model(self.pr_model, pr.Vector3(x, y, z), scale, mod_color.MColor(*filled_color).to_pyray())
        if stroke_color:
            pr.draw_model_wires(self.pr_model, pr.Vector3(x, y, z), scale, mod_color.MColor(*stroke_color).to_pyray())

    def draw2(self, x, y, z, scale=(1, 1, 1), rotation_axis=(0, 0, 0), rotation_angle=0,
              filled_color=(255, 255, 255, 255), stroke_color: mod_color.MColor = None):
        if filled_color:
            pr.draw_model_ex(self.pr_model, pr.Vector3(x, y, z), pr.Vector3(*rotation_axis), rotation_angle,
                             pr.Vector3(*scale), mod_color.MColor(*filled_color).to_pyray())
        if stroke_color:
            pr.draw_model_wires_ex(self.pr_model, pr.Vector3(x, y, z), pr.Vector3(*rotation_axis), rotation_angle,
                                   pr.Vector3(*scale), mod_color.MColor(*stroke_color).to_pyray())

    def get_bounding_box(self):
        boundingbox = mod_boundingbox.MBoundingBox()
        boundingbox.pr_boundingbox = pr.get_model_bounding_box(self.pr_model)
        return boundingbox

    def set_mesh_matrrial(self, mesh_id: int, material_id: int):
        pr.set_model_mesh_material(self.pr_model, mesh_id, material_id)