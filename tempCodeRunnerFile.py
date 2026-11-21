from manim import *

class EuclidPaperDivision(Scene):
    def construct(self):
        config.background_color = "#FFFFF0"  # Cream background

        colors = {
            "dividend": "#1E90FF",  # DodgerBlue
            "divisor": "#FF8C00",   # DarkOrange
            "quotient": "#2E8B57",  # SeaGreen
            "remainder": "#DC143C", # Crimson
            "highlight": "#9400D3", # DarkViolet
            "explanation": "#696969" # DimGray
        }

        steps = [
            (28, 18),
            (18, 10),
            (10, 8),
            (8, 2),
            (2, 0)
        ]

        current_y = 3.0  # Starting Y position

        # Title
        title = Text("Finding GCD using Euclid's Division Algorithm", font_size=36, color=BLACK)
        subtitle = Text("GCD(28, 18)", font_size=32, color=BLACK)
        title_group = VGroup(title, subtitle).arrange(DOWN)
        self.play(Write(title_group))
        self.wait(1.5)
        self.play(FadeOut(title_group))
        self.wait(0.5)

        # Main Algorithm
        for i, (dividend, divisor) in enumerate(steps):
            if divisor == 0:
                break

            division_group = self.create_division_setup(dividend, divisor, colors, current_y)
            self.play(FadeIn(division_group))
            self.wait(0.3)

            quotient = dividend // divisor
            remainder = dividend % divisor

            # Show quotient
            quotient_text = Text(str(quotient), color=colors["quotient"], font_size=32)
            quotient_text.next_to(division_group[0], UP, buff=0.2)
            self.play(Write(quotient_text))

            # Explanation on left
            explain1 = Text("Find quotient and remainder", font_size=24, color=colors["explanation"])
            explain1.to_edge(LEFT).shift(DOWN * 0.5)
            self.play(Write(explain1))
            self.wait(0.3)

            # Multiplication product
            product = divisor * quotient
            product_text = Text(str(product), color=colors["divisor"], font_size=32)
            product_text.next_to(division_group[1], DOWN, aligned_edge=RIGHT, buff=0.2)

            sub_line = Line(LEFT, RIGHT, color=BLACK, stroke_width=2)
            sub_line.width = division_group[1].width * 0.7
            sub_line.next_to(product_text, DOWN, buff=0.1)

            self.play(Write(product_text), Create(sub_line))
            self.wait(0.2)

            # Remainder
            remainder_text = Text(str(remainder), color=colors["remainder"], font_size=32)
            remainder_text.next_to(sub_line, DOWN, aligned_edge=RIGHT, buff=0.2)
            self.play(Write(remainder_text))

            # Equation on right
            equation = MathTex(f"{dividend} = ({divisor} \\times {quotient}) + {remainder}", font_size=30)
            equation.to_edge(RIGHT).shift(UP * current_y * 0.2)
            self.play(Write(equation))
            self.wait(0.3)

            if remainder != 0:
                explain2 = Text("New divisor = old remainder", font_size=24, color=colors["explanation"])
                explain2.next_to(explain1, DOWN, aligned_edge=LEFT)
                arrow = Arrow(remainder_text.get_bottom(), division_group[1].get_top() + DOWN*3.5,
                              color=colors["remainder"], buff=0.1, stroke_width=2)
                self.play(Write(explain2), GrowArrow(arrow))
                self.wait(0.8)

                # Clean up for next step
                self.play(FadeOut(explain1), FadeOut(explain2), FadeOut(arrow), FadeOut(equation))
            else:
                explain_final = Text("Remainder = 0, so we stop!",
                                     font_size=26, color=colors["highlight"])
                explain_final.next_to(equation, DOWN, buff=0.7)
                gcd_box = SurroundingRectangle(
                    division_group[2].copy(),
                    color=colors["highlight"],
                    buff=0.3,
                    corner_radius=0.1,
                    stroke_width=3
                )
                gcd_text = Text("GCD = ", font_size=32, color=BLACK).next_to(gcd_box, LEFT)
                self.play(Write(explain_final), Create(gcd_box),
                          Write(gcd_text), Flash(division_group[2], color=colors["highlight"], flash_radius=1.5))
                self.wait(2)
                break

            self.play(FadeOut(explain1), FadeOut(equation))
            current_y -= 1.8

        self.wait(2)

    def create_division_setup(self, dividend, divisor, colors, y_position):
        dividend_text = Text(str(dividend), color=colors["dividend"], font_size=36)

        horizontal_line = Line(LEFT, RIGHT, color=BLACK)
        horizontal_line.width = 1.2
        vertical_line = Line(UP, DOWN, color=BLACK)
        vertical_line.height = 0.8

        bracket = VGroup(horizontal_line, vertical_line)
        bracket.arrange(DR, buff=0)
        bracket.next_to(dividend_text, LEFT, buff=0.3)

        divisor_text = Text(str(divisor), color=colors["divisor"], font_size=36)
        divisor_text.next_to(vertical_line, LEFT, buff=0.3)

        division_group = VGroup(horizontal_line, dividend_text, divisor_text, vertical_line)
        division_group.move_to(UP * y_position)

        return division_group
