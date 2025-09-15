from manim import *
from math import comb

class FinalPositionedFibonacciPascal(Scene):
    def construct(self):
        # Configuration (keeping all original settings)
        max_rows = 7
        triangle_scale = 0.9
        animation_speed = 1.5
        
        # Create Pascal's Triangle (original code)
        triangle = VGroup()
        for row in range(max_rows):
            new_row = VGroup()
            for col in range(row + 1):
                num = comb(row, col)
                number = Integer(num).scale(triangle_scale)
                new_row.add(number)
            new_row.arrange(RIGHT, buff=0.7)
            triangle.add(new_row)
        
        triangle.arrange(DOWN, aligned_edge=ORIGIN, buff=0.6)
        
        # Original animation for triangle creation
        if triangle:
            self.play(LaggedStart(
                *(FadeIn(row, shift=DOWN*0.3) for row in triangle),
                lag_ratio=0.2,
                run_time=2/animation_speed
            ))
        self.wait(0.5/animation_speed)

        # ONLY CHANGE: Fibonacci display on RIGHT
        fib_numbers = VGroup()
        fib_title = Text("Fibonacci Sequence:", font_size=36)
        fib_title.to_edge(UP + RIGHT).shift(DOWN*0.5)  # Right side
        self.play(Write(fib_title))

        # Process diagonals (original code)
        for diag in range(max_rows):
            positions = []
            for i in range(diag + 1):
                j = diag - i
                if i < len(triangle) and j < len(triangle[i]):
                    positions.append((i, j))
            
            if not positions:
                continue
                
            highlights = VGroup(*[
                SurroundingRectangle(triangle[i][j], color=YELLOW, 
                                  buff=0.15, fill_opacity=0.2)
                for i,j in positions
            ])
            
            numbers_copy = VGroup(*[
                triangle[i][j].copy().set_color(YELLOW) 
                for i,j in positions
            ])
            
            # ONLY CHANGE: Addition calculations on LEFT
            numbers_copy.arrange(RIGHT, buff=0.5)
            numbers_copy.to_edge(LEFT).shift(DOWN * (0.5 + diag*0.3))  # Left side
            
            plus_signs = VGroup()
            if len(numbers_copy) > 1:
                plus_signs = VGroup(*[
                    Text("+", font_size=32).next_to(numbers_copy[k], RIGHT, buff=0.1)
                    for k in range(len(numbers_copy)-1)
                ])
            
            # Original highlight animation
            self.play(
                *[Create(hl) for hl in highlights],
                *[triangle[i][j].animate.set_color(YELLOW).scale(1.1) 
                  for i,j in positions],
                run_time=0.8/animation_speed
            )
            
            # Original sum animation
            anims = [FadeIn(numbers_copy)]
            if plus_signs:
                anims.append(Write(plus_signs))
            
            self.play(*anims, run_time=1.0/animation_speed)
            
            # Calculate and show result (on left)
            fib_num = sum(triangle[i][j].get_value() for i,j in positions)
            equals = Text("=", font_size=32).next_to(numbers_copy[-1], RIGHT, buff=0.2)
            result = Integer(fib_num, color=GREEN).next_to(equals, RIGHT, buff=0.2)
            
            self.play(
                Write(equals),
                Write(result),
                run_time=0.6/animation_speed
            )
            self.wait(0.3/animation_speed)
            
            # ONLY CHANGE: Fibonacci markers stay on RIGHT
            fib_marker = VGroup(
                Text(f"F{diag+1} =", font_size=28),
                Integer(fib_num, color=GREEN, font_size=32)
            ).arrange(RIGHT, buff=0.2)
            
            if diag == 0:
                fib_marker.next_to(fib_title, DOWN, buff=0.5)
            else:
                fib_marker.next_to(fib_numbers[-1], DOWN, buff=0.3, aligned_edge=LEFT)
            
            fib_numbers.add(fib_marker)
            self.play(FadeIn(fib_marker), run_time=0.5/animation_speed)
            
            # Original cleanup
            cleanup_anims = [
                FadeOut(highlights),
                FadeOut(numbers_copy),
                *[triangle[i][j].animate.set_color(WHITE).scale(1/1.1) for i,j in positions]
            ]
            if plus_signs:
                cleanup_anims.append(FadeOut(plus_signs))
            cleanup_anims.extend([FadeOut(equals), FadeOut(result)])
            
            self.play(*cleanup_anims, run_time=1.0/animation_speed)
        
        # Original final reveal
        if triangle:
            self.play(FadeOut(triangle), run_time=1/animation_speed)
        
        final_text = VGroup(
            Text("The diagonal sums form", font_size=36, color=GOLD),
            Text("the Fibonacci sequence!", font_size=36, color=GOLD),
            Text("1, 1, 2, 3, 5, 8, 13...", font_size=32, color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        final_text.move_to(ORIGIN).shift(DOWN*0.5)
        
        self.play(Write(final_text[0]))
        self.play(Write(final_text[1]))
        self.play(Write(final_text[2]))
        
        if fib_numbers:
            self.play(
                fib_numbers.animate.set_color(GOLD).scale(1.1),
                run_time=1.5/animation_speed
            )
        
        self.wait(2/animation_speed)
        if self.mobjects:
            self.play(
                *[FadeOut(mob) for mob in self.mobjects],
                run_time=1.5/animation_speed
            )