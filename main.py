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
for intermediate grade school students?""", font_size=24, slant=ITALIC), 
            BulletedList (
                r"$H_0$: There is $\bold{no}$ association between grade level and coding experience.", 
                r"$H_a$: There is $\bold{an}$ association between grade level and coding experience.", 
                font_size=36
            ).move_to(2 * DOWN), 
            Text ("(For intermediate grade school students.)", 
                font_size=16, slant=ITALIC).move_to(3.5 * DOWN)
        ).next_to(title, 2 * DOWN)
        self.play(Write(description))
        self.wait(1)
        FadeOutAll(self)
