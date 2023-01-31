字体 (Font)
============================

Maliang默认字体无法展示象形文字, 如中文, 更多时候我们需要使用自定义的字体文件,以满足开发需求


-----------------------------

load_font()
-----------------------------


.. _load_font.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/text/load_font.py


::

    load_font(
        filename='',    # 字体文件路径
        filetype='.ttf' # 字体格式 支持freetype/truetype, 默认为".ttf"
    )


* load_font.py_

.. image:: /_static/examples/text/load_font.png
.. literalinclude:: ../../../../examples/text/load_font.py
    :language: python
    :linenos:


-----------------------------

load_fontset()
----------------------------

开发过程中, 往往::

    1.只需要展示部分文字
    2.文字的大小(font_size)是一致的

满足这两个条件的情况之下, 推荐使用load_fontset()以获取更高的性能


.. _load_fontset.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/text/load_fontset.py


::

    load_fontset(
        filename='',    # 字体文件路径
        fontsize=32,    # 字体文件大小
        words=''        # 文本.仅会展示存在于words中的文字
    )


* load_fontset.py_

.. image:: /_static/examples/text/load_fontset.png
.. literalinclude:: ../../../../examples/text/load_fontset.py
    :language: python
    :linenos:


注释::

    fontset = app.load_fontset(filename="fonts/LXGWWenKaiLite-Regular.ttf", fontsize=24, words=not_repeated_words )

这行代码加载了字体"LXGWWenKaiLite-Regular.ttf", 并且指定了字体大小24.

当使用text渲染文本的时候, 可以发现当font_size为16/24/32的时候都可以展示, 似乎没有问题.
但是如果仔细观察就会发现, 仅仅等于24的时候, 文字才足够饱满, 其余两种文字有不少瑕疵, 或模糊不清, 或展示不全

无论是>24或者<24, 渲染出来的文字总是"存有杂质", 这就是load_fontset()中参数"fontsize"的作用.


-----------------------------

自定义字体渲染引擎 [FontEngine]
-----------------------------

自定义字体渲染引擎, 是maliang保留的功能. 当不满足于马良提供的文本渲染功能的时候, 可以自定义一套渲染逻辑.
一个最基础的引擎对象应该至少满足如下结构:


.. literalinclude:: ../../../../examples/text/engine_basic.py
    :language: python
    :linenos:


如下是一个使用pillow渲染文字的例子 [仅仅是demo, 建议不要用于生产环境]:

.. _font_engine.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/text/font_engine.py

* font_engine.py.py_

.. literalinclude:: ../../../../examples/text/font_engine.py
    :language: python
    :linenos:

