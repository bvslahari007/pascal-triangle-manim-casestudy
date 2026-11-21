from manim import *

class PascalsTriangle(Scene):
    def construct(self):
        self.show_flow_chart()
        self.wait(2)
        self.show_real_life_scenario()
    
    def show_flow_chart(self):
        # Title
        title = Text("Pascal's Triangle Tree Diagram", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Define nodes for first few rows
        row_spacing = 1.2  # Adjust spacing between rows
        col_spacing = 1.8  # Adjust spacing between columns
        nodes = {
            (0, 0): (0, 3, 0),
            (1, 0): (-col_spacing/2, 3-row_spacing, 0), (1, 1): (col_spacing/2, 3-row_spacing, 0),
            (2, 0): (-col_spacing, 3-2*row_spacing, 0), (2, 1): (0, 3-2*row_spacing, 0), (2, 2): (col_spacing, 3-2*row_spacing, 0),
            (3, 0): (-1.5*col_spacing, 3-3*row_spacing, 0), (3, 1): (-0.5*col_spacing, 3-3*row_spacing, 0), 
            (3, 2): (0.5*col_spacing, 3-3*row_spacing, 0), (3, 3): (1.5*col_spacing, 3-3*row_spacing, 0),
        }

        # Define connections
        edges = [
            ((0, 0), (1, 0)), ((0, 0), (1, 1)),
            ((1, 0), (2, 0)), ((1, 0), (2, 1)),
            ((1, 1), (2, 1)), ((1, 1), (2, 2)),
            ((2, 0), (3, 0)), ((2, 0), (3, 1)),
            ((2, 1), (3, 1)), ((2, 1), (3, 2)),
            ((2, 2), (3, 2)), ((2, 2), (3, 3)),
        ]

        circles = {}
        labels = {}

        # Create nodes
        for key, pos in nodes.items():
            circles[key] = Circle(radius=0.25, color=WHITE).move_to(pos)
            labels[key] = Text("1", font_size=24).move_to(pos)

        # Create edges
        lines = [Line(circles[start].get_bottom(), circles[end].get_top(), color=WHITE) for start, end in edges]

        # Animate tree appearance
        self.play(*[FadeIn(circles[key], labels[key]) for key in circles])
        self.play(*[Create(line) for line in lines])
        self.wait(1)

        # Explanation with arrows
        explanation_texts = [
            ("Start with 1 at the top", (0, 3.5, 0)),
            ("Each number splits into two branches", (-2, 2.5, 0)),
            ("Numbers add up when merging", (-3, 1.5, 0)),
            ("Forms an inverted triangle!", (-3.5, 0.5, 0)),
        ]
        
        for text, pos in explanation_texts:
            explanation = Text(text, font_size=28).move_to(pos)
            arrow = Arrow(start=pos, end=(pos[0], pos[1] - 0.5, 0), buff=0.2, color=YELLOW)
            self.play(GrowArrow(arrow), Write(explanation))
            self.wait(2)
            self.play(FadeOut(explanation), FadeOut(arrow))
        
    def show_real_life_scenario(self):
        self.play(FadeOut(*self.mobjects))  # Clear previous scene
        
        # Real-life analogy explanation
        explanation_texts = [
            "Row 0: An empty bowl (1 scoop option starts).",
            "Row 1: Choose a single scoop or none (1 1).",
            "Row 2: Two flavors 🍫 & 🍦 (1 2 1).",
            "Mixing order: 🍫-🍦, 🍦-🍫, or single scoops!",
            "Row 3: Three flavors 🍫, 🍦, 🍓 (1 3 3 1).",
            "More combinations: 🍫-🍦-🍓, 🍦-🍫-🍓, ..."
        ]
        
        text_objects = VGroup(*[Text(t, font_size=30).to_edge(UP) for t in explanation_texts])
        
        for text in text_objects:
            self.play(Write(text))
            self.wait(1.5)
            self.play(FadeOut(text))
        
        self.wait(2)
