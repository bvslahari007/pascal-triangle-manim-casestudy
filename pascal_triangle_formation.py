from manim import *
import math

class PascalTriangleWithElegantEnd(Scene):
    def construct(self):
        # Configure scene with dark background
        self.camera.background_color = "#000000"
        
        # Title animation
        title = Tex("Let's see how it's built", font_size=42, color=BLUE_C)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP, buff=0.5))
        self.wait(0.3)

        # Build triangle structure (5 rows)
        rows = 5
        triangle = VGroup()
        number_map = {}
        
        for n in range(rows):
            row = VGroup()
            for k in range(n+1):
                num = Integer(0, color=WHITE).set_opacity(0)
                row.add(num)
                number_map[(n,k)] = num
            row.arrange(RIGHT, buff=0.7)
            triangle.add(row)
        
        triangle.arrange(DOWN, buff=0.5)
        triangle.center().shift(UP*0.3)
        
        # Animate base structure
        self.play(FadeIn(triangle))
        self.wait(0.2)

        # Animation sequence
        for n in range(rows):
            for k in range(n+1):
                current_num = number_map[(n,k)]
                
                if n == 0:  # Top 1
                    self.reveal_number(current_num, 1, PURPLE_A)
                elif k == 0 or k == n:  # Edge 1's
                    self.reveal_number(current_num, 1, PURPLE_A)
                else:
                    left_parent = number_map[(n-1,k-1)]
                    right_parent = number_map[(n-1,k)]
                    sum_value = left_parent.get_value() + right_parent.get_value()
                    
                    # Create addition equation
                    equation = MathTex(
                        f"{left_parent.get_value()} + {right_parent.get_value()}",
                        color=YELLOW
                    ).move_to(current_num)
                    
                    # Create pointing arrows
                    left_arrow = Arrow(
                        left_parent.get_bottom(),
                        equation.get_top() + LEFT*0.2,
                        color=GOLD_A,
                        buff=0.1,
                        stroke_width=4
                    )
                    right_arrow = Arrow(
                        right_parent.get_bottom(),
                        equation.get_top() + RIGHT*0.2,
                        color=GOLD_A,
                        buff=0.1,
                        stroke_width=4
                    )
                    
                    # Animate addition process
                    self.play(
                        GrowArrow(left_arrow),
                        GrowArrow(right_arrow),
                        left_parent.animate.set_color(GOLD_A),
                        right_parent.animate.set_color(GOLD_A),
                        run_time=0.5
                    )
                    self.wait(0.2)
                    self.play(FadeIn(equation))
                    self.wait(0.3)
                    
                    # Transform to result
                    result = Integer(sum_value, color=GREEN_B).move_to(current_num)
                    self.play(
                        Transform(equation, result),
                        run_time=0.8
                    )
                    self.play(
                        current_num.animate.set_value(sum_value).set_color(GREEN_B).set_opacity(1),
                        run_time=0.3
                    )
                    
                    # Clean up
                    self.play(
                        FadeOut(left_arrow),
                        FadeOut(right_arrow),
                        left_parent.animate.set_color(WHITE),
                        right_parent.animate.set_color(WHITE),
                        run_time=0.3
                    )
                    self.remove(equation)
        
        # Your requested ending text
        final_text = Tex(
            r"And so it grows...",  
            r"endlessly",  
            font_size=36,
            color=GREEN_B,
            tex_environment="center"
        ).next_to(triangle, DOWN, buff=0.7)
        
        # Animate text with fade-in effect
        self.play(
            FadeIn(final_text, shift=UP*0.3),
            run_time=1.5
        )
        self.wait(3)  # Hold final frame
    
    def reveal_number(self, mobject, value, color):
        """Helper to animate number appearance"""
        mobject.set_value(value)
        self.play(
            mobject.animate.set_opacity(1).set_color(color),
            run_time=0.4
        )
        self.wait(0.1)