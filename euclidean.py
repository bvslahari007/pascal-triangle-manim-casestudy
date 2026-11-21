from manim import *

class EuclidPaperDivision(Scene):
    def construct(self):
        # Configure colors and font
        config.background_color = "#FFFFF0"  # Cream background
        Text.set_default(font="Times New Roman")
        MathTex.set_default(font="Times New Roman")
        
        colors = {
            "dividend": "#1E90FF",  # DodgerBlue
            "divisor": "#FF8C00",    # DarkOrange
            "quotient": "#2E8B57",   # SeaGreen
            "remainder": "#DC143C",   # Crimson
            "highlight": "#9400D3",   # DarkViolet
            "explanation": "#696969"  # DimGray
        }
        
        # Initialize variables
        steps = [
            (28, 18),  # dividend, divisor
            (18, 10),
            (10, 8),
            (8, 2),
            (2, 0)
        ]
        all_divisions = VGroup()
        current_y = 3.0  # Starting Y position
        
        # Title
        title = Text("Finding GCD using Euclid's Division Algorithm", font_size=36, color=BLACK)
        subtitle = Text("GCD(28, 18)", font_size=32, color=BLACK)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
        self.play(Write(title_group))
        self.wait()
        self.play(title_group.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)
        
        # Main algorithm
        for i, (dividend, divisor) in enumerate(steps):
            if divisor == 0:
                break
                
            # Create division setup
            division_group = self.create_division_setup(dividend, divisor, colors, current_y)
            all_divisions.add(division_group)
            self.play(FadeIn(division_group, shift=UP*0.5))
            self.wait(0.5)
            
            # Calculate values
            quotient = dividend // divisor
            remainder = dividend % divisor
            
            # Show quotient
            quotient_text = Text(str(quotient), color=colors["quotient"], font_size=32)
            quotient_text.next_to(division_group[0], UP, buff=0.2, aligned_edge=RIGHT)
            self.play(Write(quotient_text))
            
            # Explanation text
            explain1 = Text("Division Step:", 
                           font_size=24, color=colors["explanation"])
            explain2 = Text(f"{dividend} ÷ {divisor}", 
                           font_size=28, color=BLACK)
            explain_group = VGroup(explain1, explain2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            explain_group.next_to(division_group, RIGHT, buff=1.2)
            self.play(Write(explain_group))
            self.wait(0.5)
            
            # Show multiplication
            product = divisor * quotient
            product_text = Text(str(product), color=colors["divisor"], font_size=32)
            product_text.next_to(division_group[1], DOWN, buff=0.2, aligned_edge=RIGHT)
            
            # Subtraction line
            sub_line = Line(LEFT, RIGHT, color=BLACK, stroke_width=2)
            sub_line.width = division_group[1].width * 0.7
            sub_line.next_to(product_text, DOWN, buff=0.1)
            
            self.play(
                Write(product_text),
                Create(sub_line)
            )
            self.wait(0.3)
            
            # Show remainder
            remainder_text = Text(str(remainder), color=colors["remainder"], font_size=32)
            remainder_text.next_to(sub_line, DOWN, buff=0.2, aligned_edge=RIGHT)
            self.play(Write(remainder_text))
            
            # Show equation
            equation = MathTex(
                f"{dividend} = {divisor} \\times {quotient} + {remainder}",
                font_size=30,
                color=BLACK
            )
            equation.next_to(division_group, DOWN, buff=0.7)
            self.play(Write(equation))
            
            # Transition explanation
            if remainder != 0:
                explain3 = Text("Now use:", 
                              font_size=24, color=colors["explanation"])
                explain4 = Text(f"Divisor ({divisor}) as new dividend", 
                              font_size=24, color=colors["dividend"])
                explain5 = Text(f"Remainder ({remainder}) as new divisor", 
                              font_size=24, color=colors["divisor"])
                transition_group = VGroup(explain3, explain4, explain5).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
                transition_group.next_to(explain_group, DOWN, buff=0.5, aligned_edge=LEFT)
                
                arrow = Arrow(
                    remainder_text.get_bottom(),
                    division_group[1].get_top() + DOWN*3.5,
                    color=colors["remainder"],
                    buff=0.1,
                    stroke_width=2,
                    tip_length=0.2
                )
                self.play(
                    Write(transition_group),
                    GrowArrow(arrow)
                )
                self.wait(1.5)
                
                # Clean up for next step
                self.play(
                    FadeOut(explain_group),
                    FadeOut(transition_group),
                    FadeOut(arrow)
                )
            else:
                # Final GCD found
                explain_final = Text("Process Complete!", 
                                   font_size=26, color=colors["highlight"])
                explain_reason = Text("Remainder is 0", 
                                     font_size=24, color=colors["explanation"])
                final_group = VGroup(explain_final, explain_reason).arrange(DOWN, buff=0.2)
                final_group.next_to(equation, DOWN, buff=0.7)
                
                gcd_box = SurroundingRectangle(
                    division_group[2].copy(),
                    color=colors["highlight"],
                    buff=0.3,
                    corner_radius=0.1,
                    stroke_width=3
                )
                gcd_text = Text("GCD = ", font_size=32, color=BLACK)
                gcd_value = division_group[2].copy()
                gcd_group = VGroup(gcd_text, gcd_value).arrange(RIGHT, buff=0.3)
                gcd_group.next_to(gcd_box, LEFT, buff=0.3)
                
                self.play(
                    Write(final_group),
                    Create(gcd_box),
                    Write(gcd_group),
                    Flash(division_group[2], color=colors["highlight"], flash_radius=1.5)
                )
                self.wait(3)
                break
            
            # Prepare for next division (lower position)
            current_y -= 1.8
            
        # Final wait
        self.wait(3)
    
    def create_division_setup(self, dividend, divisor, colors, y_position):
        """Creates the traditional long division bracket setup with proper alignment"""
        # Create elements
        dividend_text = Text(str(dividend), color=colors["dividend"], font_size=36)
        divisor_text = Text(str(divisor), color=colors["divisor"], font_size=36)
        
        # Create bracket (L-shape)
        bracket_width = max(dividend_text.width, divisor_text.width) * 1.2
        horizontal_line = Line(LEFT, RIGHT, color=BLACK, stroke_width=2)
        horizontal_line.width = bracket_width
        vertical_line = Line(UP, DOWN, color=BLACK, stroke_width=2)
        vertical_line.height = 0.8
        
        # Position elements
        bracket = VGroup(horizontal_line, vertical_line)
        bracket.arrange(DR, buff=0)
        bracket.next_to(dividend_text, LEFT, buff=0.3)
        
        # Align divisor with vertical line
        divisor_text.next_to(vertical_line, LEFT, buff=0.3)
        divisor_text.align_to(horizontal_line, UP)
        
        # Group all elements
        division_group = VGroup(
            horizontal_line,
            vertical_line,
            dividend_text,
            divisor_text
        )
        
        # Position the entire group
        division_group.move_to(UP * y_position)
        
        return division_group