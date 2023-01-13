from maliang import Maliang
import random

app = Maliang(fps=1)

def on_draw():
    app.resize(random.randint(100, 300), random.randint(100, 300))
    app.background(255)

app.regist_event("on_draw", on_draw)

app.run()
