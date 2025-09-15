from manim import *
from math import comb

class InspiringPascalFinal(Scene):
    def construct(self):
        # Setup
        self.camera.background_color = BLACK
        
        # 1. Create Pascal's Triangle
        rows = 7
        triangle = VGroup()
        for n in range(rows):
            row = VGroup()
            for k in range(n+1):
                num = MathTex(str(comb(n, k)), color=WHITE, font_size=36)
                row.add(num)
            row.arrange(RIGHT, buff=0.6)
            triangle.add(row)
        triangle.arrange(DOWN, buff=0.4, aligned_edge=ORIGIN).center()
        
        # 2. Show Triangle
        self.play(DrawBorderThenFill(triangle), run_time=2)
        self.wait(2)
        
        # 3. Fade to background
        self.play(triangle.animate.set_opacity(0.3), run_time=1.5)
        
        # 4. Main Text Reveal
        main_lines = [
            "If something as simple as this triangle",
            "can reveal so much...",
            "imagine what else is hiding",
            "in the world around us.",
            "All it takes is a closer look."
        ]
        main_text = VGroup(*[Text(line, font="Times New Roman", weight=BOLD, font_size=36) for line in main_lines])
        main_text.arrange(DOWN, center=True, buff=0.4).center()
        
        for line in main_text:
            self.play(Write(line), run_time=1)
            self.wait(0.2)
        
        # 5. Highlight final line
        self.play(main_text[-1].animate.set_color("#FFD700"), run_time=1.5)
        self.wait(2)
        
        # 6. Fade out everything
        self.play(FadeOut(triangle), FadeOut(main_text), run_time=2)
        
        # 7. Final inspirational message (with proper highlighting)
        closing_lines = [
            "Thank you...",
            "and keep looking closer.",
            "You never know what you'll find."
        ]
        closing_text = VGroup()
        for line in closing_lines:
            text = Text(line, font="Times New Roman", weight=BOLD, font_size=36)
            closing_text.add(text)
        closing_text.arrange(DOWN, center=True, buff=0.6).center()
        
        # Animate line by line
        for line in closing_text:
            self.play(Write(line), run_time=1.5)
            self.wait(0.3)
        
        # PROPERLY highlight "keep looking closer" as one phrase
        second_line = closing_text[1]
        start_idx = second_line.text.find("keep")
        end_idx = second_line.text.find(".")  # Until the period
        highlight_phrase = second_line.chars[start_idx:end_idx]
        
        self.play(
            highlight_phrase.animate.set_color("#FFD700"),
            Flash(
                highlight_phrase,
                color="#FFD700",
                flash_radius=0.35,
                line_length=0.6,
                run_time=2
            )
        )
        
        # Final hold
        self.wait(5)