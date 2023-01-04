"""
◆ 如果一个细胞为ON，邻居中少于两个为ON，它变为OFF。（模拟生命数量过少）
◆ 如果一个细胞为ON，邻居中有两个或3个为ON，它保持为ON。
◆ 如果一个细胞为ON，邻居中超过3个为ON，它变为OFF。（模拟生命数量过多）
◆ 如果一个细胞为OFF，邻居中恰好有3个为ON，它变为ON。（模拟繁殖）
"""
import random
import traceback

from maliang import Maliang

app = Maliang(width=300, height=300, fps=30)
app.set_window_title("Conway Life Game")

class Cells():
    def __init__(self):
        self.cells = []
        self.cell_size = 4
        self.cell_num_x = int(app.width / self.cell_size)
        self.cell_num_y = int(app.height / self.cell_size)
        # colors
        self.background_color = (235, 235, 235, 255)
        self.grid_color = (200, 200, 200, 255)
        self.cell_color = (0, 0, 0, 235)

    # 1 init random cells
    def init_random_cells(self):
        for x in range(self.cell_num_x):
            line_cells = []
            for y in range(self.cell_num_y):
                line_cells.append(random.choice((True, False)))
                # line_cells.append(random.random() > 0.90)
            self.cells.append(line_cells)

    def display_grids(self):
        if self.cell_size > 1:
            for x in range(self.cell_num_x):
                _x = x * self.cell_size
                app.line(_x, 0, _x, app.height, stroke_width=1, stroke_color=self.grid_color)

            for y in range(self.cell_num_y):
                _y = y * self.cell_size
                app.line(0, _y, app.width, _y, stroke_width=1, stroke_color=self.grid_color)

    def display_cells(self):
        for x in range(self.cell_num_x):
            for y in range(self.cell_num_y):
                if self.cells[x][y]:
                    if self.cell_size == 1:
                        app.point(x, y, stroke_width=1, stroke_color=self.cell_color)
                    else:
                        app.rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)

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
        return (left_x, up_y), (x, up_y), (right_x, up_y), \
               (left_x, y), (right_x, y), \
               (left_x, down_y), (x, down_y), (right_x, down_y)

    def update_cells(self):
        raw_cells = {}

        def get_raw_cell(x, y):
            if (x, y) in raw_cells:
                return raw_cells[(x, y)]
            else:
                return self.cells[x][y]

        for x in range(self.cell_num_x):
            for y in range(self.cell_num_y):
                # get neighboors
                lived_neighboors = 0
                for neighboor in self.get_neighboor_coors(x, y):
                    # if raw_cells[neighboor[0]][neighboor[1]]:
                    if get_raw_cell(neighboor[0], neighboor[1]):
                        lived_neighboors += 1
                #
                if self.cells[x][y]:
                    if 2 <= lived_neighboors <= 3:
                        continue
                    else:
                        raw_cells[(x, y)] = True
                        self.cells[x][y] = False
                        continue
                else:
                    if lived_neighboors == 3:
                        raw_cells[(x, y)] = False
                        self.cells[x][y] = True
                # # random error
                # if random.random() < 0.0001:
                #     self.cells[x][y] = not self.cells[x][y]


cells = Cells()


def on_setup():
    cells.init_random_cells()
    app.no_stroke()
    app.fill(*cells.cell_color)


def on_draw():
    if app.is_mouse_clicked():
        on_mouse_clicked()

    cells.update_cells()
    app.background(*cells.background_color)
    cells.display_grids()
    cells.display_cells()


def on_mouse_clicked(*args):
    x = int(app.mouse_x / cells.cell_size)
    y = int(app.mouse_y / cells.cell_size)
    # print(app.mouse_x, app.mouse_y,x,y, len(cells.cells), len(cells.cells[0]))
    try:
        cells.cells[x][y] = not cells.cells[x][y]
        # app.rect(x * cells.cell_size, y * cells.cell_size, cells.cell_size, cells.cell_size, filled_color=(255, 0, 0))
    except IndexError:
        pass
    except:
        traceback.print_exc()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.loop()
