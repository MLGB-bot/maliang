背景色(background)
=========================

设置窗口的背景颜色

Maliang使用的是RGBA格式的颜色格式, 由四个[0, 255]区间范围内的整数依次分别代表红(R), 绿(G), 蓝(B), 透明度(A).

::

    background(r, g, b, a)



.. _background.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/ahead/background.py

* background.py_

.. image:: /_static/examples/ahead/background.png
.. literalinclude:: ../../../../examples/ahead/background.py
    :language: python
    :linenos:

* 参数::

    background使用的是形参, 可以传入以下几种格式的参数,以及其代表的意义见下方

    background(i)          #  (i, i, i, 255)
    background(i, a)       #  (i, i, i, a)
    background(r, g, b)    #  (r, g, b, 255)
    background(r, g, b, a) #  (r, g, b, a)


