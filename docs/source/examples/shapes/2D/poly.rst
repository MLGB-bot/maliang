正多边形(poly)
=====================

.. _poly.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/poly.py


::

    poly(x: float, y: float, r: float, sides: int, rotation: float)


* 参数 ::

    x  中心x坐标
    y  中心y坐标
    r  外接圆半径
    sides  多少个边 > 2
    rotation  旋转角度 [顺时针为正, 逆时针为负]


* poly.py_

.. image:: /_static/examples/shapes/2D/poly.png
.. literalinclude:: ../../../../../examples/shapes/2D/poly.py
    :language: python
    :linenos:

* 示例 ::

    poly(50, 50, 30, 5, rotation=20, stroke_width=2, stroke_color=(0, 255, 0), filled_color=(255, 0, 0))

