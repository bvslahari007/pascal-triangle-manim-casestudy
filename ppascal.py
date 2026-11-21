from manim import *

class PascalsTriangleVisualization(Scene):
    def construct(self):
        # Title at the center
        title = Text("Pascal's Triangle", font_size=60).move_to(UP * 3)
        self.play(FadeIn(title, scale=0.8))
        self.wait(2)
        self.play(FadeOut(title))

        # First number "1" at the top
        top_1 = Text("1", font_size=48).move_to(UP * 2)
        faded_zeros = VGroup(
            Text("0", font_size=36, color=GRAY).move_to(UP * 2 + LEFT * 1.5),
            Text("0", font_size=36, color=GRAY).move_to(UP * 2 + RIGHT * 1.5)
        )

        self.play(FadeIn(top_1))
        self.play(FadeIn(faded_zeros, run_time=1))
        self.wait(1)

        # Second row numbers
        row_2 = VGroup(
            Text("1", font_size=48).move_to(UP * 1 + LEFT * 1),
            Text("1", font_size=48).move_to(UP * 1 + RIGHT * 1)
        )

        self.play(FadeIn(row_2))

        # Create arrows after row_2 appears
        arrow_1 = Arrow(start=top_1.get_bottom(), end=row_2[0].get_top(), buff=0.1)
        arrow_2 = Arrow(start=top_1.get_bottom(), end=row_2[1].get_top(), buff=0.1)
        self.play(GrowArrow(arrow_1), GrowArrow(arrow_2))
        self.wait(1)

        # Third row numbers
        row_3 = VGroup(
            Text("1", font_size=48).move_to(DOWN * 0 + LEFT * 2),
            Text("2", font_size=48).move_to(DOWN * 0),
            Text("1", font_size=48).move_to(DOWN * 0 + RIGHT * 2)
        )
        self.play(FadeIn(row_3))

        # Ensure arrows connect valid points
        arrows_3 = VGroup(
            Arrow(start=row_2[0].get_bottom(), end=row_3[0].get_top(), buff=0.1),
            Arrow(start=row_2[0].get_bottom(), end=row_3[1].get_top(), buff=0.1),
            Arrow(start=row_2[1].get_bottom(), end=row_3[1].get_top(), buff=0.1),
            Arrow(start=row_2[1].get_bottom(), end=row_3[2].get_top(), buff=0.1)
        )
        self.play(GrowArrow(arrows_3))
        self.wait(1)

        # Fourth row numbers
        row_4 = VGroup(
            Text("1", font_size=48).move_to(DOWN * 1 + LEFT * 3),
            Text("3", font_size=48).move_to(DOWN * 1 + LEFT * 1),
            Text("3", font_size=48).move_to(DOWN * 1 + RIGHT * 1),
            Text("1", font_size=48).move_to(DOWN * 1 + RIGHT * 3)
        )
        self.play(FadeIn(row_4))

        # Arrows for fourth row
        arrows_4 = VGroup(
            Arrow(start=row_3[0].get_bottom(), end=row_4[0].get_top(), buff=0.1),
            Arrow(start=row_3[0].get_bottom(), end=row_4[1].get_top(), buff=0.1),
            Arrow(start=row_3[1].get_bottom(), end=row_4[1].get_top(), buff=0.1),
            Arrow(start=row_3[1].get_bottom(), end=row_4[2].get_top(), buff=0.1),
            Arrow(start=row_3[2].get_bottom(), end=row_4[2].get_top(), buff=0.1),
            Arrow(start=row_3[2].get_bottom(), end=row_4[3].get_top(), buff=0.1)
        )

        self.play(GrowArrow(arrows_4))
        self.wait(2)

        # Fade out arrows to clean up
        self.play(FadeOut(arrows_4))
        self.wait(1)

        # Final messageafrom manim import *

