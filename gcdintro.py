from manim import *

class GCDTimesNewRoman(Scene):
    def construct(self):
        # Set up professional paper-like background
        self.camera.background_color = "#FFF8E7"
        
        # Title with Times New Roman
        title = Text("Understanding the Greatest Common Divisor",
                    font="Times New Roman",
                    color=BLUE_D,
                    weight=BOLD,
                    font_size=48)
        subtitle = Text("A friendly introduction to GCD",
                       font="Times New Roman",
                       color=GRAY,
                       font_size=28)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Real-world analogy
        analogy_title = Text("A Practical Example:",
                           font="Times New Roman",
                           color=BLACK,
                           weight=BOLD,
                           font_size=36)
        
        analogy_text = Text(
            "Imagine you have two ribbons:\n"
            "One is 18 inches long\n"
            "The other is 24 inches long\n\n"
            "You want to cut them into equal pieces\n"
            "without any leftover material",
            font="Times New Roman",
            color=BLACK,
            font_size=32,
            line_spacing=1.2
        )
        
        analogy_group = VGroup(analogy_title, analogy_text)
        analogy_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(analogy_title))
        self.wait(0.5)
        self.play(Write(analogy_text))
        self.wait(3)
        
        # Visual representation
        self.play(FadeOut(analogy_group))
        
        # Create ribbon visualizations
        ribbon18 = Rectangle(width=4.5, height=0.3, color=RED, fill_opacity=0.6)
        ribbon24 = Rectangle(width=6, height=0.3, color=BLUE, fill_opacity=0.6)
        ribbon_group = VGroup(ribbon18, ribbon24).arrange(DOWN, buff=1)
        
        length18 = Text("18 inches", font="Times New Roman", font_size=24).next_to(ribbon18, UP)
        length24 = Text("24 inches", font="Times New Roman", font_size=24).next_to(ribbon24, UP)
        
        self.play(Create(ribbon18), Create(ribbon24))
        self.play(Write(length18), Write(length24))
        self.wait(2)
        
        # Possible cuts
        possible_title = Text("Possible Equal Divisions:",
                            font="Times New Roman",
                            color=BLACK,
                            weight=BOLD,
                            font_size=36)
        
        possible_text = Text(
            "• 1 inch pieces (18 and 24 pieces)\n"
            "• 2 inch pieces (9 and 12 pieces)\n"
            "• 3 inch pieces (6 and 8 pieces)\n"
            "• 6 inch pieces (3 and 4 pieces)",
            font="Times New Roman",
            color=BLACK,
            font_size=30,
            line_spacing=1.2
        )
        
        possible_group = VGroup(possible_title, possible_text)
        possible_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(FadeOut(ribbon_group), FadeOut(length18), FadeOut(length24))
        self.play(Write(possible_title))
        self.wait(0.5)
        self.play(Write(possible_text))
        self.wait(3)
        
        # Highlight GCD
        gcd_highlight = Text(
            "The largest possible equal division is 6 inches",
            font="Times New Roman",
            color=GREEN_D,
            weight=BOLD,
            font_size=32
        )
        
        gcd_def = Text(
            "This is the Greatest Common Divisor (GCD)\n"
            "of 18 and 24",
            font="Times New Roman",
            color=BLUE_D,
            font_size=32,
            line_spacing=1.2
        )
        
        self.play(possible_group.animate.shift(UP))
        self.play(Write(gcd_highlight.next_to(possible_group, DOWN, buff=0.7)))
        self.wait(2)
        self.play(Write(gcd_def.next_to(gcd_highlight, DOWN, buff=0.5)))
        self.wait(3)
        
        # Formal definition
        self.play(FadeOut(possible_group), FadeOut(gcd_highlight), FadeOut(gcd_def))
        
        formal_def = Text(
            "The GCD of two numbers is the largest number\n"
            "that divides both of them without leaving a remainder",
            font="Times New Roman",
            color=BLACK,
            weight=BOLD,
            font_size=36,
            line_spacing=1.2
        )
        
        example = Text(
            "GCD(18, 24) = 6",
            font="Times New Roman",
            color=RED_D,
            weight=BOLD,
            font_size=40
        )
        
        self.play(Write(formal_def))
        self.wait(2)
        self.play(Write(example.next_to(formal_def, DOWN, buff=0.7)))
        self.wait(3)
        
        # Calculation method
        self.play(FadeOut(formal_def), FadeOut(example))
        
        method_title = Text("Finding the GCD:", 
                           font="Times New Roman",
                           color=BLACK,
                           weight=BOLD,
                           font_size=36)
        
        method_steps = Text(
            "1. List all divisors of each number\n"
            "2. Identify the common divisors\n"
            "3. Select the largest common divisor",
            font="Times New Roman",
            color=BLACK,
            font_size=32,
            line_spacing=1.2
        )
        
        method_group = VGroup(method_title, method_steps)
        method_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(method_title))
        self.wait(0.5)
        self.play(Write(method_steps))
        self.wait(3)
        
        # Practical example
        self.play(method_group.animate.shift(UP*1.5))
        
        example_title = Text("Example with 18 and 24:", 
                           font="Times New Roman",
                           color=BLUE_D,
                           font_size=32)
        
        divisors18 = Text("Divisors of 18: 1, 2, 3, 6, 9, 18", 
                         font="Times New Roman",
                         color=BLACK,
                         font_size=28)
        
        divisors24 = Text("Divisors of 24: 1, 2, 3, 4, 6, 8, 12, 24", 
                         font="Times New Roman",
                         color=BLACK,
                         font_size=28)
        
        common = Text("Common divisors: 1, 2, 3, 6", 
                     font="Times New Roman",
                     color=PURPLE_D,
                     font_size=28)
        
        gcd_result = Text("GCD = 6", 
                         font="Times New Roman",
                         color=RED_D,
                         weight=BOLD,
                         font_size=36)
        
        example_group = VGroup(example_title, divisors18, divisors24, common, gcd_result)
        example_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        example_group.next_to(method_group, DOWN, buff=0.7)
        
        self.play(Write(example_title))
        self.wait(0.5)
        self.play(Write(divisors18))
        self.wait(0.5)
        self.play(Write(divisors24))
        self.wait(0.5)
        self.play(Write(common))
        self.wait(1)
        self.play(Write(gcd_result))
        self.wait(3)
        
        # Conclusion
        conclusion = Text(
            "The GCD helps us find the largest\n"
            "possible equal division of two quantities",
            font="Times New Roman",
            color=BLACK,
            weight=BOLD,
            font_size=36,
            line_spacing=1.2
        )
        
        applications = Text(
            "Useful in fraction simplification,\n"
            "pattern design, and resource allocation",
            font="Times New Roman",
            color=GREEN_D,
            font_size=32,
            line_spacing=1.2
        )
        
        self.play(FadeOut(method_group), FadeOut(example_group))
        self.play(Write(conclusion))
        self.wait(2)
        self.play(Write(applications.next_to(conclusion, DOWN, buff=0.7)))
        self.wait(3)