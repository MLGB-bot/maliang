import random

from maliang import Maliang
from maliang.structs import MImage

app = Maliang(width=500, height=400, buffer_proxy=True, fps=0)
app.set_static_relative_dir('../../resources/')

text = "落霞与孤鹜齐飞\n秋水共长天一色"
text_en = "How are you?\nI am Fine, thank you! and you?"

font = app.load_font(filename="fonts/LXGWWenKaiLite-Regular.ttf", )


def on_draw():
    app.background(255)
    app.text(text_en, 0, 0, text_size=12)
    app.text(text, 0, 40, text_size=18)
    app.text(text_en, 0, 90, text_size=24, font=font)
    app.text(text, 0, 160, text_size=30, font=font)
    # app.text(text, random.randint(0, app.width), random.randint(0, app.height), text_size=random.randint(12, 50),
    #          font=font, space_x=1)
    app.draw_fps(0, app.height-20)

app.regist_event("on_draw", on_draw)

app.run()
