from manim import *

class PascalTriangleSymmetry(Scene):
    def generate_pascals_triangle(self, rows):
        triangle = [[1]]
        for i in range(1, rows):
            new_row = [1]
            for j in range(len(triangle[-1]) - 1):
                new_row.append(triangle[-1][j] + triangle[-1][j + 1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle

    def construct(self):
        rows = 6  # Keep only 6 rows
        triangle = self.generate_pascals_triangle(rows)

        # Title
        title = Text("Symmetry in Pascal’s Triangle", font_size=36)
        title.to_edge(UP, buff=0.5)  # Move title slightly down
        self.play(Write(title))

        elements = []
        y_start = 1.5  # Move triangle downward

        for i, row in enumerate(triangle):
            x_offset = -len(row) / 2  # Adjust to center each row
            row_elements = []
            for j, num in enumerate(row):
                num_text = Text(str(num), font_size=30, color=WHITE, font="Times New Roman")  # Font adjusted
                num_text.move_to(np.array([x_offset + j, y_start - i * 0.7, 0]))  # Better spacing
                row_elements.append(num_text)
            elements.append(row_elements)

        full_group = VGroup(*[num for row in elements for num in row])
        self.play(FadeIn(full_group, run_time=2))  # Faded-in motion effect
        self.wait(1)

        # Apply highlights for symmetry (slower effect)
        highlight_anims = []
        for i, row in enumerate(elements):
            for j in range(len(row) // 2):
                row[j].set_color(BLUE)
                row[-(j + 1)].set_color(RED)
                highlight_anims.append(Indicate(row[j], scale_factor=1.2, run_time=0.8))
                highlight_anims.append(Indicate(row[-(j + 1)], scale_factor=1.2, run_time=0.8))

        self.play(*highlight_anims, run_time=2.5)  # Adjusted for better timing

        # Final Message (Properly aligned)
        message = Text("Each number on the left mirrors the number on the right!", font_size=24, color=YELLOW)
        message.next_to(full_group, DOWN, buff=0.75)  # Ensuring it's placed BELOW the triangle
        self.play(Write(message))

        self.wait(2)  # Pause before ending