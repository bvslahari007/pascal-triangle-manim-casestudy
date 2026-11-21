from manim import *

class PascalTitle(Scene):
    def construct(self):
        # Set the font to Times New Roman
        Text.set_default(font="Times New Roman")
        
        # Create the complete text with different colors
        full_text = Text(
            "Let's Discover the Secret Patterns Inside Pascal's Triangle",
            font_size=48,
            # Color different parts of the text
            t2c={
                "Let's Discover": WHITE,
                "the Secret Patterns": YELLOW,
                "Inside Pascal's Triangle": BLUE
            }
        )
        
        # Animate the entire text appearing at once with a smooth fade-in
        self.play(FadeIn(full_text, scale=1.2))
        self.wait(1)
        
        # Add a subtle underline that grows beneath the text
        underline = Line(LEFT, RIGHT, color=WHITE).next_to(full_text, DOWN, buff=0.3)
        underline.width = 0  # Start with zero width
        
        # Correct animation syntax - using animate.set_width() instead of assignment
        self.play(
            underline.animate.set_width(full_text.width),  # Correct way to animate width
            run_time=1.5
        )
        self.wait(1)