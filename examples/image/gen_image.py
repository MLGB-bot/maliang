from maliang import Maliang

app = Maliang(width=300, height=300)

img_color = app.gen_image_color(100, 100, color=(200, 200, 200))
img_checked = app.gen_image_checked(100, 100, color1=(255, 255, 255), color2=(0, 0, 0), checksx=10, checksy=10)
img_cellular = app.gen_image_cellular(100, 100, tile_size=10)

img_gradient_v = app.gen_image_gradient_v(100, 100, color1=(255, 255, 255), color2=(0, 0, 0))
img_gradient_h = app.gen_image_gradient_h(100, 100, color1=(255, 255, 255), color2=(0, 0, 0))
img_gradient_radial = app.gen_image_gradient_radial(100, 100, color1=(0, 0, 0), color2=(255, 255, 255), density=0.5)

img_white_noise = app.gen_image_white_noise(100, 100, factor=0.5)


def on_setup():
    app.image(img_color, 0, 0, 100, 100)
    app.image(img_checked, 100, 0, 100, 100)
    app.image(img_cellular, 200, 0, 100, 100)

    app.image(img_gradient_v, 0, 100, 100, 100)
    app.image(img_gradient_h, 100, 100, 100, 100)
    app.image(img_gradient_radial, 200, 100, 100, 100)

    app.image(img_white_noise, 0, 200, 100, 100)


def on_exit():
    for img in (img_color, img_checked, img_cellular,
                img_gradient_v, img_gradient_h, img_gradient_radial,
                img_white_noise):
        img.unload()
        img.unload_texture()


app.regist_event('on_setup', on_setup)
app.regist_event('on_exit', on_exit)
app.run()