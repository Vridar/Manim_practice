from manim import *

class frac(Scene):
    def construct(self):

        rectangle = RoundedRectangle(stroke_width = 6, stroke_color = WHITE,
        fill_color = BLUE_B, width = 14, height = 2)

        mathtext = MathTex("\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)").set_color_by_gradient(DARK_BROWN, BLUE).set_height(1.5)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center()))

        self.play(FadeIn(rectangle))
        self.wait()
        self.play(Write(mathtext), run_time=2)
        self.wait()

        self.play(rectangle.animate.shift(RIGHT*2.5+DOWN*2), run_time=3)
        self.wait()
        self.play(rectangle.animate.shift(LEFT*2.3 + UP*3.8), run_time=3)
        self.wait()
