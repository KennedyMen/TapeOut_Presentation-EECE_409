import sys
from manim.utils import images
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
        color_img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        self.add(color_img)
        self.wait(0.5)
        self.play(color_img.animate.scale(18))
        self.wait(0.5)
        self.play(color_img.animate.shift(LEFT*5))
        #setting up the grayscale image for being moved around 
        grayscale_img = ImageMobject(np.array(start_img))
        grayscale_img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
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

class UART(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        self.convert_image_to_binary()
    
    def convert_image_to_binary(self):
        def HEX_conv(Gray):
            # Normalize grayscale value to 0-1 range for color
            normalized_gray = Gray 
            return ManimColor.from_rgb((normalized_gray, normalized_gray, normalized_gray))
        
        # Open the image and convert to grayscale
        start_img = Image.open("/home/deck/Documents/Projects/Python/Presentation_manim/media/images/image_Processing/Hollow.png").convert('L')
        
        # Create ImageMobject
        image = ImageMobject(np.array(start_img))
        image.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        image.height = 7
        image.move_to(LEFT*5)
        
        self.play(FadeIn(image))
        
        # Get pixel array and dimensions
        image_array = image.get_pixel_array()
        img_height, img_width = image_array.shape[:2]
        
        # Create grid of squares
        grid = VGroup()
        for x in range(img_width):
            for y in range(img_height):
                # Get grayscale value and convert to color
                gray_value = image_array[y, x]  # Note: swap x and y to match image indexing
                
                # Create square with color based on grayscale value
                square = Square(
                    color=HEX_conv(gray_value), 
                    fill_color=HEX_conv(gray_value),
                    fill_opacity=1,
                    side_length=0.15
                ).move_to(
                    image.get_corner(UL) + 
                    np.array([x * image.width/img_width, -y * image.height/img_height, 0])
                )
                grid.add(square)
        
        # Animate grid creation
        self.play(Create(grid))
        self.wait(2)
