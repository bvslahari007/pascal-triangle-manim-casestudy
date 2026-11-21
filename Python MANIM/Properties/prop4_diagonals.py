from manim import *

class PascalDiagonalExplained(Scene):
    def construct(self):
        # Set black background
        self.camera.background_color = BLACK
        
        # Title with explanation - properly spaced
        title = Text("Pascal's Triangle", font="Times New Roman", font_size=48)
        subtitle = Text("Hidden Diagonal Patterns", font_size=32, color=GRAY)
        
        # Better positioning of subtitle
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle).center()
        
        self.play(
            Write(title),
            run_time=1.5
        )
        self.play(
            FadeIn(subtitle, shift=DOWN*0.3),
            run_time=1
        )
        self.wait(1)
        
        # Brief intro text - better positioned to avoid overlap
        intro_text = Text(
            "Each diagonal reveals special number sequences",
            font_size=28,
            color=BLUE_C
        ).next_to(subtitle, DOWN, buff=0.5)
        
        self.play(FadeIn(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text), FadeOut(title), FadeOut(subtitle))
        
        # Create classic Pascal's Triangle - improved layout
        rows = 8
        triangle = VGroup()
        numbers = []
        
        # Build the triangle with improved spacing and alignment
        for n in range(rows):
            row = VGroup()
            for k in range(n+1):
                coeff = self.comb(n, k)
                num = Integer(coeff).scale(0.7)
                
                # Position the number - improved triangle geometry
                x = (k - n/2) * 0.8  # Center each row horizontally
                y = -n * 0.8         # Each row is vertically below the previous
                num.move_to(np.array([x, y, 0]))
                
                row.add(num)
            numbers.append(row)
            triangle.add(row)
        
        # Center the triangle and scale for better visibility
        triangle.center().scale(1.2)
        
        # Animate triangle creation
        self.play(
            LaggedStart(*[
                FadeIn(num, scale=1.2)
                for row in numbers
                for num in row
            ], lag_ratio=0.1),
            run_time=3
        )
        self.wait(0.5)
        
        # Diagonal explanations with proper formatting
        diagonals = [
            {
                "index": 0,
                "color": RED,
                "name": "Ones Diagonal",
                "desc": [
                    "These are all 1s.",
                    "No matter how deep you go,",
                    "the edges of Pascal's Triangle are always 1"
                ],
                "wait_time": 3,
                "position": "RIGHT"  # First 3 explanations on the right
            },
            {
                "index": 1,
                "color": GREEN,
                "name": "Natural Numbers",
                "desc": [
                    "1, 2, 3, 4...",
                    "These are natural counting numbers.",
                    "They appear on this second diagonal."
                ],
                "wait_time": 3,
                "position": "RIGHT"  # First 3 explanations on the right
            },
            {
                "index": 2,
                "color": BLUE,
                "name": "Triangular Numbers",
                "desc": [
                    "These numbers form triangle shapes—",
                    "like 1 dot, 3 dots, 6 dots...",
                    "You'd see them if you stack",
                    "balls into a triangle!"
                ],
                "wait_time": 4,
                "position": "LEFT"  # First 3 explanations on the right
            },
            {
                "index": 3,
                "color": GOLD,
                "name": "Tetrahedral Numbers",
                "desc": [
                    "These make a pyramid out of "
                    "triangle numbers.",
                    "Think of stacking triangles"
                    "into a 3D pyramid!"
                ],
                "wait_time": 4,
                "position": "LEFT"  # Last 2 explanations on the left
            },
            {
                "index": 4,
                "color": PURPLE,
                "name": "Pentatope Numbers",
                "desc": [
                    "These represent 4-dimensional simplex numbers.",
                    "They extend the pattern to 4D space!",
                    "Also called 4-simplex or 5-cell numbers."
                ],
                "wait_time": 4,
                "position": "LEFT"  # Last 2 explanations on the left
            }
        ]
        
        # Dim the triangle during explanations
        for diag in diagonals:
            # First dim the entire triangle
            self.play(
                triangle.animate.set_opacity(0.3),
                run_time=0.8
            )
            
            # Get numbers in this diagonal
            diag_numbers = []
            for n in range(diag["index"], rows):
                k = diag["index"]
                if n >= k:
                    diag_numbers.append(numbers[n][k])
            
            # Create highlight boxes
            highlights = VGroup(*[
                SurroundingRectangle(num, color=diag["color"], buff=0.15, fill_opacity=0.2)
                for num in diag_numbers
            ])
            
            # Create explanation text with proper line formatting
            title_text = Text(diag["name"], color=diag["color"], font_size=30)
            
            # Create separate text objects for each line of description
            desc_lines = VGroup(*[
                Text(line, font_size=24, color=WHITE)
                for line in diag["desc"]
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            
            # Group title and description lines
            text_group = VGroup(title_text, desc_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            
            # Position text based on the "position" property
            if diag["position"] == "RIGHT":
                text_group.to_edge(RIGHT, buff=0.7).shift(UP*0.5)
                shift_direction = LEFT*0.3  # Text comes in from the right
            else:
                text_group.to_edge(LEFT, buff=0.7).shift(UP*0.5)
                shift_direction = RIGHT*0.3  # Text comes in from the left
            
            # Animation sequence - highlight the diagonal
            self.play(
                Create(highlights),
                *[num.animate.set_color(diag["color"]).set_opacity(1) for num in diag_numbers],
                run_time=1.5
            )
            self.play(
                FadeIn(text_group, shift=shift_direction),
                run_time=1
            )
            self.wait(diag["wait_time"])
            
            # Clean up
            self.play(
                FadeOut(highlights),
                FadeOut(text_group),
                *[num.animate.set_color(WHITE) for num in diag_numbers],
                run_time=1.5
            )
            
            # Restore the triangle opacity
            self.play(
                triangle.animate.set_opacity(1),
                run_time=0.8
            )
        
        # Fade everything before conclusion
        self.play(FadeOut(triangle), run_time=1.5)
        
        # Final conclusion with proper line formatting
        conclusion_lines = [
            "The diagonals reveal deep mathematical patterns",
            "connecting combinatorics, algebra, and geometry"
        ]
        
        conclusion = VGroup(*[
            Text(line, font_size=28, color=YELLOW)
            for line in conclusion_lines
        ]).arrange(DOWN, buff=0.3).center()
        
        self.play(Write(conclusion), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(conclusion))
        
    def comb(self, n, k):
        """Efficient binomial coefficient calculation"""
        if k < 0 or k > n:
            return 0
        k = min(k, n - k)
        res = 1
        for i in range(1, k+1):
            res = res * (n - k + i) // i
        return res