from manim import *
class Video(Scene):
    def construct(self):
        a = Union(*MathTex(r"\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)-\frac{\partial F}{\partial y}=0").copy()[0]).scale(2).set_stroke(width=0).set_fill(opacity=1).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)
        rect = SurroundingRectangle(a, fill_color=WHITE, fill_opacity=0.1, buff=1).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)
        self.add(a,rect)
