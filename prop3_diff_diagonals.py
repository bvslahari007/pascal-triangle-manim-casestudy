from manim import *
import math

class PowersOf11Pascal(Scene):
    def construct(self):
        # Title with proper spacing
        title = Tex("Pascal's Triangle and Powers of 11", font_size=52)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title))
        self.wait(2)

        # Configuration variables
        ROW_SPACING = 1.0
        DIGIT_SPACING = 0.7
        POWER_LABEL_OFFSET = 2.5
        ANIMATION_SPEED = 0.7
        WAIT_TIME = 1.5  # Increased wait time for better visibility

        # Create all elements but don't show them yet
        triangle = VGroup()
        row_numbers = VGroup()
        power_labels = VGroup()
        arrows = VGroup()

        for n in range(7):
            # Create row of digits
            row = VGroup()
            for k in range(n + 1):
                coeff = str(math.comb(n, k))
                digit = Tex(coeff, font_size=36)
                row.add(digit)
            
            row.arrange(RIGHT, buff=DIGIT_SPACING)
            row.shift(DOWN * n * ROW_SPACING)
            triangle.add(row)

            # Row number label
            row_num = Tex(f"Row {n}:", font_size=36)
            row_num.next_to(row, LEFT, buff=0.5)
            row_numbers.add(row_num)

            # Power label
            power = 11 ** n
            power_label = Tex(f"$11^{n} = {power}$", font_size=36)
            power_label.next_to(row, RIGHT, buff=POWER_LABEL_OFFSET)
            power_labels.add(power_label)

            # Arrow
            arrow = Arrow(
                row.get_right() + RIGHT*0.1,
                power_label.get_left() + LEFT*0.1,
                buff=0,
                stroke_width=4,
                color=YELLOW
            )
            arrows.add(arrow)

        # Center everything
        main_group = VGroup(row_numbers, triangle, arrows, power_labels)
        main_group.center().next_to(title, DOWN, buff=1.0)

        # Create an explanation area at the center of the screen
        explanation_area = Rectangle(
            width=10, 
            height=3, 
            stroke_opacity=0,
            fill_opacity=0
        )
        explanation_area.move_to(ORIGIN)  # Place it at the center of the screen

        # ANIMATE ROWS ONE BY ONE
        for n in range(7):
            # Animate current row appearing
            self.play(
                Write(row_numbers[n]),
                Write(triangle[n]),
                run_time=ANIMATION_SPEED
            )
            
            # Animate power label and arrow
            self.play(
                Write(power_labels[n]),
                GrowArrow(arrows[n]),
                run_time=ANIMATION_SPEED
            )
            
            # Add explanation for first 4 rows with improved visibility at row 4
            if n == 4:
                # Save the original state
                main_group_copy = main_group.copy()
                
                # Dim the triangle for better explanation visibility
                self.play(main_group.animate.set_opacity(0.3))
                
                # Create a highly visible explanation that overlays the dimmed triangle
                explanation = Tex(
                    "Perfect match up to row 4!",
                    font_size=48,  # Larger font
                    color=GREEN
                )
                
                # Add a background rectangle for better visibility
                bg_rect = SurroundingRectangle(
                    explanation, 
                    color=GREEN, 
                    fill_opacity=0.2,
                    buff=0.5,
                    corner_radius=0.3
                )
                explanation_group = VGroup(bg_rect, explanation)
                explanation_group.move_to(explanation_area)  # Center of screen
                
                self.play(Write(explanation_group))
                self.wait(WAIT_TIME * 2)  # Extra wait time
                
                # Fade out explanation and restore triangle
                self.play(
                    FadeOut(explanation_group),
                    main_group.animate.set_opacity(1.0)  # Restore full opacity
                )
            
            self.wait(WAIT_TIME)

        # After all rows appear
        self.play(FadeOut(title))
        self.play(main_group.animate.to_edge(UP, buff=0.75))
        self.wait(WAIT_TIME)

        # Problem at row 5 explanation with improved visibility
        # Dim the triangle again
        self.play(main_group.animate.set_opacity(0.3))
        
        problem_text = Tex(
            "But at row 5, we have digits $\\geq$ 10...",
            font_size=48,  # Larger font
            color=RED
        )
        
        # Add a background for better visibility
        problem_bg = SurroundingRectangle(
            problem_text, 
            color=RED, 
            fill_opacity=0.2,
            buff=0.5,
            corner_radius=0.3
        )
        problem_group = VGroup(problem_bg, problem_text)
        problem_group.move_to(explanation_area)  # Center of screen
        
        self.play(Write(problem_group))
        self.wait(WAIT_TIME * 2)  # Extra wait time
        
        # Restore triangle opacity and fade out problem text
        self.play(
            FadeOut(problem_group),
            main_group.animate.set_opacity(1.0)
        )
        self.wait(WAIT_TIME)

        # Focus on row 5
        row5 = triangle[5]
        row5_copy = row5.copy()
        row5_group = VGroup(row_numbers[5].copy(), row5_copy).scale(1.5)
        
        # Position the row5 demo in the upper part of the screen
        row5_demo_area = Rectangle(width=12, height=4, fill_opacity=0, stroke_opacity=0)
        row5_demo_area.to_edge(UP, buff=1.0)
        row5_group.move_to(row5_demo_area)
        
        self.play(
            FadeOut(main_group),
            FadeIn(row5_group)
        )
        self.wait(WAIT_TIME)

        # Highlight digits
        digits = [1, 5, 10, 10, 5, 1]
        digit_boxes = VGroup()
        for i, d in enumerate(digits):
            box = SurroundingRectangle(
                row5_copy[i], 
                color=BLUE, 
                buff=0.3,
                corner_radius=0.1
            )
            digit_boxes.add(box)
            self.play(Create(box), run_time=0.3)
        self.wait(WAIT_TIME)

        # Reposition explanation area for the remaining demo
        explanation_area.next_to(row5_group, DOWN, buff=1.0)
        
        # Carry explanation with improved visibility
        carry_explanation = VGroup(
            Tex("We need to carry over", font_size=42),
            Tex("when digits $\\geq$ 10", font_size=42)
        ).arrange(DOWN, buff=0.3)
        
        # Add a background for the explanation
        carry_bg = SurroundingRectangle(
            carry_explanation, 
            color=BLUE, 
            fill_opacity=0.15,
            buff=0.4,
            corner_radius=0.2
        )
        carry_group = VGroup(carry_bg, carry_explanation)
        carry_group.move_to(explanation_area)
        
        self.play(Write(carry_group))
        self.wait(WAIT_TIME * 2)

        # Show place values
        places = ["100000", "10000", "1000", "100", "10", "1"]
        place_values = VGroup()
        for i, place in enumerate(places):
            p = Tex(place, font_size=32).next_to(row5_copy[i], UP, buff=0.7)
            place_values.add(p)
        self.play(Write(place_values))
        self.wait(WAIT_TIME)
        
        # Fade out carry explanation before showing multiplication
        self.play(FadeOut(carry_group))

        # Multiplication process with improved visibility
        multiplication = VGroup(
            Tex("$1\\times100000 + 5\\times10000 + 10\\times1000$", font_size=38),
            Tex("$+ 10\\times100 + 5\\times10 + 1\\times1 = 161051$", font_size=38)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Add background for multiplication steps
        mult_bg = SurroundingRectangle(
            multiplication, 
            color=YELLOW, 
            fill_opacity=0.15,
            buff=0.4,
            corner_radius=0.2
        )
        mult_group = VGroup(mult_bg, multiplication)
        mult_group.move_to(explanation_area)
        
        self.play(Write(mult_group))
        self.wait(WAIT_TIME * 3)
        
        # Fade out multiplication before showing result
        self.play(FadeOut(mult_group))

        # Final result with improved visibility
        result = Tex("$11^5 = 161051$", font_size=52, color=YELLOW)
        
        # Add a highlighting box around the result
        result_bg = SurroundingRectangle(
            result, 
            color=YELLOW, 
            fill_opacity=0.2,
            buff=0.5,
            corner_radius=0.3
        )
        result_group = VGroup(result_bg, result)
        result_group.move_to(explanation_area)
        
        self.play(Write(result_group))
        self.wait(WAIT_TIME * 3)

        # Return to full triangle
        self.play(
            FadeOut(row5_group),
            FadeOut(result_group),
            FadeOut(place_values),
            FadeOut(digit_boxes),
            FadeIn(main_group)
        )
        
        # Reposition explanation area for remaining content
        explanation_area.move_to(ORIGIN)  # Center of screen
        self.wait(WAIT_TIME)

        # Highlight row 6
        row6 = triangle[6]
        row6_original_color = WHITE  # Store original color
        power_label6_original_color = WHITE
        arrow6_original_color = YELLOW
        
        self.play(
            row6.animate.set_color(YELLOW),
            power_labels[6].animate.set_color(YELLOW),
            arrows[6].animate.set_color(YELLOW)
        )
        self.wait(WAIT_TIME * 2)
        
        # Now return Row 6 back to its original color
        self.play(
            row6.animate.set_color(row6_original_color),
            power_labels[6].animate.set_color(power_label6_original_color),
            arrows[6].animate.set_color(arrow6_original_color)
        )
        
        # Clear everything for the final explanations
        self.play(FadeOut(main_group))
        self.wait(WAIT_TIME)

        # Set up center stage for final explanations
        center_stage = Rectangle(
            width=12, 
            height=6, 
            stroke_opacity=0,
            fill_opacity=0
        )
        center_stage.move_to(ORIGIN)
        
        # Row 6 explanation with improved visibility - standalone
        row6_expl = VGroup(
            Tex("Row 6: $1\\ 6\\ 15\\ 20\\ 15\\ 6\\ 1$", font_size=48),
            Tex("After carrying: $1,771,561 = 11^6$", font_size=48)
        ).arrange(DOWN, buff=0.5)
        
        # Add background for row 6 explanation
        row6_bg = SurroundingRectangle(
            row6_expl, 
            color=YELLOW, 
            fill_opacity=0.15,
            buff=0.5,
            corner_radius=0.3
        )
        row6_expl_group = VGroup(row6_bg, row6_expl)
        row6_expl_group.move_to(center_stage)
        
        self.play(Write(row6_expl_group))
        self.wait(WAIT_TIME * 3)
        
        # Fade out row 6 explanation before showing conclusion
        self.play(FadeOut(row6_expl_group))
        self.wait(WAIT_TIME)

        # Final conclusion with improved visibility - standalone and larger
        conclusion = VGroup(
            Tex("Pascal's Triangle rows correspond to", font_size=48),
            Tex("powers of 11 when we handle carries", font_size=48),
            Tex("properly!", font_size=58, color=GREEN)
        ).arrange(DOWN, buff=0.5)
        
        # Add background for conclusion
        conclusion_bg = SurroundingRectangle(
            conclusion, 
            color=GREEN, 
            fill_opacity=0.2,
            buff=0.6,
            corner_radius=0.3
        )
        conclusion_group = VGroup(conclusion_bg, conclusion)
        conclusion_group.move_to(center_stage)
        
        self.play(Write(conclusion_group))
        self.wait(WAIT_TIME * 4)

        # Fade out everything
        self.play(FadeOut(conclusion_group))