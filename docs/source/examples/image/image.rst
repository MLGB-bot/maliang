展示图片 image()
==============================

::

    image(
        img: MImage,
        x: int, # 顶点x坐标
        y: int, # 顶点y坐标
        w=0,    # 展示宽度
        h=0,    # 展示高度
        mode=None,  # from maliang.units import ImageMode
        gif_player=None,    # 展示gif动态图片的时候 额外传入
        tint_color=(255, 255, 255, 255)     # 渲染染色 白色为保持原始图片颜色
    )

------------------------------

.png
-----------------

.. _png.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/image/png.py

* png.py_

.. literalinclude:: ../../../../examples/image/png.py
    :language: python
    :linenos:


注释::

    app.set_static_relative_dir('../resources/')

作用: 设置当前静态文件文件夹的相对路径(相对于os.getcwd())

注释::

    logo = app.load_image('img/logo_300x250.png')

作用: 加载图片文件. 此时读取的文件路径为:  ../resources/img/logo_300x250.png
    logo -> class Mimage


------------------------------

.gif
-------------------------

.. _gif.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/image/gif.py

* gif.py_

.. literalinclude:: ../../../../examples/image/gif.py
    :language: python
    :linenos:


注释::

    gif = app.load_gif('img/real_fighter.gif', fps_delay=60)

作用::

    load_gif(
        filename,       # 文件名称
        fps_delay=0,    # 动图每一帧播放之间间隔多少帧(image()每调用一次为一帧).
        loop=0          # 动图播放次数 0.无限循环播放 1.播放1次 2播放2次 ...
    )


* GifPlayer()

::

    GifPlayer(
        fps_delay=0,    # 动图每一帧播放之间间隔多少帧(on_draw每循环一次为一帧).
        loop=0          # 动图播放次数 0.无限循环播放 1.播放1次 2播放2次 ...
    )

每当load_gif执行的时候, MImage对象会自动创建一个属性"self.gif_player", 为GifPlayer()对象的一个实例,
gif动态图片的播放就是通过这个实例来控制的.

.. attention::
    如果查看源代码就会发现,
    因为image()展示动图时候, 每一次调用都是相当于一帧来处理的, 倘若共用一个GifPlayer对象, 会造成动图播放速度的加快,属于"跳帧"的问题.

    ::

        def on_draw():
            image(gif)
            image(gif)

    此时gif的播放共用的是同一个GifPlayer对象, 两个image()函数会轮流展示下一帧.产生"跳帧"播放的问题.

    想像这么一个场景: 一颗炮弹的爆炸效果, 我们希望同类型的炮弹无论何时爆炸, 无论爆炸多少颗, 每一颗之间的威力与持续时间都应是一样的.
    不应该因为同时打出两枚炮弹,就导致两枚炮弹的爆炸时间同时缩短为原来的一半.

    为了解决此问题, 创建了GifPlayer对象.通过额外的对象管理播放效果.

    当有需要不同的速度\循环次数等需求播放同一张gif图片素材的时候, 引入预先创建好的gif_player对象即可.

    ::

        gif_player1 = GifPlayer(fps_delay=120, loop=1)
        gif_player2 = GifPlayer(fps_delay=240, loop=2)
        def on_draw():
            # 此时gif图片会使用传入的gif_player1/gif_player2来替代默认的gif.gif_player对象进行播放
            image(gif, gif_player=gif_player1)
            image(gif, gif_player=gif_player2)

    另外:

    GifPlayer()只是为了满足gif播放所做的一个拓展对象, 如果有其余不同的播放效果需求,完全可以自定义新的对象以替代,
    比如当前对象是通过"image调用"间隔来控制gif图片的播放速度, 可以重构以直接通过"时间"间隔来控制.等