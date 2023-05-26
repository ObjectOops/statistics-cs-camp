from manim import *

def FadeOutAll(scene : Scene):
    scene.play(*[FadeOut(i) for i in scene.mobjects])

class Stat_Title(Scene):
    def construct(self):
        title = Text ("CS Camp Pilot Survey Statistics")
        self.play(Write(title))
        self.wait(1)
        FadeOutAll(self)

class Description(Scene):
    def construct(self):
        title = Title ("Description")
        self.play(Write(title))
        description = VGroup(
            Text ("""
Is there an association between grade level and coding experience 
for intermediate school students (around middle school)?""", font_size=24, slant=ITALIC), 
            BulletedList (
                r"$H_0$: There is $\bold{no}$ association between grade level and coding experience.", 
                r"$H_a$: There is $\bold{an}$ association between grade level and coding experience.", 
                font_size=36
            ).move_to(2 * DOWN), 
            Text ("(For intermediate school students.)", 
                font_size=16, slant=ITALIC).move_to(3.5 * DOWN)
        ).next_to(title, 2 * DOWN)
        self.play(Write(description))
        self.wait(1)
        FadeOutAll(self)

class Design_1(Scene):
    def construct(self):
        title = Title ("Design - Process")
        self.play(Write(title))
        process = BulletedList (
            r"Sent out survey to a mailing list \\containing 101 emails (irrelevant questions omitted).", # > 100 cols
            r"Q1: Grade (options - below 6th, 6th, 7th, 8th, 9th, above 9th)", 
            r"Q2: What coding language(s) do you know? \\(at least 1 will be considered coding experience)",  # > 100 cols
            font_size=36
        ).next_to(title, 2 * DOWN)
        self.play(Write(process))
        self.wait(1)
        FadeOutAll(self)

class Design_2(Scene):
    def construct(self):
        title = Title ("Design - Flaws")
        self.play(Write(title))
        flaws = BulletedList (
            r"Nonresponse Bias: Only 22 recipients responded.", 
            r"Convenience Sampling \& Undercoverage: The mailing list is not representative \\of the population of intermediate school students.", # > 100 cols
            font_size=36
        ).next_to(title, 2 * DOWN)
        self.play(Write(flaws))
        self.wait(1)
        FadeOutAll(self)

class Data(Scene):
    def construct(self):
        title = Title ("Aggregated Data")
        self.play(Write(title))
        data = IntegerTable (
            [
                [3, 0, 2, 2, 2, 0, 9], 
                [4, 1, 4, 3, 0, 1, 13], 
                [7, 1, 6, 5, 2, 1, 22]
            ], 
            row_labels=[Text ("Experience"), Text ("No Experience"), Text ("Col Total")], 
            col_labels=[Text (i) for i in [
                "Below 6th", "6th", "7th", "8th", "9th", "Above 9th", "Row Total"
            ]]
        ).next_to(title, DOWN).scale(0.45)
        self.play(Create(data))
        prop = MathTex (
            "\\hat{p}=", "(\\textrm{Experience Total})", "/", "(\\textrm{Total})"
        ).next_to(data, 2 * DOWN)
        stddev = MathTex ("\\sigma=", "\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}").next_to(prop, DOWN) # > 100 cols
        self.play(Write(prop), Write(stddev))
        self.wait(1)
        self.play(
            TransformMatchingTex(prop, MathTex (
                "\\hat{p}=", "9", "/", "22", "\\approx0.41"
            ).next_to(data, 2 * DOWN)), 
            TransformMatchingTex(stddev, MathTex (
                "\\sigma=", "\\sqrt{\\frac{0.41(1-0.41)}{22}}", "\\approx0.105"
            ).next_to(prop, DOWN))
        )
        self.wait(1)
        FadeOutAll(self)

class Test(Scene):
    def construct(self):
        statement = Text ("This will be a chi-square test for independence.", 
            font_size=24, 
            slant=ITALIC
        ).to_edge(UL)
        ec_label = Text ("Expected Counts", font_size=24).next_to(statement, DOWN).to_edge(LEFT) # > 100 cols
        expected_counts = MathTex ("\\frac{(\\textrm{Row Total})(\\textrm{Col Total})}{(\\textrm{Table Total})}").next_to(ec_label, DOWN).to_edge(LEFT) # > 100 cols
        self.play(Write(statement), Write(ec_label), Create(expected_counts))
        self.wait(1)
        # Could also have used a matrix here.
        expected_counts_table = DecimalTable (
            [
                [2.86364, 0.40909, 2.45455, 2.04545, 0.81818, 0.40909], 
                [4.13636, 0.59091, 3.54545, 2.95454, 1.18182, 0.59091]
            ], 
            row_labels=[Text ("Experience"), Text ("No Experience")], 
            col_labels=[Text (i) for i in [
                "Below 6th", "6th", "7th", "8th", "9th", "Above 9th"
            ]], 
            element_to_mobject_config={"num_decimal_places":5}
        ).scale(0.45).next_to(ec_label, DOWN).to_edge(LEFT)
        conditions = BulletedList (
            r"Random: No, the mailing list is not a random sample.", 
            r"10\%: $n\le\frac{1}{10}N \rightarrow 22<N$ \\(some respondants appear to be relatives)", # > 100 cols
            r"Large Counts: Expected Count$>5 \rightarrow$ Not satisfied.", 
            font_size=36
        ).next_to(expected_counts_table, DOWN).to_edge(LEFT)
        stats = VGroup(
            MathTex ("\\chi^2=4.42865"), 
            MathTex ("p\\textrm{-}val=0.48949").move_to(DOWN), 
            MathTex ("df=5").move_to(2 * DOWN), 
            MathTex ("\\alpha=0.10").move_to(3 * DOWN)
        ).next_to(conditions, RIGHT).shift(DOWN)
        self.play(
            Transform(expected_counts, expected_counts_table), 
            Write(conditions), 
            Create(stats)
        )
        self.wait(1)
        # Short on time. Can't get axis to scale right at the moment.
        # k = 5 # df
        # chi_sq_dist = FunctionGraph (
        #     lambda t: (np.power(t, k / 2 - 1) * np.power(np.e, -t / 2)) / (np.power(2, k / 2) * math.gamma(k / 2)), # > 100 cols
        #     x_range=[0, 25, 0.01], 
        #     color=RED
        # )
        # self.play(Create(chi_sq_dist))
        dist = ImageMobject ("chi_square_dist.png")
        self.play(FadeIn(dist))
        self.wait(1)
        FadeOutAll(self)

class Conclusion(Scene):
    def construct(self):
        title = Title ("Conclusion")
        self.play(Write(title))
        conclusion = Text ("""
Because the p-value (~0.49) is greater than the significance level (0.10), 
we fail to reject the null hypothesis.
There is no convincing evidence that there is an association between 
grade level and coding experience for intermediate school students 
similar to those in this study.
""", font_size=24)
        self.play(Write(conclusion))
