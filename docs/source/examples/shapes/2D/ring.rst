环(ring)
=====================

.. _ring.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/ring.py


::

    ring(x: float, y: float, d_in: float, d_out: float, start_angle: float=0, end_angle: float=360)



* 参数 ::

        x  圆心x坐标
        y  圆心y坐标
        d_in  内圆直径
        d_out 外圆直径
        start_angle 起始角度
        end_angle   终止角度



.. attention::
    circle_mode()处的改动对ring()同样生效, 即:环(ring)与圆(circle)共享circle_mode()


* ring.py_

.. image:: /_static/examples/shapes/2D/ring.png
.. literalinclude:: ../../../../../examples/shapes/2D/ring.py
    :language: python
    :linenos:


* 示例 ::

    ring(50, 50, 60, 80, 0, 360)
    ring(50, 50, 60, 80, 0, 360, stroke_width=4)
    ring(50, 50, 60, 80, 0, 90, stroke_color=(255, 0, 0))
    ring(50, 50, 60, 80, 0, 90, stroke_width=2, stroke_color=(0, 255, 0), filled_color=(255, 0, 0))

    ring(50, 50, 60, 80)
    ring(50, 50, 60, 80, mode=CircleMode.CORNER)
    ring(50, 50, 60, 80, mode=CircleMode.CENTER)
    ring(50, 50, 60, 80, mode=CircleMode.RADIUS)

