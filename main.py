import manim
import numpy
from manim import *
class ImageGrid(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("path/to/your/image.png")
        image.scale(0.5)  # Scale the image to fit the scene

        # Create a grid
        rows, cols = 16, 16
        grid = VGroup()
        for i in range(rows):
            for j in range(cols):
                rect = Square(side_length=image.get_height() / rows)
                rect.set_stroke(WHITE, width=1)
                rect.move_to(
                    image.get_corner(UL)
                    + np.array([rect.get_width() * j, -rect.get_height() * i, 0])
                )
                grid.add(rect)

        # Add the image and grid to the scene
        self.add(image, grid)


if __name__ == "__main__":
    from manim import config

    config.media_width = "100%"
    config.quality = "high_quality"
    scene = ImageGrid()
    scene.render()
