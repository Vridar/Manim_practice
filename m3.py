from manim import*

class SquareToCircle(Scene):
    def construct(self):
        triangle = Triangle()  
        triangle.set_fill(PINK, opacity=0.3) 

        square = Square()  
        square.rotate(PI / 4) 

        circle = Circle()  
        circle.rotate(PI / 2)  

        self.play(Create(square))  
        self.play(Transform(square, triangle))  
        self.play(ReplacementTransform(square, circle))
        self.play(
            circle.animate.set_fill(GREEN, opacity=0.7)
        )
        self.play(FadeOut(square))