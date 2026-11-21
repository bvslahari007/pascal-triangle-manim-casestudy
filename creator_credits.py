from manim import *

class VideoCreators(Scene):
    def construct(self):
        title = Text("Video created by", font_size=48, color=BLUE).to_edge(UP)

        creators = [
            "• Chintala Sejal - 2024021878",
            "• P.G. Yuktha Reddy - 2024024788",
            "• Yadla Sai Sushma - 2024165826",
            "• Baswa Vinaya Sangeeta Lahari - 2024169782"
        ]

        # Create a list of Text mobjects
        creator_texts = [Text(name, font_size=36) for name in creators]

        # Arrange them vertically
        creator_group = VGroup(*creator_texts).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(title, DOWN, buff=1)

        # Add title
        self.play(Write(title))
        self.wait(0.5)

        # Animate each name one by one
        for creator in creator_texts:
            self.play(FadeIn(creator, shift=UP), run_time=1)
            self.wait(0.3)

        self.wait(2)
