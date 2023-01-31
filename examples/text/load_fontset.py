from maliang import Maliang

app = Maliang(width=500, height=400)
app.set_static_relative_dir('../resources/')


text = "How are you?\nI am Fine, thank you! and you?\n" \
       "落霞与孤鹜齐飞\n秋水共长天一色"

not_repeated_words = ''.join(list(set(text)))

fontset = app.load_fontset(filename="fonts/LXGWWenKaiLite-Regular.ttf", fontsize=24, words=not_repeated_words )

def on_draw():
    app.background(255)
    app.text(text, 0, 0, font_size=16, font=fontset)
    app.text(text, 0, 90, font_size=24, font=fontset, text_color=(255, 0, 0))
    app.text(text, 0, 220, font_size=32, font=fontset)

def on_exit():
    fontset.unload()

app.regist_event("on_draw", on_draw)
app.regist_event("on_exit", on_exit)

app.run()
