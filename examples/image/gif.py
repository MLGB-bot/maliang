from maliang import Maliang
from maliang.units import GifPlayer


app = Maliang(width=500, height=400, fps=0)
app.set_static_relative_dir('../resources/')

gif = app.load_gif('img/real_fighter.gif', fps_delay=60)
gif_player1 = GifPlayer(fps_delay=120, loop=1)
gif_player2 = GifPlayer(fps_delay=240, loop=2)
gif_player3 = GifPlayer(fps_delay=480, loop=3)

def on_draw():
    app.background(255)
    app.image(gif, 0, 0, )
    # app.image(gif, 0, 200, )
    app.image(gif, 310, 10, 180, 120, gif_player=gif_player1)
    app.image(gif, 310, 140, 180, 120, tint_color=(255, 100), gif_player=gif_player2)
    app.image(gif, 310, 270, 180, 120, tint_color=(255, 0, 0), gif_player=gif_player3)

def on_exit():
    gif.unload()
    gif.gif_player.unload()
    gif_player1.unload()
    gif_player2.unload()
    gif_player3.unload()

app.regist_event('on_draw', on_draw)
app.regist_event('on_exit', on_exit)
app.run()