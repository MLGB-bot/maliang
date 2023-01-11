弧(arc)
=====================

.. _arc.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/arc.py


::

    arc(x: float, y: float, w: float, h: float, start_angle: float, end_angle: float, segments: int=30, shape: int=1)


* 参数 ::

    x  中心x坐标
    y  中心y坐标
    w  椭圆的宽
    h  椭圆的高
    start_angle  起始角度
    end_angle    终止角度
    segments     弧段数
    shape        1/2/3/4 形状 >>> maliang.ArcShape


.. attention::
    ellipse_mode()处的改动对arc()同样生效, 即:环(arc)与圆(ellipse)共享ellipse_mode()

* arc.py_

.. image:: /_static/examples/shapes/2D/arc.png
.. literalinclude:: ../../../../../examples/shapes/2D/arc.py
    :language: python
    :linenos:

* 示例 ::

    arc(150, 150, 240, 200, 0, 45, stroke_width=2, stroke_color=(0, 255, 0), filled_color=(255, 0, 0))