class PascalsTriangleVisualization(Scene):
    def construct(self):
        # Title appears at the center and fades away
        title = Text("Pascal's Triangle", font_size=60).move_to(UP * 3)
        self.play(FadeIn(title, scale=0.8))
        self.wait(2)
        self.play(FadeOut(title))

        # Step 1: Add the first "1" at the top
        top_1 = Text("1", font_size=48).move_to(UP * 2)
        self.play(FadeIn(top_1))
        self.wait(1)

        # Step 2: Add faded zeros around the first "1"
        faded_zeros = VGroup(
            Text("0", font_size=36, color=GRAY).move_to(UP * 2 + LEFT * 1.5),
            Text("0", font_size=36, color=GRAY).move_to(UP * 2 + RIGHT * 1.5)
        )
        self.play(FadeIn(faded_zeros))
        self.wait(1)

        # Step 3: Add second row
        row_2 = VGroup(
            Text("1", font_size=48).move_to(UP * 1 + LEFT * 1),
            Text("1", font_size=48).move_to(UP * 1 + RIGHT * 1)
        )
        self.play(FadeIn(row_2))
        self.wait(1)

        # Step 4: Create arrows for second row **AFTER numbers exist**
        arrow_1 = Arrow(start=top_1.get_bottom(), end=row_2[0].get_top(), buff=0.1)
        arrow_2 = Arrow(start=top_1.get_bottom(), end=row_2[1].get_top(), buff=0.1)
        self.play(GrowArrow(arrow_1), GrowArrow(arrow_2))
        self.wait(1)

        # Step 5: Add third row
        row_3 = VGroup(
            Text("1", font_size=48).move_to(DOWN * 0 + LEFT * 2),
            Text("2", font_size=48).move_to(DOWN * 0),
            Text("1", font_size=48).move_to(DOWN * 0 + RIGHT * 2)
        )
        self.play(FadeIn(row_3))
        self.wait(1)

        # Step 6: Arrows for third row (after numbers appear)
        arrows_3 = VGroup(
            Arrow(start=row_2[0].get_bottom(), end=row_3[0].get_top(), buff=0.1),
            Arrow(start=row_2[0].get_bottom(), end=row_3[1].get_top(), buff=0.1),
            Arrow(start=row_2[1].get_bottom(), end=row_3[1].get_top(), buff=0.1),
            Arrow(start=row_2[1].get_bottom(), end=row_3[2].get_top(), buff=0.1)
        )
        self.play(GrowArrow(arrows_3))
        self.wait(1)

        # Step 7: Fourth row
        row_4 = VGroup(
            Text("1", font_size=48).move_to(DOWN * 1 + LEFT * 3),
            Text("3", font_size=48).move_to(DOWN * 1 + LEFT * 1),
            Text("3", font_size=48).move_to(DOWN * 1 + RIGHT * 1),
            Text("1", font_size=48).move_to(DOWN * 1 + RIGHT * 3)
        )
        self.play(FadeIn(row_4))
        self.wait(1)

        # Step 8: Arrows for fourth row (after numbers appear)
        arrows_4 = VGroup(
            Arrow(start=row_3[0].get_bottom(), end=row_4[0].get_top(), buff=0.1),
            Arrow(start=row_3[0].get_bottom(), end=row_4[1].get_top(), buff=0.1),
            Arrow(start=row_3[1].get_bottom(), end=row_4[1].get_top(), buff=0.1),
            Arrow(start=row_3[1].get_bottom(), end=row_4[2].get_top(), buff=0.1),
            Arrow(start=row_3[2].get_bottom(), end=row_4[2].get_top(), buff=0.1),
            Arrow(start=row_3[2].get_bottom(), end=row_4[3].get_top(), buff=0.1)
        )
        self.play(GrowArrow(arrows_4))
        self.wait(2)

        # Fade out arrows for a cleaner look
        self.play(FadeOut(arrows_4))
        self.wait(1)

        # Final message explaining Pascal's Triangle
        message = Text("Each number is the sum of the two above!", font_size=32).move_to(DOWN * 2)
        self.play(Write(message))
        self.wait(3)
        self.play(FadeOut(message))

        message = Text("Each number is the sum of the two above!", font_size=32).move_to(DOWN * 2)
        self.play(Write(message))
        self.wait(3)
        self.play(FadeOut(message))
