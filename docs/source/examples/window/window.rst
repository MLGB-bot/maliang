窗口 (window)
====================


.. _window.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/window/window.py


* window.py_

.. image:: /_static/examples/window/window.png
.. literalinclude:: ../../../../examples/window/window.py
    :language: python
    :linenos:

::

    Maliang(
        width:int =100,         # 窗口宽度
        height: int =100,       # 窗口高度
        title: str ='',         # 窗口标题
        buffer_proxy: bool=False,   # 是否使用texture作为窗口管理模块DoubleBuffer的代理层
        fps: int=0,            # 窗口刷新帧率(每秒钟刷新次数), 0代表cpu所能达到的上限
        background_color: tuple=(235, 235, 235, 255),  # 窗口默认背景颜色
        fullscreen: bool=False # 是否全屏
    )




* 示例 ::

    Maliang(0, 0)
    Maliang(0, 0, fullscreen=True)
    Maliang(200, 150, "MaLiang", double_buffer=False, fps=30, background_color=(255, 200, 155), fullscreen=False)
    Maliang(1024, 768, "MaLiang", double_buffer=True, fps=60, background_color=(255, 200, 155), fullscreen=True)

