from manim import *

class PascalNamed(Scene):
    def construct(self):
        # Set default font for Text mobjects
        Text.set_default(font="Times New Roman")
        
        # Left side: Definition - Using Text instead of Tex for Times New Roman
        definition = VGroup(
            Text("Pascal's Triangle", font_size=36, color=BLUE),
            Text("• Each number is the sum", font_size=30),
            Text("  of the two above it", font_size=30),
            Text("• Starts/ends with 1", font_size=30),
            Text("• Named after", font_size=30),
            Text("Blaise Pascal", font_size=30, color=YELLOW),
            Text("(Known earlier to:\nYang Hui, al-Karaji, Pingala)", 
                font_size=20, 
                color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT*3.5)

        # Right side: Triangle (6 rows)
        rows = [
            [1], 
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ]
        
        triangle = VGroup()
        for row in rows:
            row_group = VGroup()
            for num in row:
                font_size = 28 if num < 10 else 24
                num_text = Text(str(num), font_size=font_size)
                row_group.add(num_text)
            row_group.arrange(RIGHT, buff=0.5)
            triangle.add(row_group)
        
        triangle.arrange(DOWN, aligned_edge=ORIGIN, buff=0.4).shift(RIGHT*3)
        
        # Animation
        self.play(
            FadeIn(definition, shift=RIGHT),
            LaggedStart(
                *[FadeIn(num, scale=0.7) for row in triangle for num in row],
                lag_ratio=0.1
            )
        )
        self.wait(5)