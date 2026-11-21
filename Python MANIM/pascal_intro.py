from manim import *
import math

class PascalsTriangleIntroduction(Scene):
    def construct(self):
        # Set the default font
        Text.set_default(font="Times New Roman")
        
        # SCENE 1: Single 1 with intriguing text
        one = Text("1", font_size=96)
        self.play(FadeIn(one), run_time=0.8)
        self.wait(0.4)
        
        text1 = Text("Imagine a simple pattern of numbers...", 
                   font_size=36).to_edge(DOWN)
        self.play(FadeIn(text1), run_time=0.8)
        self.wait(1.2)
        
        text2 = Text("From a single seed grows mathematical wonder...", 
                   font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(text1, run_time=0.6),
            FadeIn(text2, run_time=0.6)
        )
        self.wait(1.2)
        
        # Add "Let's dive in" text
        lets_dive = Text("Let's dive in!", 
                       font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(text2, run_time=0.6),
            FadeIn(lets_dive, run_time=0.6)
        )
        self.wait(0.8)
        
        # SCENE 2: Build Pascal's Triangle starting from the single 1
        self.play(FadeOut(lets_dive, run_time=0.6))
        
        # Create the triangle
        triangle = self.build_pascals_triangle(6)
        
        # Save the position of the top element of the triangle
        top_position = triangle[0][0].get_center()
        
        # Move the initial "1" to the position of the top element of the triangle
        self.play(
            one.animate.scale(0.33).move_to(top_position),
            run_time=1.2
        )
        self.wait(0.4)
        
        # Remove the top element from the triangle to avoid duplication
        original_top = triangle[0][0]
        triangle[0].remove(original_top)
        
        # If the first row is now empty, remove it from the triangle
        if len(triangle[0]) == 0:
            first_row = triangle[0]
            triangle.remove(first_row)
        
        # Add the rows of the triangle one by one
        for i in range(len(triangle)):
            self.play(FadeIn(triangle[i]), run_time=0.35)
        
        # Now add the original 1 to the first row of the triangle VGroup
        # so it's part of the triangle for future operations
        triangle.add_to_back(one)  # Add to back so it appears at the top visually
        
        # Add text to identify this as Pascal's Triangle
        pascal_label = Text("This is Pascal's Triangle", 
                          font_size=36).to_edge(DOWN)
        self.play(FadeIn(pascal_label), run_time=0.8)
        self.wait(1.2)
        
        ancestors_text = Text("Each number, a sum of its ancestors...", 
                            font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(pascal_label, run_time=0.6),
            FadeIn(ancestors_text, run_time=0.6)
        )
        self.wait(1.2)
        
        text3 = Text("Just adding numbers above... or is there more?", 
                   font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(ancestors_text, run_time=0.6),
            FadeIn(text3, run_time=0.6)
        )
        self.wait(1.2)
        
        # SCENE 3: Highlight Patterns
        self.play(FadeOut(text3, run_time=0.6))
        
        patterns_intro = Text("Let's uncover the secrets hidden in plain sight...", 
                            font_size=36).to_edge(DOWN)
        self.play(FadeIn(patterns_intro), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(patterns_intro), run_time=0.6)
        
        # Fibonacci pattern
        fib_high = self.highlight_fibonacci(triangle)
        fib_text = Text("Hidden Fibonacci sequence!", font_size=36).to_edge(DOWN)
        self.play(
            LaggedStart(*[Create(h) for h in fib_high], lag_ratio=0.17),
            FadeIn(fib_text, run_time=0.8)
        )
        self.wait(1.7)
        
        # Powers of 2 pattern
        sum_high = self.highlight_row_sums(triangle)
        powers_intro = Text("The sum of each row tells a story...", 
                          font_size=36).to_edge(DOWN)
        self.play(
            *[Uncreate(h) for h in fib_high],
            FadeOut(fib_text, run_time=0.6),
            FadeIn(powers_intro, run_time=0.6)
        )
        self.wait(1.2)
        
        powers_text = Text("Row sums reveal powers of 2!", font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(powers_intro, run_time=0.6),
            LaggedStart(*[Create(h) for h in sum_high], lag_ratio=0.17),
            FadeIn(powers_text, run_time=0.6)
        )
        self.wait(1.7)
        
        # SCENE 4: Applications - Tree emerging from triangle
        applications_intro = Text("From pure numbers to real-world applications...", 
                                font_size=36).to_edge(DOWN)
        self.play(
            *[FadeOut(h) for h in sum_high],
            FadeOut(powers_text, run_time=0.6),
            FadeIn(applications_intro, run_time=0.6)
        )
        self.wait(1.2)
        
        prob_tree = self.create_probability_tree()
        # Center the probability tree
        prob_tree.move_to(ORIGIN)
        prob_text = Text("Emerging from the triangle... coin flip probabilities!", 
                       font_size=36).to_edge(DOWN)
        
        # Animate triangle morphing into probability tree
        self.play(
            FadeOut(applications_intro, run_time=0.6),
            Transform(triangle, prob_tree, run_time=1.7),
            FadeIn(prob_text, run_time=0.6)
        )
        self.wait(1.7)
        
        # Binomial Theorem Application
        binomial_intro = Text("The mathematical foundation behind countless formulas...", 
                            font_size=36).to_edge(DOWN)
        self.play(
            FadeOut(prob_text, run_time=0.6),
            FadeIn(binomial_intro, run_time=0.6)
        )
        self.wait(1.2)
        
        binomial = MathTex(r"(a+b)^n = \sum_{k=0}^n \binom{n}{k}a^{n-k}b^k").scale(1.2)
        binom_text = Text("The key to binomial expansions!", 
                        font_size=36).to_edge(DOWN)
        box = SurroundingRectangle(binomial, buff=0.3, 
                                color=WHITE, fill_color=BLACK, fill_opacity=1)
        
        # Fade out the tree from center
        self.play(
            FadeOut(triangle, scale=0.5, run_time=1.2),  # Scale down while fading for center effect
            FadeOut(binomial_intro, run_time=0.6)
        )
        
        # Now bring in the binomial
        self.play(
            FadeIn(box, run_time=0.8),
            FadeIn(binomial, run_time=0.8),
            FadeIn(binom_text, run_time=0.8)
        )
        self.wait(1.7)
        
        # FINAL SCENE: Clean separate slide for conclusion
        # First fade out all mathematical content
        self.play(
            FadeOut(box, run_time=0.8),
            FadeOut(binomial, run_time=0.8),
            FadeOut(binom_text, run_time=0.8)
        )
        
        # Clear pause before final reveal
        self.wait(0.4)
        
        transition_text = Text("A triangle so simple, yet endlessly deep...", 
                             font_size=36)
        self.play(FadeIn(transition_text, run_time=0.8))
        self.wait(1.2)
        self.play(FadeOut(transition_text, run_time=0.6))
        self.wait(0.4)
        
        # Create final text elements
        final_title = Text("Pascal's Triangle", font_size=60, weight=BOLD)
        final_subtitle = Text("Where simple patterns reveal profound mathematics",
                            font_size=36).next_to(final_title, DOWN, buff=0.5)
        
        # Animate final text appearing
        self.play(
            FadeIn(final_title, shift=UP, run_time=1.2),
            FadeIn(final_subtitle, shift=DOWN, run_time=1.2)
        )
        self.wait(2.2)
        
        # Add "Let's explore" at the end
        lets_explore = Text("Let's explore!", font_size=42, color=YELLOW)
        lets_explore.next_to(final_subtitle, DOWN, buff=0.7)
        
        self.play(
            FadeIn(lets_explore, run_time=0.8, scale=1.2)  # Scale effect for emphasis
        )
        self.wait(1.5)
        
        # Graceful exit - fade everything out
        self.play(
            FadeOut(final_title, run_time=0.8),
            FadeOut(final_subtitle, run_time=0.8),
            FadeOut(lets_explore, run_time=0.8)
        )

    # Helper Methods
    def build_pascals_triangle(self, rows):
        tri = VGroup()
        for i in range(rows):
            row = VGroup(*[
                Text(str(math.comb(i,j)), font_size=32)
                for j in range(i+1)
            ])
            row.arrange(RIGHT, buff=0.5)
            tri.add(row)
        tri.arrange(DOWN, buff=0.3, aligned_edge=ORIGIN)
        return tri
    
    def highlight_fibonacci(self, triangle):
        diagonals = [
            [(0,0)], [(1,0)], [(2,0),(1,1)],
            [(3,0),(2,1)], [(4,0),(3,1),(2,2)],
            [(5,0),(4,1),(3,2)]
        ]
        return [
            SurroundingRectangle(
                VGroup(*[triangle[i][j] for i,j in diag 
                      if i<len(triangle) and j<len(triangle[i])]),
                color=YELLOW, buff=0.1)
            for diag in diagonals
        ]
    
    def highlight_row_sums(self, triangle):
        return [
            SurroundingRectangle(row, color=GREEN, buff=0.2)
            for row in triangle
        ]
    
    def create_probability_tree(self):
        levels = 4
        tree = VGroup()
        for i in range(levels):
            level = VGroup(*[
                MathTex(r"\frac{1}{%d}"%2**i).scale(0.7) 
                for _ in range(2**i)
            ])
            level.arrange(RIGHT, buff=1.2).shift(DOWN*i*0.8)
            tree.add(level)
        
        lines = VGroup()
        for i in range(levels-1):
            for j in range(2**i):
                start = tree[i][j].get_center()
                left = tree[i+1][2*j].get_center()
                right = tree[i+1][2*j+1].get_center()
                lines.add(Line(start, left), Line(start, right))
        
        return VGroup(tree, lines)