import pyray as pr


class MTexture:
    npatch_layouts = [
        0,  # Npatch layout: 3x3 tiles
        1,  # Npatch layout: 1x3 tiles
        2  # Npatch layout: 3x1 tiles
    ]

    def __init__(self):
        self.pr_texture = None

    @property
    def width(self):
        return self.pr_texture.width

    @property
    def height(self):
        return self.pr_texture.height

    @property
    def format(self):
        return self.pr_texture.format

    @property
    def mipmaps(self):
        return self.pr_texture.mipmaps

    def unload(self):
        if self.pr_texture:
            pr.unload_texture(self.pr_texture)
            self.pr_texture = None

    def gen_mipmaps(self):
        pr.gen_texture_mipmaps(self.pr_texture)

    def set_filter(self, filter: int):
        pr.set_texture_filter(self.pr_texture, filter)

    def set_wrap(self, wrap: int):
        pr.set_texture_wrap(self.pr_texture, wrap)

    # todo update_rect
    def update(self, pixels):
        pr.update_texture(self.pr_texture, pixels)

    def draw(self, x, y, tint=pr.WHITE):
        pr.draw_texture(self.pr_texture, x, y, tint)

    def draw_pro(self, x, y, w, h, src_x=0, src_y=0, src_w=0, src_h=0, origin: tuple[int, int] = (0, 0), rotation=0,
                 tint=pr.WHITE):
        pr.draw_texture_pro(
            self.pr_texture,
            pr.Rectangle(src_x, src_y, src_w or self.width, src_h or self.height),
            pr.Rectangle(x, y, w, h),
            pr.Vector2(*origin),
            rotation,
            tint
        )

    def draw_ex(self, x, y, scale=1, src_x=0, src_y=0, src_w=0, src_h=0, origin: tuple[int, int] = (0, 0), rotation=0,
                tint=pr.WHITE):
        src_w = src_w or self.width
        src_h = src_h or self.height
        if scale == 1 and rotation == 0:
            # 既不缩放也不旋转
            pr.draw_texture_rec(
                self.pr_texture,
                pr.Rectangle(src_x, src_y, src_w or self.width, src_h or self.height),
                pr.Vector2(x, y),
                pr.WHITE
            )
        elif origin == (0, 0) and src_x == 0 and src_y == 0 and src_w == self.width and src_h == self.height:
            # 以(0,0)为左上角 旋转与缩放, 不裁剪图片
            pr.draw_texture_ex(self.pr_texture, pr.Vector2(x, y), rotation, scale, tint)
        else:
            dst_w = src_w * scale
            dst_h = src_h * scale
            if (dst_w and dst_h):
                self.draw_pro(x, y, dst_w, dst_h, src_x, src_y, src_w, src_h, origin, rotation, tint)

    def draw_tiled(self, x, y, w, h, src_x=0, src_y=0, src_w=0, src_h=0, scale=1, origin: tuple[int, int] = (0, 0),
                   rotation=0, tint=pr.WHITE):
        # 平铺 不缩放 仅仅裁剪
        pr.draw_texture_tiled(
            self.pr_texture,
            pr.Rectangle(src_x, src_y, src_w or self.width, src_h or self.height),
            pr.Rectangle(x, y, w, h),
            pr.Vector2(*origin),
            rotation,
            scale,
            tint
        )

    def draw_quad(self, x, y, w, h, num_x=1, num_y=1, offset_x: float = 0, offset_y: float = 0, tint=pr.WHITE):
        """
        :param x:
        :param y:
        :param w:
        :param h:
        :param num_x:
        :param num_y:
        :param offset_x: -1~1
        :param offset_y: -1~1
        :param tint:
        :return:
        """
        # 填充
        pr.draw_texture_quad(
            self.pr_texture,
            pr.Vector2(num_x, num_y),
            pr.Vector2(offset_x, offset_y),
            pr.Rectangle(x, y, w, h),
            tint
        )

    def draw_npatch(self, x, y, w, h, src_x=0, src_y=0, src_w=0, src_h=0, left=0, top=0, right=0, bottom=0, layout=0,
                    origin: tuple[int, int] = (0, 0), rotation=0, tint=pr.WHITE):
        # assert layout in self.npatch_layouts
        pr.draw_texture_n_patch(
            self.pr_texture,
            pr.NPatchInfo(
                pr.Rectangle(src_x, src_y, src_w or self.width, src_h or self.height),
                left, top, right, bottom, layout
            ),
            pr.Rectangle(x, y, w, h),
            pr.Vector2(*origin),
            rotation,
            tint
        )

    def draw_poly(self, points, tint=pr.WHITE):
        """
        source_code.py
        # >>>
            center = tx.width / 2, tx.height / 2
            pr.rl_set_texture(tx.pr_texture.id)
            pr.rl_color4ub(*tint)
            pr.rl_begin(7)
            for i in range(len(texcoords) - 1):
                pr.rl_tex_coord2f(0.5, 0.5)
                pr.rl_vertex2f(*center)

                pr.rl_tex_coord2f(*texcoords[i])
                pr.rl_vertex2f(points[i][0] + center[0], points[i][1] + center[1])

                pr.rl_tex_coord2f(*texcoords[i + 1])
                pr.rl_vertex2f(points[i + 1][0] + center[0], points[i + 1][1] + center[1])

                pr.rl_tex_coord2f(*texcoords[i + 1])
                pr.rl_vertex2f(points[i + 1][0] + center[0], points[i + 1][1] + center[1])
            pr.rl_end()
            pr.rl_set_texture(0)
        # >>>
        :param center_x:
        :param center_y:
        :param w:
        :param h:
        :param src_x:
        :param src_y:
        :param src_w:
        :param src_h:
        :param left:
        :param top:
        :param right:
        :param bottom:
        :param layout:
        :param origin:
        :param rotation:
        :param tint:
        :return:
        """
        texcoords = []
        positions = []
        center = self.width * 0.5, self.height * 0.5
        for point in points:
            texcoords.append(((point[0]-center[0])/self.width+0.5, (point[1]-center[1])/self.height+0.5))
            positions.append((point[0]-center[0], point[1]-center[1] ))

        pr.draw_texture_poly(
            self.pr_texture,
            pr.Vector2(*center),
            positions,
            texcoords,
            len(points),
            tint
        )
