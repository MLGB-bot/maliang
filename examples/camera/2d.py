import random
from maliang import Maliang, KeyboardKeys


app = Maliang(width=800, height=450, buffer_proxy=False, fps=80)

MAX_BUILDINGS = 100
spacing = 0
buildings = []

for i in range(MAX_BUILDINGS):
    width = random.randint(50, 200)
    height = random.randint(100, 800)
    buildings.append({
        "width": width,
        "height": height,
        "x": int(-6000.0 + spacing),
        "y": int(app.height - 130.0 - height),
        "color": (random.randint(200, 240), random.randint(200, 240), random.randint(200, 250), 255)
    })
    spacing += width


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self):
        app.rect(self.x, self.y, self.w, self.h, filled_color=(255, 0, 200), stroke_width=0)

player = Player(400, 280, 40, 40)

camera = app.camera_2d()
camera.target = (player.x + 20.0, player.y + 20.0, )
camera.offset = (app.width/2, app.height/2)
camera.rotation = 0
camera.zoom = 1.0

RED = (255, 0, 0)
BLACK = (0, 0 ,0)
DARKGRAY = (80, 80, 80)

def on_setup():
    app.no_stroke()
    pass

def on_draw():
    if app.is_key_down(KeyboardKeys.KEY_A):
        # print("s: running?", )
        player.x -= 1
    if app.is_key_down(KeyboardKeys.KEY_D):
        # print("s: running?", )
        player.x += 1

    camera.target = (player.x + 20, player.y + 20)

    if app.is_key_down(KeyboardKeys.KEY_W):
        camera.rotation -= 1
    elif app.is_key_down(KeyboardKeys.KEY_S):
        camera.rotation += 1
    if camera.rotation >= 360:
        camera.rotation = 0
    elif camera.rotation <= -360:
        camera.rotation = 0

    camera.zoom += app.is_mouse_wheel() * 0.05
    if camera.zoom > 3:
        camera.zoom = 3
    elif camera.zoom < 0.1:
        camera.zoom = 0.1

    if (app.is_key_clicked(KeyboardKeys.KEY_R)):
        camera.zoom = 1.0
        camera.rotation = 0

    app.background(255, 50)
    app.begin_camera(camera)
    app.rect(-6000, 320, 13000, 8000, filled_color=DARKGRAY)
    for building in buildings:
        # print(building)
        app.rect(building['x'], building['y'], building['width'], building['height'], filled_color=building['color'])
    player.show()
    app.line(int(camera.target[0]), -app.height*10, int(camera.target[0]), app.height*10, stroke_color=(0, 255, 0), stroke_width=1)
    app.line(-app.width*10, camera.target[1], app.width*10, camera.target[1], stroke_color=(0, 255, 0), stroke_width=1)
    # app.line(0, 0, app.width, app.height, stroke_color=(0, 255, 0), stroke_width=1 )
    app.end_camera()

    app.rect(0, 0, app.width, 5, filled_color=RED)
    app.rect(0, 5, 5, app.height - 10, filled_color=RED)
    app.rect(app.width - 5, 5, 5, app.height - 10, filled_color=RED)
    app.rect(0, app.height - 5, app.width, 5, filled_color=RED)
    app.text("Free 2d camera controls:", 20, 20, 10, text_color= BLACK)
    app.text("- A / D to move Offset", 40, 40, 10, text_color=DARKGRAY)
    app.text("- Mouse Wheel to Zoom in-out", 40, 60, 10, text_color=DARKGRAY)
    app.text("- W / S to Rotate", 40, 80, 10, text_color=DARKGRAY)
    app.text("- R to reset Zoom and Rotation", 40, 100, 10, text_color=DARKGRAY)

    # app.text("SCREEN AREA", 30, 400, 20, text_color=RED)
    app.text(f"PLAYER: {player.x}, {player.y}", 30, 350, 16, text_color=RED)
    app.text(f"ROTATE: {camera.rotation}", 30, 370, 16, text_color=RED)
    app.text(f"ZOOM: {camera.zoom}", 30, 390, 16, text_color=RED)

app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)

app.run()
