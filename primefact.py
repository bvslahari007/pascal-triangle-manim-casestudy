from manim import *

class GCDPrimeFactorization(Scene):
    def construct(self):
        # Set paper-like background
        self.camera.background_color = "#FFF8E7"

        # === Title ===
        title = Text("Middle-School GCD Method",
                     font="Times New Roman", color=BLUE_D, weight=BOLD, font_size=48)
        subtitle = Text("(Prime Factorization Approach)",
                        font="Times New Roman", color=GRAY, font_size=28).next_to(title, DOWN, buff=0.3)
        self.play(Write(title), Write(subtitle))
        self.wait(1.5)

        # Quick intro
        intro = Text("Let's break it down step-by-step:",
                     font="Times New Roman", color=BLACK, font_size=32).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(intro))

        # === Step 1 ===
        step1 = Text("Step 1: Factorize first number",
                     font="Times New Roman", color=BLUE_D, weight=BOLD, font_size=36)
        factors1 = MathTex("60 = 2 \\times 2 \\times 3 \\times 5",
                           color=BLUE, font_size=42).next_to(step1, DOWN, buff=0.4)
        self.play(Write(step1))
        self.play(Write(factors1))
        self.wait(1.5)
        self.play(FadeOut(step1), FadeOut(factors1))

        # === Step 2 ===
        step2 = Text("Step 2: Factorize second number",
                     font="Times New Roman", color=GREEN_D, weight=BOLD, font_size=36)
        factors2 = MathTex("24 = 2 \\times 2 \\times 2 \\times 3",
                           color=GREEN, font_size=42).next_to(step2, DOWN, buff=0.4)
        self.play(Write(step2))
        self.play(Write(factors2))
        self.wait(1.5)
        self.play(FadeOut(step2), FadeOut(factors2))

        # === Step 3 ===
        step3 = Text("Step 3: Identify common factors",
                     font="Times New Roman", color=PURPLE_D, weight=BOLD, font_size=36)
        self.play(Write(step3))
        f1 = MathTex("2", "\\times", "2", "\\times", "3", "\\times", "5", font_size=44, color=BLACK).move_to(LEFT * 3 + DOWN)
        f2 = MathTex("2", "\\times", "2", "\\times", "2", "\\times", "3", font_size=44, color=BLACK).move_to(RIGHT * 3 + DOWN)
        self.play(Write(f1), Write(f2))
        self.wait(0.5)

        # Matching indices
        matching_indices_f1 = [0, 2, 4]
        matching_indices_f2 = [0, 2, 6]
        boxes_f1 = [SurroundingRectangle(f1[i], color=YELLOW) for i in matching_indices_f1]
        boxes_f2 = [SurroundingRectangle(f2[i], color=YELLOW) for i in matching_indices_f2]
        for b1, b2 in zip(boxes_f1, boxes_f2):
            self.play(Create(b1), Create(b2))
            self.wait(0.3)

        common = MathTex("2 \\times 2 \\times 3", color=YELLOW, font_size=48).next_to(step3, DOWN, buff=2)
        self.play(Write(common))
        self.wait(1.5)
        self.play(FadeOut(step3), FadeOut(f1), FadeOut(f2), *[FadeOut(b) for b in boxes_f1 + boxes_f2], FadeOut(common))

        # === Step 4 ===
        step4 = Text("Step 4: Calculate GCD",
                     font="Times New Roman", color=RED_D, weight=BOLD, font_size=36)
        gcd_result = MathTex(
            "\\text{GCD}(60, 24) = 2 \\times 2 \\times 3 = 12",
            color=RED, font_size=46
        ).next_to(step4, DOWN, buff=0.4)
        gcd_result[0][12:15].set_color(BLACK)  # 2×2×3
        gcd_result[0][-2:].set_color(GOLD)      # 12
        self.play(Write(step4))
        self.play(Write(gcd_result))
        final_box = SurroundingRectangle(gcd_result, color=GOLD, buff=0.3)
        self.play(Create(final_box))
        self.wait(2.5)
        self.play(FadeOut(step4), FadeOut(gcd_result), FadeOut(final_box))

        # === Summary ===
        summary = Text("Key Takeaways:",
                       font="Times New Roman", color=BLUE_D, weight=BOLD, font_size=42).to_edge(UP, buff=1.0)
        bullets = BulletedList(
            "Find prime factors of both numbers",
            "Identify COMMON factors (minimum counts)",
            "Multiply them for the GCD",
            buff=0.5
        ).next_to(summary, DOWN, buff=0.8)

        for item in bullets:
            item.set(font="Times New Roman", font_size=36, color=BLACK)
        bullets[1].set_color(YELLOW)

        self.play(Write(summary))
        self.wait(0.5)
        self.play(Write(bullets))
        self.wait(4)
