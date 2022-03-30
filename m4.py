from turtle import left
from manim import *

class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(3)
        image.background_rectangle = SurroundingRectangle(image, RED_A)
        self.add(image, image.background_rectangle)
        self.play(
            FadeOut(image),
            FadeOut(image.background_rectangle),
            FadeIn(image, shift=LEFT, run_time=3),
            FadeIn(image.background_rectangle, shift=LEFT, run_time=3),
            )
        self.wait