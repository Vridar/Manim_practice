from manim import *

class ManimVridarLogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_vridar = MathTex(r"\mathbb{VRIDAR}", fill_color=logo_black).scale(5)
        ds_vridar.shift(2.25 * LEFT + 1.2 * UP)
        circle = Circle(color=logo_green, fill_opacity=12).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=18).shift(DOWN)
        triangle = Triangle(color=logo_red, fill_opacity=15).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_vridar)
        logo.move_to(ORIGIN)
        self.add(logo)
        
        # success second one maybe not