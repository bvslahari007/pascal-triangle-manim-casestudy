from manim import *

class BinarySearchVisualization(Scene):
    def construct(self):
        # Sorted list
        numbers = [1, 2, 3, 4, 5, 6, 7]
        number_mobs = []

        # Create boxes with numbers
        for i, num in enumerate(numbers):
            box = Square(side_length=1).shift(RIGHT * i)
            text = Text(str(num), font_size=24).move_to(box.get_center())
            number_mobs.append(VGroup(box, text))
        
        number_line = VGroup(*number_mobs)
        number_line.move_to(ORIGIN)
        self.play(LaggedStartMap(FadeIn, number_line))

        # Binary Search Steps (searching for 6)
        low = 0
        high = len(numbers) - 1
        target = 6

        while low <= high:
            mid = (low + high) // 2

            # Highlight current search range
            self.play(
                number_mobs[low][0].animate.set_stroke(color=BLUE, width=4),
                number_mobs[high][0].animate.set_stroke(color=BLUE, width=4)
            )
            self.wait(0.5)

            # Highlight mid
            self.play(number_mobs[mid][0].animate.set_fill(color=YELLOW, opacity=0.5))
            self.wait(1)

            if numbers[mid] == target:
                # Found it!
                self.play(number_mobs[mid][0].animate.set_fill(color=GREEN, opacity=0.7))
                found_text = Text("Found!", font_size=32, color=GREEN).next_to(number_mobs[mid], DOWN)
                self.play(FadeIn(found_text))
                break
            elif numbers[mid] < target:
                # Eliminate left half
                for i in range(low, mid + 1):
                    self.play(number_mobs[i][0].animate.set_fill(color=RED, opacity=0.5), run_time=0.2)
                low = mid + 1
            else:
                # Eliminate right half
                for i in range(mid, high + 1):
                    self.play(number_mobs[i][0].animate.set_fill(color=RED, opacity=0.5), run_time=0.2)
                high = mid - 1

            self.wait(0.5)
