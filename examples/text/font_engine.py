
from maliang import Maliang
from maliang.exts.font.engine_pillow import FontEnginePillow

app = Maliang(width=500, height=400)
app.set_static_relative_dir('../resources/')

font = app.load_font(filename="fonts/LXGWWenKaiLite-Regular.ttf", engine=FontEnginePillow)

text = "How are you?\nI am Fine, thank you! and you?\n" \
       "落霞与孤鹜齐飞\n秋水共长天一色"

def on_draw():
    app.background(255)
    app.text(text, 0, 0, font_size=12, font=font)
    app.text(text, 0, 90, font_size=18, font=font)

app.regist_event("on_draw", on_draw)
app.run()