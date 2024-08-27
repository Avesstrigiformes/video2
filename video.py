from manim import *
class Video(Scene): 
    def construct(self):

        #define a cancel out function
        
        def cancel(mob):
            return Line(mob.get_corner(UR), mob.get_corner(DL), color=RED)

        #expressions

        placeholder = Dot([-6,3,0])
        PROBLEM = Tex(r"In this video we will prove the Euler-Lagrange equation:$$\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)-\frac{\partial F}{\partial y}=0$$")
        t = Tex(r"Proof:").shift(DOWN)
        PROBLEM.next_to(placeholder, DOWN, aligned_edge=LEFT)
        rect = SurroundingRectangle(PROBLEM, fill_color=WHITE, fill_opacity=0.2, buff=0.1, color=BLUE)
        rect.set_z_index(-1)

        c1 = Tex(r"Let's start with definitions:",color=RED).shift(UP*3)
        definitions = [
            Tex(r"$F(x,y(x),y'(x))$ is a function whose inputs are functions").shift(DOWN),
            Tex(r"We want to find a $y(x)$ which should be an extremum of\\ $\int_{x_{1}}^{x_{2}}F(x,y(x),y'(x))dx$").shift(DOWN),
            Tex(r"By considering a general case,\\ we expect to find a nice equation for $y(x)$").shift(DOWN)
        ]
        temp = Tex(r"$F(x,y(x),y'(x))$ is a ",r"functional")
        m1 = Tex(r"Before the proof, I want to explain why it is useful to minimize $F$:\\ Principle of least action states that a particle moves the path of\\ function that minimizes the Lagrangian, which is also a functional.\\Thanks to this equation, we can find $y(x)$ that satisfies the conditions.",font_size=40,stroke_color=GOLD)
        t1_1 = MathTex(r"\text{Consider: }\bar{y}(x)=y(x)+\varepsilon\cdot\eta(x)",color=RED).shift(UP*3,LEFT*3.5).scale(0.9)
        t1_1_5 = Tex(r"$\eta(x)$ is a function that is twice differentiable\\ with each derivative continuous on the interval $[x_{1},x_{2}]$", color=RED).to_edge(DOWN).scale(0.9)
        t1_2 = MathTex(r"\text{Note that: }\eta(x_{1})=\eta(x_{2})=0",color=RED).shift(UP*3,RIGHT*3.5).scale(0.9)
        animations1 =[
            FadeIn(t1_1, target_position=0, scale=0.6, run_time=1),
            FadeIn(t1_1_5, target_position=0, scale=0.6, run_time=1),
            FadeIn(t1_2, target_position=0, scale=0.6, run_time=1)
        ]
        t1_3 = [MathTex(r"\underbrace{\int_{x_{1}}^{x_{2}}F(x,\bar{y}(x),\bar{y}'(x))dx}_{\text{This function depends on } \varepsilon}").shift(UP),
                MathTex(r"\int_{x_{1}}^{x_{2}}F(x,\bar{y}(x),\bar{y}'(x))dx:=I(\varepsilon)").shift(UP),
                MathTex(r"\int_{x_{1}}^{x_{2}}F(x,\bar{y}(x),\bar{y}'(x))dx").shift(UP)]
        t1_3_1 = MathTex(r"\underbrace{\qquad\qquad\qquad\qquad\qquad}_{\text{We know that this function is minimized when }\varepsilon=0}").next_to(t1_3[2],DOWN)
        t1_4 = MathTex(r"\frac{dI(\varepsilon)}{d\varepsilon}\Bigg|_{\varepsilon=0}=0", color=GREEN).to_corner(UL)
        r1 = MathTex(*r"\text{Recall: If }F(x(t),y(t)),$\\\frac{dF}{dt}=\frac{\partial F}{\partial x}\cdot\frac{dx}{dt} + \frac{\partial F}{\partial y}\cdot\frac{dy}{dt}".split("$"),stroke_color=GOLD).shift(UP)
        r2 = MathTex(*r"\text{Recall: If }F(x,\bar{y}(x),\bar{y}'(x)),$\\\frac{dF}{d\varepsilon}=\frac{\partial F}{\partial x}\cdot\frac{dx}{d\varepsilon} + \frac{\partial F}{\partial\bar{y}}\cdot\frac{d\bar{y}}{d\varepsilon} + \frac{\partial F}{\partial\bar{y}'}\cdot\frac{d\bar{y}'}{d\varepsilon}".split("$"),stroke_color=GOLD).shift(UP)
        r3 = MathTex(r"\frac{dF}{d\varepsilon}=\frac{\partial F}{\partial\bar{y}}\cdot\frac{d\ y(x)+\varepsilon\cdot\eta(x)}{d\varepsilon} + \frac{\partial F}{\partial\bar{y}'}\cdot\frac{d\ y'(x)+\varepsilon\cdot\eta'(x)}{d\varepsilon}").move_to(r2[1])
        r4 = MathTex(r"\frac{dF}{d\varepsilon}=\frac{\partial F}{\partial\bar{y}}\cdot\eta(x)+\frac{\partial F}{\partial\bar{y}'}\cdot\eta'(x)", color=GREEN).to_corner(UR)
        z = Tex(r"0", color=RED).move_to(r2[1][12:17])
        z2 = MathTex(r"\eta(x)", color=RED).move_to(r3[0][13:28])
        z3 = MathTex(r"\eta'(x)", color=RED).move_to(r3[0][37::])
        
        f1 = MathTex(r"\frac{dI}{d\varepsilon}=\int_{x_{1}}^{x_{2}}\frac{dF}{d\varepsilon}dx")
        info = Tex(r"when $\varepsilon=0$").shift(DOWN)
        info2 = Tex(r"Since $\varepsilon=0,\bar{y}=y$")
        info3 = Tex(r"Recall that $\eta(x_{1})=\eta(x_{2})=0$", color=RED)
        new1 = MathTex(r"y").set_color(RED)
        new2 = MathTex(r"y'").set_color(RED)
        f2 = Tex(r"If we apply integration by parts to the second term, we get:")
        f3 = MathTex(r"\int_{x_{1}}^{x_{2}}\frac{\partial F}{\partial y'}\cdot\eta'(x)dx=\frac{\partial F}{\partial y'}\cdot\eta(x)\Bigg|_{x_{1}}^{x_{2}}-\int_{x_{1}}^{x_{2}}\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)\cdot\eta(x)dx").shift(DOWN*0.9)
        f4 = MathTex(r"\int_{x_{1}}^{x_{2}}\left[\frac{\partial F}{\partial y}-\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)\right]\eta(x)dx=0").shift(UP*1.5)
        f5 = Tex(r"Since $\eta(x)$ is arbitrary, therefore first term must be equal to 0\\by the fundamental lemma of calculus of variations.")
        f6 = Union(*MathTex(r"\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)-\frac{\partial F}{\partial y}=0").copy()[0]).scale(2).set_stroke(width=0).set_fill(opacity=1).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)
        line = cancel(f3[0][20:40])
        sqr = Square(side_length=0.25).next_to(f6,RIGHT)
        tfw = Union(*Tex(r"Thanks For Watching").scale(2).copy()[0]).set_color_by_gradient([PURE_RED, PURE_BLUE]).set_sheen_direction(UR)

        group_ibp = VGroup(f1[0][10::-1],f1[0][16::],r4[0][6::],t1_4[0][-2::],info)
        group_arb = VGroup(f1[0][10::-1],r4[0][6:18],t1_4[0][-2::],info,f3[0][46::])

        #intro

        self.play(Create(rect), Write(PROBLEM), run_time=5)
        self.wait(5)
        self.play(Write(t))
        self.play(Flash(t, line_length=0.5, num_lines=50, color=BLUE, flash_radius=1.1, time_width=0.5, run_time=2, rate_func = rush_from))
        self.play(FadeOut(PROBLEM), FadeOut(t), FadeOut(rect))

        #main 1

        self.play(Write(c1))
        already_shown = VGroup()
        for i in range(3):
            self.play(already_shown.animate.shift(UP*1.4))
            if i == 2:
                self.play(Write(definitions[2],run_time=2.5))
                temp.next_to(definitions[0],0)
                temp.set_color_by_tex(r"functional",YELLOW)
                self.play(Transform(definitions[0],temp))
                self.wait(1)
                break
            self.play(Write(definitions[i]))
            already_shown += definitions[i]
            self.wait(2)
        self.play(FadeOut(already_shown,c1,definitions[2]))
        self.play(Write(m1,run_time=5))
        self.wait(3)
        self.play(FadeOut(m1,run_time=2))
        self.play(AnimationGroup(animations1, lag_ratio=2))
        self.play(Write(t1_3[0]))
        for i in range(2):
            self.wait(3)
            self.play(ReplacementTransform(t1_3[i],t1_3[i+1]))
        self.play(Write(t1_3_1))
        self.wait(1)
        self.play(FadeOut(t1_3[2]))
        self.play(FadeOut(t1_1,t1_1_5,t1_2))

        #main 2
        
        self.play(ReplacementTransform(t1_3_1,t1_4))
        self.play(Write(r1[0]))
        self.play(Write(r1[1]))
        self.wait(3)
        self.play(ReplacementTransform(r1[0],r2[0]),ReplacementTransform(r1[1],r2[1]))
        self.wait(1)
        self.play(ReplacementTransform(r2[1][12:17],z))
        self.wait(1)
        self.play(FadeOut(r2[1][6:18],z),r2[1][18::].animate.shift(LEFT*2.45))
        self.wait(2)
        self.play(FadeOut(r2[1][0:6]),ReplacementTransform(r2[1][18::],r3)) 
        self.wait(2)
        self.play(ReplacementTransform(r3[0][13:28],z2),ReplacementTransform(r3[0][37::],z3))
        self.play(FadeOut(r2[0],z2,z3),ReplacementTransform(r3[0],r4))
        self.wait(2)
        self.play(Write(f1))
        self.wait(1)
        self.play(FadeOut(f1[0][11:16]),f1[0][10::-1].animate.shift(LEFT*3),f1[0][16::].animate.shift(RIGHT*1.45),r4[0][6::].animate.move_to(0).set_color(WHITE),FadeOut(r4[0][5::-1]),t1_4[0][-2::].animate.move_to(RIGHT*3.77).set_color(WHITE),FadeOut(t1_4[0][-3::-1]),run_time=3)
        self.play(Write(info))
        self.play(group_ibp.animate.shift(UP*2.7).set_color(RED))
        self.play(Write(info2))
        self.play(Transform(r4[0][10:12],new1.move_to(r4[0][11])),Transform(r4[0][22:25],new2.move_to(r4[0][22:25].get_center())))
        self.play(Unwrite(info2))
        self.play(DrawBorderThenFill(f2.next_to(info,DOWN)))
        self.play(Write(f3))
        self.wait(4)
        self.play(Create(line))
        self.play(DrawBorderThenFill(info3.next_to(f3,DOWN)))
        self.wait(2)

        #conclusion
        
        self.play(FadeOut(line,f3[0][20:40]))
        self.play(FadeOut(f3[0][:20],f3[0][40:46],info3,group_ibp[2][12::],group_ibp[1]),f3[0][46::].animate.move_to(group_ibp[2][12::].get_center()+RIGHT).set_color(RED),group_ibp[3].animate.shift(RIGHT*1.22),Transform(r4[0][17],MathTex("-", color=RED).move_to(r4[0][17])),run_time=3)
        self.play(f2.animate.scale(0),ReplacementTransform(group_arb,f4),run_time=3)
        self.play(DrawBorderThenFill(f5))
        self.wait(3)
        self.play(f5.animate.scale(0),ReplacementTransform(f4,f6), run_time=2)
        self.play(Create(sqr))
        self.wait(1)
        self.play(Transform(VGroup(f6,sqr),tfw))
        self.wait(3)
