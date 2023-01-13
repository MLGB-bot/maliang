from maliang import Maliang

app = Maliang()

def on_draw():
    print("i am on_draw")

app.regist_event("on_draw", on_draw)

app.run()
