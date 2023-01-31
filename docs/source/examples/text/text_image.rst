文本->图片 text_image()
=============================

.. warning::

    text_image()生成的文字图片应该与text()一致, 但经测试发现并非如此, 这可能是raylib当前版本自身的bug, 并不影响使用

    另外, 如果渲染文本较多的话, 相较于text()实时输出文字, text_image()预先生成图片对象, 仅展示图片理应有更高的性能.

.. _text_image.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/text/text_image.py


::

    text_image(
        text: string,   # 文本
        text_size: int=None,     # 文字大小
        text_color: MColor=None, # 文字颜色
        font: MFont|MFontSet = None,    # 字体
        space_x=1,  # 文本横向间隔
    )


* text_image.py_

.. image:: /_static/examples/text/text_image.png
.. literalinclude:: ../../../../examples/text/text_image.py
    :language: python
    :linenos:
