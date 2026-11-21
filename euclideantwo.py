from manim import *

config.background_color = "#FFFFF0"

class EuclidPaperDivision(Scene):
    def construct(self):
        Text.set_default(font="Times New Roman")
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{mathptmx}")
        MathTex.set_default(tex_template=tex_template)
        
        colors = {
            "dividend": "#1E90FF",
            "divisor": "#FF8C00",
            "quotient": "#2E8B57",
            "remainder": "#DC143C",
            "highlight": "#9400D3",
            "explanation": "#333333"
        }
        
        steps = [
            (78, 66),
            (66, 12),
            (12, 6),
            (6, 0)
        ]
        
        current_y = 3.0
        all_divisions = VGroup()
        previous_step_elements = []

        # Title
        title = Text("Finding GCD using Euclid's Division Algorithm", font_size=36, color=BLACK)
        subtitle = Text("Let's take the example of GCD(78, 66)", font_size=30, color=BLACK)
        title_group = VGroup(title, subtitle).arrange(DOWN)
        self.play(Write(title_group))
        self.wait(1.2)
        self.play(title_group.animate.to_edge(UP))
        self.wait(0.3)

        # Fade out title before starting first division
        self.play(FadeOut(title_group))
        self.wait(0.3)

        for i, (dividend, divisor) in enumerate(steps):
            if divisor == 0:
                break
            
            # Fade previous step elements before starting the next one
            if previous_step_elements:
                fade_group = VGroup(*previous_step_elements)
                self.play(fade_group.animate.set_opacity(0.3))
                self.wait(0.2)

            # Reset the list for the current step
            current_step_elements = []

            division_group = self.create_division_setup(dividend, divisor, colors, current_y)
            all_divisions.add(division_group)
            self.play(FadeIn(division_group))
            self.wait(0.4)
            current_step_elements.append(division_group)

            quotient = dividend // divisor
            remainder = dividend % divisor

            # Add quotient above the division bar
            quotient_text = Text(str(quotient), color=colors["quotient"], font_size=32)
            quotient_text.next_to(division_group[0], UP, buff=0.2)
            self.play(Write(quotient_text))
            current_step_elements.append(quotient_text)

            # Add product and subtraction line below dividend
            product = divisor * quotient
            product_text = Text(str(product), color=colors["divisor"], font_size=32)
            product_text.next_to(division_group[1], DOWN, aligned_edge=RIGHT, buff=0.2)
            sub_line = Line(LEFT, RIGHT, color=BLACK, stroke_width=2)
            sub_line.width = division_group[1].width * 0.7
            sub_line.next_to(product_text, DOWN, buff=0.1)
            self.play(Write(product_text), Create(sub_line))
            current_step_elements.extend([product_text, sub_line])

            # Add remainder below subtraction line
            remainder_text = Text(str(remainder), color=colors["remainder"], font_size=32)
            remainder_text.next_to(sub_line, DOWN, aligned_edge=RIGHT, buff=0.2)
            self.play(Write(remainder_text))
            current_step_elements.append(remainder_text)

            # Math formula (left side)
            equation = MathTex(
                f"{dividend} = ({divisor} \\times {quotient}) + {remainder}",
                font_size=34,
                color=BLACK
            )
            equation.to_edge(LEFT).shift(UP * (current_y - 0.4))
            self.play(Write(equation))
            self.wait(0.5)
            current_step_elements.append(equation)

            # Explanatory text (right side)
            if remainder != 0:
                explain_text = Text(
                    f"Now take {divisor} as new dividend\nand {remainder} as new divisor",
                    font_size=26, color=colors["explanation"]
                )
            else:
                explain_text = Text(
                    f"Ta-da! Remainder hits zero, GCD is {divisor}! 🌟",
                    font_size=26, color=colors["highlight"]
                )
            explain_text.to_edge(RIGHT).shift(UP * (current_y - 0.4))
            self.play(Write(explain_text))
            self.wait(1)
            current_step_elements.append(explain_text)

            # Highlight final GCD
            if remainder == 0:
                gcd_box = SurroundingRectangle(
                    division_group[2],
                    color=colors["highlight"],
                    buff=0.3, corner_radius=0.1, stroke_width=3
                )
                self.play(
                    Create(gcd_box),
                    Flash(division_group[2], flash_radius=0.5, color=colors["highlight"])
                )
                self.wait(2)
                break

            # Store current step elements for fading in the next iteration
            previous_step_elements = current_step_elements
            current_y -= 2.5

        self.wait(2)

    def create_division_setup(self, dividend, divisor, colors, y_position):
        dividend_text = Text(str(dividend), color=colors["dividend"], font_size=36)
        horizontal_line = Line(LEFT, RIGHT, color=BLACK).set_width(dividend_text.width + 0.2)
        vertical_line = Line(UP, DOWN, color=BLACK).set_height(0.8)
        bracket = VGroup(horizontal_line, vertical_line).arrange(DR, buff=0)
        bracket.next_to(dividend_text, LEFT, buff=0.3)
        divisor_text = Text(str(divisor), color=colors["divisor"], font_size=36)
        divisor_text.next_to(vertical_line, LEFT, buff=0.3)
        division_group = VGroup(
            horizontal_line,
            dividend_text,
            divisor_text,
            vertical_line
        ).move_to(UP * y_position)
        return division_group