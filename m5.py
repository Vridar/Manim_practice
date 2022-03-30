from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1).set_color(GREEN)
        framebox2 = SurroundingRectangle(text[3], buff = .1).set_color(BLUE)
        self.play(
            FadeIn(framebox1),
            Create(framebox1),
            
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()