from manim import *
import math

class BinomialPascalFinal(Scene):
    def construct(self):
        # Configure settings with Times New Roman font
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{mathptmx}")  # Times New Roman
        
        # Title with optimized size
        title = Tex("Binomial Expansion \\& Pascal's Triangle", 
                   font_size=46,  # Slightly reduced from 54
                   tex_template=template)
        self.play(Write(title, run_time=1.25))
        self.wait(0.75)
        self.play(title.animate.to_edge(UP, buff=0.5), run_time=0.75)
        self.wait(0.5)
        
        # Create Pascal's Triangle with optimized size
        pascal_triangle = self.create_classic_pascal_triangle(3)
        pascal_triangle.to_edge(RIGHT, buff=1)
        self.play(FadeIn(pascal_triangle, run_time=1.25))
        self.wait(0.5)
        
        # Show expansions with adjusted size
        for n in range(4):
            self.show_expansion_with_pascal(n, pascal_triangle, template)
            self.wait(0.75)
        
        # Final conclusion with optimized size
        conclusion = Tex(
            "The coefficients in the expansion\\\\",
            "exactly match the numbers\\\\", 
            "in Pascal's Triangle!",
            tex_template=template,
            font_size=38  # Slightly reduced from 42
        )
        conclusion.move_to(LEFT*3)
        self.play(Write(conclusion, run_time=2.0))
        self.wait(3)
    
    def create_classic_pascal_triangle(self, max_n):
        """Create Pascal's Triangle with optimized size"""
        rows = VGroup()
        for n in range(max_n + 1):
            row = VGroup()
            for k in range(n + 1):
                coeff = str(math.comb(n, k))
                num = Text(coeff, font="Times New Roman", font_size=38)  # Reduced from 42
                num.set_opacity(0.3)
                row.add(num)
            row.arrange(RIGHT, buff=0.6)  # Slightly reduced spacing
            rows.add(row)
        rows.arrange(DOWN, center=True, buff=0.6)  # Slightly reduced spacing
        return rows
    
    def show_expansion_with_pascal(self, n, pascal_triangle, template):
        """Animation with optimized equation size"""
        try:
            expansion = self.get_explicit_binomial_expansion(n, template)
            if not hasattr(expansion, 'terms'):
                return False
                
            expansion.scale(1.1)  # Slightly reduced from 1.2
            expansion.to_edge(LEFT, buff=1)
            
            self.play(Write(expansion, run_time=1.25))
            self.wait(0.5)
            
            pascal_row = pascal_triangle[n]
            pascal_highlights = VGroup()
            for num in pascal_row:
                box = SurroundingRectangle(num, color=BLUE, fill_opacity=0.2, buff=0.15)
                pascal_highlights.add(box)
            
            for i in range(len(expansion.terms)):
                term = expansion.terms[i]
                coeff_highlight = SurroundingRectangle(
                    term.coeff_part, color=YELLOW, buff=0.08, stroke_width=3  # Slightly thinner
                )
                
                self.play(
                    term.coeff_part.animate.set_color(YELLOW),
                    Create(coeff_highlight, run_time=0.75),
                    pascal_row[i].animate.set_opacity(1),
                    Create(pascal_highlights[i], run_time=0.75),
                )
                self.wait(0.5)
                
                self.play(
                    FadeOut(coeff_highlight, run_time=0.5),
                    term.coeff_part.animate.set_color(WHITE),
                    FadeOut(pascal_highlights[i], run_time=0.5),
                )
            
            self.play(FadeOut(expansion, run_time=1.0))
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
    
    def get_explicit_binomial_expansion(self, n, template):
        """Create equations with optimized size"""
        terms = VGroup()
        expansion = VGroup(MathTex(f"(x + y)^{{{n}}} = ", 
                               tex_template=template, 
                               font_size=42))  # Reduced from 48
        
        for k in range(n + 1):
            coeff = math.comb(n, k)
            x_exp = n - k
            y_exp = k
            
            # Build term with explicit coefficient
            term_str = f"{coeff}"
            if x_exp > 0:
                term_str += f"x^{{{x_exp}}}" if x_exp > 1 else "x"
            if y_exp > 0:
                term_str += f"y^{{{y_exp}}}" if y_exp > 1 else "y"
            
            term = MathTex(term_str, 
                       tex_template=template, 
                       font_size=42)  # Reduced from 48
            
            # Mark coefficient part
            term.coeff_part = term[0][:len(str(coeff))] if len(term[0]) > 0 else term[0]
            
            terms.add(term)
            if k > 0:
                expansion.add(MathTex("+", 
                                 tex_template=template, 
                                 font_size=42))  # Reduced from 48
            expansion.add(term)
        
        expansion.arrange(RIGHT, buff=0.35)  # Slightly reduced spacing
        expansion.terms = terms
        return expansion