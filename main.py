import sys

import numpy as np
from manim import *
from numpy import asarray
from PIL import Image


class ImageGrid(Scene):
    def construct(self):
        img = ImageMobject("images/HollowRed.png")
        self.add(img)
