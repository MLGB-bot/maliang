展示文本 text()
=============================



.. _text.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/text/text.py


::

    text(
        text: string,   # 文本
        x: float=0,     # 左上角x坐标
        y: float=0,     # 左上角y坐标
        text_size: int=None,     # 文字大小
        text_color: MColor=None, # 文字颜色
        font: MFont|MFontSet = None,    # 字体
        space_x=1,  # 文本横向间隔
    )


* text.py_

.. image:: /_static/examples/text/text.png
.. literalinclude:: ../../../../examples/text/text.py
    :language: python
    :linenos:
