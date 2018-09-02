import unittest
import numpy as np
from contextfree.contextfree import init, get_npimage, write_to_png, report, check_limits
from contextfree.contextfree import circle, box, line, triangle
from contextfree.contextfree import translate, color, scale, rotate, flip_y


class Tests(unittest.TestCase):

    def test_main(self):
        init(face_color="#123456", background_color="#aaaaaa")
        circle(1)
        a = get_npimage()
        print(a.shape)
        report()
        write_to_png("/tmp/test.png")

    def test_primitives(self):
        init(face_color="#123456", background_color="#aaaaaa")
        line(1, 1)
        triangle(0.5)
        a = get_npimage()
        print(a.shape)
        report()
        write_to_png("/tmp/primitives.png")

    def test_color(self):
        init(face_color="#123456", background_color="#aaaaaa")
        with scale(0.7):
            circle(0.5)
            with translate(0.5, 0.5):
                with color(alpha=1, hue=0.2):
                    circle(0.5)
            with translate(0.5, -0.5):
                with scale(0.6):
                    with color(alpha=0.7, hue=0):
                        circle(0.5)

        write_to_png("/tmp/color.png")

    def test_rotate(self):
        init()
        with rotate(0.1):
            box(0.5)
        write_to_png("/tmp/rotate.png")
        a = get_npimage()
        self.assertIsInstance(a, np.ndarray)

    def test_flip(self):
        init()
        with flip_y():
            box(0.5)
        a = get_npimage(y_origin="bottom")
        self.assertIsInstance(a, np.ndarray)

    def test_scale_limit(self):
        @check_limits
        def element():
            circle(0.1)
            with translate(0.2, 0):
                with scale(0.5, 0.4):
                    with scale(0.5):
                        element()

        init()
        element()
        write_to_png("/tmp/scale.png")