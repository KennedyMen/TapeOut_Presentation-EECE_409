import sys
import numpy as np
from manim import *
from PIL import Image
from manim_slides import Slide

class ImageGrid(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        start_img = Image.open("/home/deck/Documents/Projects/Python/Presentation_manim/media/images/image_Processing/Hollow.png").convert('L')
        color_img = ImageMobject("media/images/image_Processing/Hollow.png")
        self.add(color_img)
        self.wait(0.5)
        self.play(color_img.animate.scale(18))
        self.wait(0.5)
        self.play(color_img.animate.shift(LEFT*5))
        #setting up the grayscale image for being moved around 
        grayscale_img = ImageMobject(np.array(start_img))
        grayscale_img.height = 4
        grayscale_img.move_to(RIGHT * 5 + UP * 2.5)
        #This is space dedicated to being worked on later 
        #all stages of processing will be placed here and presented
        #i want to make sure all the outputs come from the verilog code itself

        Outputs = [
                FadeIn(grayscale_img, target_position= color_img , scale= .25)
        ]
        self.play(AnimationGroup(*Outputs))
        grayscale_text = Text('Grayscale', font_size=23).next_to(grayscale_img, UP)
        self.play(FadeIn(grayscale_text))
