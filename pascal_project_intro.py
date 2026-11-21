from manim import *

class ProjectPresentation(Scene):
    def construct(self):
        # Explicitly set background (though black is default)
        self.camera.background_color = BLACK
        
        # Create text elements with simpler formatting
        title = Text("Visualizing Hidden Patterns", 
                   font_size=48, 
                   color="#FFD700").to_edge(UP)
        
        subtitle = Text("of Pascal's Triangle using MANIM", 
                      font_size=36, 
                      color="#FFD700").next_to(title, DOWN)
        
        details = VGroup(
            Text("Case Study for PPS2", font_size=28),
            Text("(Programming for Problem Solving 2)", font_size=24),
            Text("Faculty: Prasad Kaviti", font_size=24, color="#6ECBFF"),
            Text("Section: K", font_size=24, color="#6ECBFF")
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(subtitle, DOWN, buff=1)
        
        # Simpler animation sequence
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(LaggedStart(
            FadeIn(details[0]),
            FadeIn(details[1]),
            FadeIn(details[2]),
            FadeIn(details[3]),
            lag_ratio=0.3
        ))
        self.wait(2)