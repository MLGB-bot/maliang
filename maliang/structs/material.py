import pyray as pr
import maliang.structs.texture as mod_texture


class MMaterial:
    MATERIAL_MAP_ALBEDO    = 0  # Albedo material (same as: MATERIAL_MAP_DIFFUSE)
    MATERIAL_MAP_METALNESS = 1  # Metalness material (same as: MATERIAL_MAP_SPECULAR)
    MATERIAL_MAP_NORMAL    = 2  # Normal material
    MATERIAL_MAP_ROUGHNESS = 3  # Roughness material
    MATERIAL_MAP_OCCLUSION = 4  # Ambient occlusion material
    MATERIAL_MAP_EMISSION  = 5  # Emission material
    MATERIAL_MAP_HEIGHT    = 6  # Heightmap material
    MATERIAL_MAP_CUBEMAP   = 7  # Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
    MATERIAL_MAP_IRRADIANCE = 8 # Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
    MATERIAL_MAP_PREFILTER = 9  # Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
    MATERIAL_MAP_BRDF  = 10     # Brdf material

    def __init__(self):
        self.pr_material = None

    def unload(self):
        pr.unload_material(self.pr_material)

    def set_texture(self, map_type: int, texture: mod_texture.MTexture):
        pr.set_material_texture(self.pr_material, map_type, texture.pr_texture)

