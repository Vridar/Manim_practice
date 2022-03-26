from manim import *

class BraceAnnotation(Scene):
    def construct(self) : 
        numberplane = NumberPlane()
        dot = Dot([-3, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(RED_E)
        b1 = Brace(line)
        b1text = b1.get_text("Horizintal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI/ 2).get_unit_vector())
        b2text = b2.get_tex("p_0-p_1")
        self.add(numberplane, line, b1, b2, b1text, b2text, dot, dot2)

        point1 = b1text
        point2 = b2text

        self.play(FadeIn(numberplane), run_time=1.5)
        self.play(Write(point1))
        self.play(Write(point2))
        self.wait()

# third one every day 
# at least do something