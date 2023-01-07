"""
◆ 如果一个细胞为ON，邻居中少于两个为ON，它变为OFF。（模拟生命数量过少）
◆ 如果一个细胞为ON，邻居中有两个或3个为ON，它保持为ON。
◆ 如果一个细胞为ON，邻居中超过3个为ON，它变为OFF。（模拟生命数量过多）
◆ 如果一个细胞为OFF，邻居中恰好有3个为ON，它变为ON。（模拟繁殖）
"""

import random

import maliang
from maliang import Maliang

app = Maliang(width=600, height=600, fps=0, full_screen=False, title='Conway Life Game')

class Cells():
    def __init__(self):
        self.background_color = (235, 235, 235, 255)
        self.grid_color = (200, 200, 200, 255)
        self.cell_color = (0, 0, 0, 235)
        self.cell_size = 20
        self.cells = {}

    @property
    def cell_num_x(self):
        return int(app.width / self.cell_size)

    @property
    def cell_num_y(self):
        return int(app.height / self.cell_size)

    # 1 init random cells
    def init_random_cells(self):
        for x in range(self.cell_num_x):
            for y in range(self.cell_num_y):
                # line_cells.append(random.choice((True, False)))
                # line_cells.append(random.random() > 0.90)
                if random.choice((True, False)):
                    self.cells[(x, y)] = True

    def display_grids(self):
        if self.cell_size > 1:
            for x in range(self.cell_num_x):
                _x = x * self.cell_size
                app.line(_x, 0, _x, app.height, stroke_width=1, stroke_color=self.grid_color)

            for y in range(self.cell_num_y):
                _y = y * self.cell_size
                app.line(0, _y, app.width, _y, stroke_width=1, stroke_color=self.grid_color)

    def get_neighboor_coors(self, x, y):
        left_x = x - 1
        if left_x < 0:
            left_x = self.cell_num_x + left_x
        right_x = x + 1
        if right_x >= self.cell_num_x:
            right_x = right_x - self.cell_num_x
        up_y = y - 1
        if up_y < 0:
            up_y = self.cell_num_y + up_y
        down_y = y + 1
        if down_y >= self.cell_num_y:
            down_y = down_y - self.cell_num_y

        for _x in (left_x, x, right_x):
            for _y in (up_y, y, down_y):
                if _x == x and _y == y:
                    continue
                yield _x, _y

    def rev_cell(self, x, y):
        if self.cells.get((x, y), False):
            del self.cells[(x, y)]
        else:
            self.cells[(x, y)] = True

    def update_cells(self):
        raw_cells = {}

        def get_raw_cell(x, y):
            return raw_cells[(x, y)] if (x, y) in raw_cells else (x, y) in self.cells

        for x in range(self.cell_num_x):
            for y in range(self.cell_num_y):
                # get neighboors
                lived_neighboors = sum([get_raw_cell(neighboor_x, neighboor_y)
                                        for neighboor_x, neighboor_y in self.get_neighboor_coors(x, y)])
                if (x, y) in self.cells:
                    if 2 <= lived_neighboors <= 3:
                        pass
                    else:
                        raw_cells[(x, y)] = True
                        del self.cells[(x, y)]
                else:
                    if lived_neighboors == 3:
                        raw_cells[(x, y)] = False
                        self.cells[(x, y)] = True

                # # random error
                # if random.random() < 0.0001:
                #     self.rev_cell(x, y)

                # show cell
                if (x, y) in self.cells:
                    if self.cell_size == 1:
                        app.point(x * self.cell_size, y * self.cell_size, stroke_width=self.cell_size,
                                  stroke_color=self.cell_color, shape='rect')
                    else:
                        app.rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, filled_color=self.cell_color)

cells = Cells()
exit_alert = False

def on_setup():
    cells.init_random_cells()
    app.no_stroke()
    app.fill(*cells.cell_color)
    app.set_exit_key(maliang.KeyboardKeys.KEY_Q)


def on_draw():
    if app.is_mouse_clicked():
        on_mouse_clicked()
    if app.is_key_clicked(maliang.KeyboardKeys.KEY_F):
        if app.is_window_fullscreen():
            app.unfull_screen()
        else:
            app.full_screen()

    global exit_alert
    if app.should_exit():
        if exit_alert:
            app.exit()
        else:
            exit_alert = True

    app.background(*cells.background_color)
    cells.display_grids()
    cells.update_cells()
    # app.draw_fps(0, 0)
    if exit_alert:
        app.rect(0, 100, app.width, 200)
        app.text("Exit? [Y/N]", 40, 180, text_size=30, text_color=(255, ))
        if app.is_key_clicked(maliang.KeyboardKeys.KEY_Y):
            app.exit()
        elif app.is_key_clicked(maliang.KeyboardKeys.KEY_N):
            exit_alert = False
        elif app.is_key_clicked(maliang.KeyboardKeys.KEY_ESCAPE):
            exit_alert = False


def on_mouse_clicked(*args):
    x = int(app.mouse_x / cells.cell_size)
    y = int(app.mouse_y / cells.cell_size)
    # print(app.mouse_x, app.mouse_y,x,y, len(cells.cells), len(cells.cells[0]))
    if 0 <= x < cells.cell_num_x and (0 <= y < cells.cell_num_x):
        cells.rev_cell(x, y)


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.loop()
