from manim import *

class ManimVridarLogo(Scene):
    def construct(self):
        self.camera.background_color = "black"
        logo_green = "#853c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_vridar = MathTex(r"\mathbb{Vridar}", fill_color=logo_black).scale(5)
        ds_vridar.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=3).shift(RIGHT)
        square = Square(color=logo_blue, fill_opacity=2).shift(DOWN)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(UP)
        logo = VGroup(triangle, square, circle, ds_vridar)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
        
        # success second one