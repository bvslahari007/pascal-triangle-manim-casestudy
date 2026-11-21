from manim import *
import numpy as np
from scipy.special import comb  # For binomial coefficients

class PascalsTriangle(Scene):
    def construct(self):
        self.show_real_life_scenario()
    
    def show_real_life_scenario(self):
        # Introduce the ice cream shop scenario with an icon
        scenario_text = Text("Ice Cream Choices & Pascal's Triangle", font_size=42)
        self.play(Write(scenario_text))
        self.wait(3)
        self.play(FadeOut(scenario_text))
        
        # Explain the problem with an illustration
        problem_text = Text("You have 5 flavors, and can choose 3 scoops. How many ways?", font_size=36)
        problem_text.to_edge(UP)
        
        flavor_labels = ["Chocolate", "Vanilla", "Strawberry", "Mango", "Pistachio"]
        flavor_nodes = [Circle(radius=0.5, color=WHITE).move_to((i - 2, 2, 0)) for i in range(5)]
        flavor_texts = [Text(flavor, font_size=24).move_to(node.get_center()) for flavor, node in zip(flavor_labels, flavor_nodes)]
        
        flavors_group = VGroup(*flavor_nodes, *flavor_texts)
        self.play(Write(problem_text), FadeIn(flavors_group))
        self.wait(3)
        
        # Draw the tree structure dynamically
        start_node = Circle(radius=0.5, color=YELLOW).move_to(UP * 3)
        start_text = Text("Start", font_size=28).move_to(start_node.get_center())
        self.play(FadeIn(start_node, start_text))
        self.wait(2)
        
        level1_lines = [Line(start_node.get_bottom(), node.get_top(), color=WHITE) for node in flavor_nodes]
        self.play(*[Create(line) for line in level1_lines])
        self.wait(2)
        
        # Create second level (choosing second scoop)
        second_level_nodes = []
        second_level_texts = []
        second_level_lines = []
        
        for i, parent_node in enumerate(flavor_nodes):
            for j in range(5):
                new_node = Circle(radius=0.4, color=BLUE).move_to(parent_node.get_center() + DOWN * 2 + (j - 2) * RIGHT * 1)
                new_text = Text(flavor_labels[j], font_size=20).move_to(new_node.get_center())
                second_level_nodes.append(new_node)
                second_level_texts.append(new_text)
                second_level_lines.append(Line(parent_node.get_bottom(), new_node.get_top(), color=WHITE))
        
        self.play(*[Create(line) for line in second_level_lines], *[FadeIn(node, text) for node, text in zip(second_level_nodes, second_level_texts)])
        self.wait(3)
        
        # Transition to Pascal’s Triangle using an arrow animation
        pascal_transition = Text("Pascal’s Triangle holds the answer!", font_size=38, color=BLUE)
        pascal_transition.next_to(problem_text, DOWN)
        arrow = Arrow(problem_text.get_bottom(), pascal_transition.get_top(), buff=0.1, color=WHITE)
        
        self.play(Write(pascal_transition), GrowArrow(arrow))
        self.wait(3)
        self.play(FadeOut(problem_text, flavors_group, pascal_transition, arrow))