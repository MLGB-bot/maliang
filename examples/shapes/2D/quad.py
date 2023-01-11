from maliang import Maliang
import raylib as rl

app = Maliang()

def on_draw():
    rl.rlBegin(0x0007)
    rl.rlColor4f(1, 1, 1, 1)
    rl.rlVertex2f(30, 76)
    rl.rlVertex2f(69, 63)
    rl.rlVertex2f(86, 20)
    rl.rlVertex2f(38, 31)
    rl.rlEnd()

app.regist_event('on_draw', on_draw)
app.run()