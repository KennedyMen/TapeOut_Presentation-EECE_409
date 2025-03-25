import sys
import numpy as np
from manim import *
from PIL import Image
from manim_slides import Slide

class ImageGrid(Scene):
    def construct(self):
        start_img = Image.open("/home/deck/Documents/Projects/Python/Presentation_manim/media/images/image_Processing/Hollow.png").convert('L')
        color_img = ImageMobject("media/images/image_Processing/Hollow.png")
        img = ImageMobject(np.array(start_img))
        self.add(img)
        self.wait(0.5)
        self.play(img.animate.scale(18))
        self.wait(0.5)
        self.play(img.animate.shift(LEFT*5))

