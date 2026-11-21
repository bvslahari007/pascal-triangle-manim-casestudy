from manim import *

class MergeSort(Scene):
    def construct(self):
        # Initial setup
        self.camera.background_color = WHITE
        initial_array = [6, 5, 12, 10, 9, 1]
        array_objects = self.create_array_objects(initial_array)
        array_group = VGroup(*array_objects).arrange(RIGHT, buff=0.5)
        array_group.to_edge(UP, buff=1.5)
        
        # Add initial array
        self.play(FadeIn(array_group))
        self.wait(0.5)
        
        # Build the split tree
        split_tree = self.build_split_tree(array_group)
        self.wait(0.5)
        
        # Build the merge tree
        final_merged = self.build_merge_tree(split_tree)
        self.wait(1)
        
        # Show final sorted array
        final_sorted = self.create_array_objects(sorted(initial_array))
        final_group = VGroup(*final_sorted).arrange(RIGHT, buff=0.5)
        final_group.next_to(array_group, DOWN, buff=3)
        
        # Animate moving the merged result to final position
        self.play(Transform(final_merged.copy(), final_group))
        self.wait(2)
    
    def create_array_objects(self, array):
        """Create rectangle objects for each array element"""
        elements = []
        for num in array:
            rect = Rectangle(
                width=1, height=1, 
                fill_color=BLUE_D, 
                fill_opacity=1, 
                stroke_color=BLACK,
                stroke_width=2
            )
            text = Text(str(num), color=WHITE, font_size=24)
            group = VGroup(rect, text).scale(0.7)
            elements.append(group)
        return elements
    
    def build_split_tree(self, parent_group):
        """Recursively split arrays and animate the process"""
        if len(parent_group) <= 1:
            return {'node': parent_group, 'children': []}
        
        # Split the array
        mid = len(parent_group) // 2
        left_group = VGroup(*parent_group[:mid]).arrange(RIGHT, buff=0.5)
        right_group = VGroup(*parent_group[mid:]).arrange(RIGHT, buff=0.5)
        
        # Position the split arrays
        left_group.next_to(parent_group, DOWN + LEFT, buff=1.5)
        right_group.next_to(parent_group, DOWN + RIGHT, buff=1.5)
        
        # Create connecting lines
        left_line = Line(
            parent_group.get_bottom(), 
            left_group.get_top(), 
            color=BLACK,
            stroke_width=2
        )
        right_line = Line(
            parent_group.get_bottom(), 
            right_group.get_top(), 
            color=BLACK,
            stroke_width=2
        )
        
        # Animate the split
        self.play(
            Create(left_line),
            Create(right_line),
            FadeIn(left_group, shift=DOWN*0.5),
            FadeIn(right_group, shift=DOWN*0.5),
            run_time=1
        )
        self.wait(0.3)
        
        # Recursively split left and right
        left_tree = self.build_split_tree(left_group)
        right_tree = self.build_split_tree(right_group)
        
        return {
            'node': parent_group,
            'left_line': left_line,
            'right_line': right_line,
            'left_child': left_tree,
            'right_child': right_tree
        }
    
    def build_merge_tree(self, tree):
        """Recursively merge arrays and animate the process"""
        if not tree.get('left_child') and len(tree['node']) == 1:
            return tree['node']
        
        # Process left and right subtrees
        left_merged = self.build_merge_tree(tree['left_child'])
        right_merged = self.build_merge_tree(tree['right_child'])
        
        # Get the arrays to merge
        left_array = left_merged
        right_array = right_merged
        
        # Get numerical values
        left_values = [int(t[1].text) for t in left_array]
        right_values = [int(t[1].text) for t in right_array]
        
        # Create temporary group for merge animation
        temp_group = VGroup()
        merged_objects = []
        i = j = 0
        
        # Position for merged elements
        merge_pos = tree['node'].get_center() + DOWN * 3
        
        while i < len(left_values) and j < len(right_values):
            # Highlight elements being compared
            self.play(
                left_array[i].animate.set_fill(RED),
                right_array[j].animate.set_fill(RED),
                run_time=0.5
            )
            self.wait(0.3)
            
            if left_values[i] <= right_values[j]:
                new_obj = left_array[i].copy()
                merged_objects.append(left_values[i])
                i += 1
            else:
                new_obj = right_array[j].copy()
                merged_objects.append(right_values[j])
                j += 1
                
            temp_group.add(new_obj)
            new_obj.move_to(merge_pos + RIGHT * (len(temp_group) - 1) * 1.5)
            self.play(FadeIn(new_obj, shift=UP*0.5), run_time=0.5)
            
            # Reset colors
            if i > 0:
                self.play(left_array[i-1].animate.set_fill(BLUE_D), run_time=0.3)
            if j > 0:
                self.play(right_array[j-1].animate.set_fill(BLUE_D), run_time=0.3)
        
        # Add remaining elements from left
        while i < len(left_values):
            new_obj = left_array[i].copy()
            merged_objects.append(left_values[i])
            temp_group.add(new_obj)
            new_obj.move_to(merge_pos + RIGHT * (len(temp_group) - 1) * 1.5)
            self.play(FadeIn(new_obj, shift=UP*0.5), run_time=0.5)
            i += 1
        
        # Add remaining elements from right
        while j < len(right_values):
            new_obj = right_array[j].copy()
            merged_objects.append(right_values[j])
            temp_group.add(new_obj)
            new_obj.move_to(merge_pos + RIGHT * (len(temp_group) - 1) * 1.5)
            self.play(FadeIn(new_obj, shift=UP*0.5), run_time=0.5)
            j += 1
        
        # Create properly arranged merged group
        merged_group = VGroup()
        for i, obj in enumerate(temp_group):
            new_obj = obj.copy()
            merged_group.add(new_obj)
        merged_group.arrange(RIGHT, buff=0.5)
        merged_group.next_to(tree['node'], DOWN, buff=1.5)
        
        # Create connecting lines
        left_merge_line = Line(
            left_array.get_bottom(), 
            merged_group.get_top(), 
            color=BLACK,
            stroke_width=2
        )
        right_merge_line = Line(
            right_array.get_bottom(), 
            merged_group.get_top(), 
            color=BLACK,
            stroke_width=2
        )
        
        # Animate the merge
        self.play(
            ReplacementTransform(temp_group, merged_group),
            Create(left_merge_line),
            Create(right_merge_line),
            run_time=1
        )
        self.wait(0.5)
        
        return merged_group