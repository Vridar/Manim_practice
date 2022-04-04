from re import S
from tokenize import group
from manim import *

class NameOfAnimation(Scene) :
    def construct(self):
        
        box = Rectangle(stroke_color = GREEN_A, stroke_opacity=0.9,
        fill_color = BLUE_A, fill_opacity=0.7, height=1, width=1)

        dot1 = always_redraw(lambda : Dot().move_to(box.get_center()))

        tri=Triangle(stroke_color = PURPLE, stroke_opacity=0.7,
        fill_color = RED_A, fill_opacity=0.5)

        dot2 = always_redraw(lambda : Dot().move_to(tri.get_center()))

        cir=Circle(stroke_color = GOLD_A, stroke_opacity=0.7,
        fill_color = ORANGE, fill_opacity=0.5, radius=0.5)

        dot3 = always_redraw(lambda : Dot().move_to(cir.get_center()))

        numberplane = NumberPlane()
        
        code = Code("m6.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
        tab_width = 2, line_spacing = 0.3, font="Monospace").set_width(6).to_edge(UL, buff=0)
        

        self.play(FadeIn(numberplane), Write(code), run_time=6)

        self.add(box, dot1)
        self.play(FadeIn(box,dot1), run_time=1.5)
        self.play(box.animate.shift(RIGHT*2), run_time=1.5)
        self.play(box.animate.shift(UP*2.4), run_time=1.5)
        self.play(box.animate.shift(LEFT*4.2+DOWN*3.8),run_time=2)
        self.play(box.animate.shift(UP*3+RIGHT*2.5),run_time=1.2)

        self.add(tri, dot2)
        self.play(FadeIn(tri, dot2), run_time=1.5)
        self.play(tri.animate.shift(UP*2), run_time=1.5)
        self.play(tri.animate.shift(RIGHT*2.4), run_time=1.5)
        self.play(tri.animate.shift(DOWN*4.2+RIGHT*1.8),run_time=1.5)
        self.play(tri.animate.shift(LEFT*3+UP*2.5),run_time=1.2)

        self.add(cir, dot3)
        self.play(FadeIn(cir, dot3), run_time=1.5)
        self.play(cir.animate.shift(LEFT*1), run_time=1.5)
        self.play(cir.animate.shift(DOWN*1.5), run_time=1.5)
        self.play(cir.animate.shift(RIGHT*4.2+DOWN*3.8),run_time=1.5)
        self.play(cir.animate.shift(UP*2.7+LEFT*8.8),run_time=1.2)

        self.wait()