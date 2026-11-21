from manim import *

class PascalTriangleStart(Scene):
    def construct(self):
        # Define colors
        faded_color = GRAY
        main_color = WHITE
        
        # Create Pascal's Triangle first few rows
        pascal_rows = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        elements = []
        
        for i, row in enumerate(pascal_rows):
            row_elements = []
            for j, num in enumerate(row):
                tex = MathTex(str(num)).scale(1.5)
                tex.move_to(RIGHT * (j - i / 2) * 1.2 + DOWN * i * 1.2)
                row_elements.append(tex)
                self.add(tex)
            elements.append(row_elements)
        
        self.wait(2)
        
        # Create a VGroup for the full Pascal's Triangle
        triangle_group = VGroup(*[num for row in elements for num in row])
        
        # Zoom into the top "1" while fading the background triangle
        one = elements[0][0]
        self.play(triangle_group.animate.set_opacity(0.2), one.animate.scale(3))  # Fade and zoom effect
        self.wait(1)
        
        # Position faded "0"s around it
        left_zero = MathTex("0", color=faded_color).scale(2).next_to(one, LEFT, buff=0.9)
        right_zero = MathTex("0", color=faded_color).scale(2).next_to(one, RIGHT, buff=0.9)
        
        # Plus signs beside 1s to show addition
        plus_left = MathTex(r"+").scale(1.5).next_to(left_zero, RIGHT, buff=0.3)
        plus_right = MathTex(r"+").scale(1.5).next_to(one, RIGHT, buff=0.2)
        
        # Animate faded "0"s and plus signs appearing
        self.play(FadeIn(left_zero, shift=LEFT), FadeIn(right_zero, shift=RIGHT))
        self.play(Write(plus_left), Write(plus_right))
        
        # Explanation text about adding zeroes
        explanation_text = Tex(
            r"The zeroes act as placeholders, ensuring the addition rule stays consistent.\\ "
            r"Each number is the sum of the two above it.\\ "
            r"The edges stay 1 because $1 + 0 = 1$ and $0 + 1 = 1$."
        ).scale(0.8)
        explanation_text.next_to(one, UP, buff=1.5)
        
        self.play(Write(explanation_text))
        self.wait(2)
