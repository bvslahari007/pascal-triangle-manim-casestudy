from manim import *

class demo(Scene):
    def construct(self):
        t = Text("hello").shift(UP)
        t2 = Text("hello").shift(DOWN)
        self.play(Write(t),Write(t2))
        self.wait(3)