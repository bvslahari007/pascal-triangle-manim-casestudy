from manim import *
import math

class SierpinskiFromPascal(Scene):
    def construct(self):
        # Configuration
        rows = 15  # For main visualization
        display_rows = 8  # Show this many rows with numbers
        dot_radius = 0.15
        colors = {"odd": WHITE, "even": DARK_GRAY, "bg": BLACK}
        self.camera.background_color = colors["bg"]
        
        # Title with cinematic intro
        title = Text("Sierpinski's Triangle", font="Times New Roman", font_size=42)
        subtitle = Text("Emerging from Pascal's Triangle", font="Times New Roman", font_size=30)
        title_group = Group(title, subtitle.next_to(title, DOWN))
        title_group.to_edge(UP, buff=0.5)
        
        self.play(
            FadeIn(title, shift=UP*0.5),
            rate_func=smooth
        )
        self.play(
            FadeIn(subtitle, shift=UP*0.3),
            rate_func=smooth
        )
        self.wait(1)
        
        # Move title to top
        compact_title = Text("Pascal's Triangle to Sierpinski Triangle", font="Times New Roman", font_size=28)
        compact_title.to_edge(UP, buff=0.3)
        self.play(
            Transform(title_group, compact_title),
            run_time=1.5
        )
        
        # Setup explanation area on left side
        explanation_box = Rectangle(
            width=5, height=7.5, 
            fill_color=colors["bg"], 
            fill_opacity=0.0,
            stroke_width=0
        ).to_edge(LEFT, buff=0.5)
        
        # STEP 1: Clear explanation of Pascal's Triangle
        step1_title = Text("Pascal's Triangle", font="Times New Roman", font_size=28, color=YELLOW)
        step1_title.move_to(explanation_box.get_top() + DOWN*0.7).align_to(explanation_box, LEFT).shift(RIGHT*0.5)
        
        explanation1 = Text(
            "Each number is the sum of the\ntwo numbers above it.\n\n" +
            "First few rows:\n" +
            "Row 0:           1\n" +
            "Row 1:         1   1\n" +
            "Row 2:       1   2   1\n" +
            "Row 3:     1   3   3   1\n" +
            "Row 4:   1   4   6   4   1",
            font="Times New Roman", font_size=22, line_spacing=1.2
        ).next_to(step1_title, DOWN, buff=0.4).align_to(step1_title, LEFT)
        
        self.play(Write(step1_title), run_time=1)
        self.play(Write(explanation1), run_time=2)
        
        # Center triangle higher on the screen
        triangle_center = np.array([3.5, 1.5, 0])  # Moved up by adding Y coordinate
        
        # Build Pascal's Triangle all at once without animation for each row
        triangle_group = Group()
        binomial_values = {}  # Store values for later use
        
        # Create all rows at once
        for n in range(display_rows):
            row_group = Group()
            
            for k in range(n+1):
                # Calculate binomial coefficient
                num = math.comb(n, k)
                binomial_values[(n, k)] = num
                
                # Calculate position - using wider spacing for better readability
                x_pos = (k - n/2) * 0.8  
                y_pos = -n * 0.7  # Vertical spacing
                position = triangle_center + np.array([x_pos, y_pos, 0])
                
                # Create visible number with clear font
                label = Integer(num)
                label.set_color(WHITE).scale(0.8)
                label.move_to(position)
                
                row_group.add(label)
            
            triangle_group.add(row_group)
        
        # Show the entire Pascal triangle at once
        self.play(
            FadeIn(triangle_group),
            run_time=1.5
        )
        self.wait(1)
        
        # STEP 2: Explain modulo 2 operation
        self.play(
            FadeOut(explanation1),
            run_time=0.8
        )
        
        step2_title = Text("Converting to Binary", font="Times New Roman", font_size=28, color=YELLOW)
        step2_title.move_to(step1_title.get_center())
        
        explanation2 = Text(
            "We now apply modulo 2 to every\nnumber in the triangle:\n\n" +
            "• If a number is even, it becomes 0\n" +
            "• If a number is odd, it becomes 1\n\n" +
            "For example:\n" +
            "1 → 1 (odd)\n" +
            "2 → 0 (even)\n" +
            "3 → 1 (odd)\n" +
            "4 → 0 (even)",
            font="Times New Roman", font_size=22, line_spacing=1.2
        ).next_to(step2_title, DOWN, buff=0.4).align_to(step2_title, LEFT)
        
        self.play(
            Transform(step1_title, step2_title),
            Write(explanation2),
            run_time=1.5
        )
        self.wait(1)
        
        # Transform numbers to binary (0 and 1)
        binary_transforms = []
        binary_labels = {}
        
        for n in range(display_rows):
            for k in range(n+1):
                # Calculate position
                x_pos = (k - n/2) * 0.8
                y_pos = -n * 0.7
                position = triangle_center + np.array([x_pos, y_pos, 0])
                
                # Get original number
                num = binomial_values[(n, k)]
                mod_result = num % 2
                
                # Create new label with binary value (0 or 1)
                binary_label = Integer(mod_result)
                binary_label.scale(0.8).move_to(position)
                
                # Color based on value (1=WHITE, 0=GRAY)
                if mod_result == 1:
                    binary_label.set_color(colors["odd"])
                else:
                    binary_label.set_color(colors["even"])
                
                # Find the corresponding original label in triangle_group
                original_label = None
                for row_group in triangle_group:
                    for label in row_group:
                        if np.allclose(label.get_center(), position):
                            original_label = label
                            break
                    if original_label:
                        break
                
                if original_label:
                    binary_transforms.append(Transform(original_label, binary_label))
                    binary_labels[(n, k)] = (original_label, mod_result)
        
        # Show transformation with special effect
        self.play(
            LaggedStart(*binary_transforms, lag_ratio=0.02),
            run_time=3
        )
        self.wait(1)
        
        # STEP 3: Explain Sierpinski pattern
        self.play(
            FadeOut(explanation2),
            run_time=0.8
        )
        
        step3_title = Text("Sierpinski's Triangle Emerges", font="Times New Roman", font_size=28, color=YELLOW)
        step3_title.move_to(step2_title.get_center())
        
        explanation3 = Text(
            "When we color the cells:\n\n" +
            "• 1 (odd) = WHITE\n" +
            "• 0 (even) = BLACK\n\n" +
            "A fractal pattern emerges!\n\n" +
            "This is Sierpinski's Triangle,\na self-similar structure with\ninfinite recursive patterns.",
            font="Times New Roman", font_size=22, line_spacing=1.2
        ).next_to(step3_title, DOWN, buff=0.4).align_to(step3_title, LEFT)
        
        self.play(
            Transform(step1_title, step3_title),
            Write(explanation3),
            run_time=1.5
        )
        
        # Create circle background for each number to make the pattern more visible
        circle_animations = []
        all_circles = VGroup()
        
        for (n, k), (label, mod_result) in binary_labels.items():
            circle = Circle(radius=0.35, stroke_width=0)
            circle.move_to(label.get_center())
            
            if mod_result == 1:  # Odd (1)
                circle.set_fill(colors["odd"], opacity=1)
            else:  # Even (0)
                circle.set_fill(colors["even"], opacity=1)
            
            circle_animations.append(
                GrowFromCenter(circle)
            )
            all_circles.add(circle)
            
            # Add the circle behind the label
            self.add(circle)
            self.remove(circle)
        
        # Play the circle animations
        self.play(
            LaggedStart(*circle_animations, lag_ratio=0.02),
            run_time=2
        )
        
        # Now re-add all circles and labels in the right order
        self.remove(*self.mobjects)
        self.add(title_group, step1_title, explanation3, all_circles)
        for (n, k), (label, _) in binary_labels.items():
            self.add(label)
        
        # Now fade out the numbers to show just the pattern
        number_fadeouts = []
        for (n, k), (label, _) in binary_labels.items():
            number_fadeouts.append(FadeOut(label))
            
        self.play(
            LaggedStart(*number_fadeouts, lag_ratio=0.01),
            run_time=1.5
        )
        
        # STEP 4: Show full Sierpinski pattern
        self.play(
            FadeOut(explanation3),
            run_time=0.8
        )
        
        step4_title = Text("Classic Sierpinski Triangle", font="Times New Roman", font_size=28, color=YELLOW)
        step4_title.move_to(step3_title.get_center())
        
        explanation4 = Text(
            "As we extend to more rows,\nthe classic Sierpinski triangle\nbecomes clear.\n\n" +
            "This elegant fractal has\napplications in mathematics,\ncomputer science, and art.\n\n" +
            "The pattern continues infinitely\nwith perfect self-similarity.",
            font="Times New Roman", font_size=22, line_spacing=1.2
        ).next_to(step4_title, DOWN, buff=0.4).align_to(step4_title, LEFT)
        
        self.play(
            Transform(step1_title, step4_title),
            Write(explanation4),
            run_time=1.5
        )
        
        # Fade out the circles from Pascal representation
        self.play(
            FadeOut(all_circles),
            run_time=1
        )
        
        # Create the classic Sierpinski triangle (using equilateral triangle shape)
                # Create the classic Sierpinski triangle (using equilateral triangle shape)
        sierpinski = self.create_sierpinski(depth=5, size=6)
        sierpinski.move_to(triangle_center + DOWN * 1.5)  # This is the key change
        
        # Dramatically reveal the classic pattern
        self.play(
            FadeIn(sierpinski),
            run_time=2
        )
        
        # Final view to appreciate the pattern
        self.wait(2)
        
        # Final fade out with cinematic effect
        self.play(
            FadeOut(step1_title),
            FadeOut(explanation4),
            FadeOut(title_group),
            FadeOut(sierpinski),
            run_time=2
        )
        # Final view to appreciate the pattern
        self.wait(2)
        
        # Final fade out with cinematic effect
        self.play(
            FadeOut(step1_title),
            FadeOut(explanation4),
            FadeOut(title_group),
            FadeOut(sierpinski),
            run_time=2
        )
    
    def create_sierpinski(self, depth, size):
        """Create a classic Sierpinski triangle with the given depth and size"""
        if depth == 0:
            # Base case: a single triangle
            triangle = Triangle(fill_color=WHITE, fill_opacity=1, stroke_width=0)
            triangle.set_height(size)
            return triangle
        
        # Create three smaller Sierpinski triangles
        sierpinski = VGroup()
        
        sub_triangle = self.create_sierpinski(depth-1, size/2)
        
        # Top triangle
        top = sub_triangle.copy()
        top.shift(UP * size/4)
        
        # Bottom left triangle
        bottom_left = sub_triangle.copy()
        bottom_left.shift(DOWN * size/4 + LEFT * size/4)
        
        # Bottom right triangle
        bottom_right = sub_triangle.copy()
        bottom_right.shift(DOWN * size/4 + RIGHT * size/4)
        
        sierpinski.add(top, bottom_left, bottom_right)
        return sierpinski