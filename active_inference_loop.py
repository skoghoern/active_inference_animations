# run with: manim -pql active_inference_loop.py ActiveInferenceLoop
from manim import *

class ActiveInferenceLoop(Scene):
    def construct(self):
        agent_box_start = RoundedRectangle(corner_radius=0.5,
            stroke_color=WHITE,
            height = 4,
            width = 4,
        ).shift(LEFT * 2.5)
        agent_label_start = Text("agent", font_size=24).next_to(agent_box_start, UP)

        env_box_start = RoundedRectangle(corner_radius=0.5,
            stroke_color=WHITE,
            height = 4,
            width = 4,
        ).shift(RIGHT * 2.5)
        env_label_start = Text("environment", font_size=24).next_to(env_box_start, UP)

        # Add avatar and globe icons
        avatar = SVGMobject("public/avatar.svg").move_to(agent_box_start) # Replace path/to/avatar.svg
        globe = SVGMobject("public/world_globe.svg").move_to(env_box_start) # Replace path/to/globe.svg

        # Add curved arrows
        arrow_bottom = ArcBetweenPoints(
            start=env_box_start.get_bottom(),
            end=agent_box_start.get_bottom(),
            angle=-TAU / 4,
            color=BLUE
        ).add_tip()  # Add arrow tip
        arrow_top = ArcBetweenPoints(
            start=agent_box_start.get_top(),
            end=env_box_start.get_top(),
            angle=-TAU / 4,
            color=BLUE
        ).add_tip() # Add arrow tip

        # Create the main containers (agent and environment)
        agent_box = RoundedRectangle(
            corner_radius=0.5,
            stroke_color=WHITE,
            height = 6,
            width = 7,
        ).shift(LEFT * 2)
        agent_label = Text("agent", font_size=24).next_to(agent_box, UP)

        env_box = RoundedRectangle(
            corner_radius=0.5,
            height=6,
            width=4,
            stroke_color=WHITE
        ).next_to(agent_box, RIGHT, buff=0)
        env_label = Text("environment", font_size=24).next_to(env_box, UP)

        # Create nodes within the agent
        preferred_states = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,UP+ LEFT).shift(0.5*(DOWN+RIGHT))
        preferred_states_text = Text("preferred\nstates", font_size=16).move_to(preferred_states)

        efe_calc = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,UP+ LEFT).shift(1.5*DOWN+2*RIGHT)
        efe_calc_text = Text("EFE\ncalculation", font_size=16).move_to(efe_calc)

        sample_action = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,UP+ LEFT).shift(1.5*DOWN+4*RIGHT)
        sample_action_text = Text("sample\naction", font_size=16).move_to(sample_action)

        predicted_state = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,RIGHT).shift(0.5*LEFT+DOWN * 0.5)
        predicted_state_text = Text("predicted\nstate", font_size=16).move_to(predicted_state)

        updated_beliefs = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,UP+ LEFT).shift(3*DOWN+0.5*RIGHT)
        updated_beliefs_text = Text("updated\nbeliefs", font_size=16).move_to(updated_beliefs)

        vfe_calc = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,DOWN+LEFT).shift(0.5*UP+3*RIGHT)
        vfe_calc_text = Text("VFE\ncalculation", font_size=16).move_to(vfe_calc)

        # Create nodes at the border
        action_node = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,UP+ RIGHT).shift(1.5*DOWN+RIGHT).set_fill(BLACK, opacity=1.0)
        action_text = Text("action", font_size=16).move_to(action_node)

        observations = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(agent_box,DOWN + RIGHT).shift(.5*UP+RIGHT).set_fill(BLACK, opacity=1.0)
        observations_text = Text("observations", font_size=16).move_to(observations)

        # Create node in environment
        hidden_states = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=1.6,
            stroke_color=GRAY
        ).align_to(env_box, RIGHT).shift(0.5*LEFT+0.5*DOWN)
        hidden_states_text = Text("hidden states", font_size=16).move_to(hidden_states)

        # Create arrows
        arrows = VGroup(
            Arrow(hidden_states.get_bottom(), observations.get_right(), color=BLUE),
            Arrow(observations.get_left(), vfe_calc.get_right(), color=BLUE),
            Arrow(vfe_calc.get_left(), updated_beliefs.get_bottom(), color=BLUE),
            Arrow(updated_beliefs.get_top(), efe_calc.get_left(), color=BLUE),
            Arrow(preferred_states.get_bottom(), efe_calc.get_left(), color=BLUE),
            Arrow(efe_calc.get_right(), sample_action.get_left(), color=BLUE),
            Arrow(sample_action.get_right(), action_node.get_left(), color=BLUE),
            Arrow(sample_action.get_right(), predicted_state.get_top(), color=BLUE),
            Arrow(action_node.get_right(), hidden_states.get_top(), color=BLUE),
            Arrow(predicted_state.get_bottom(), vfe_calc.get_right(), color=BLUE)
        )

        # Add D arrow
        d_arrow = Arrow(
            start=predicted_state.get_left()+LEFT,
            end=predicted_state.get_left(),
            color=BLUE,
            buff=0.1
        )
        d_label = Text("D", font_size=24).next_to(d_arrow, UP, buff=0.1)


        # Create the animation sequence sequentially
        self.play(
            Create(env_box_start),
            Write(env_label_start),
            Create(globe)
        )
        self.play(
            Create(arrow_bottom),
        )
        self.play(
            Create(agent_box_start),
            Write(agent_label_start),
            Create(avatar)
        )
        self.play(
            Create(arrow_top)
        )


        self.wait(3)
        self.play(Transform(agent_box_start, agent_box),
                  Transform(env_box_start, env_box),
                  Transform(agent_label_start, agent_label),
                  Transform(env_label_start, env_label),
                  Uncreate(avatar), # Remove avatar
                  Uncreate(globe),  # Remove globe
                  Uncreate(arrow_top), # Remove top arrow
                  Uncreate(arrow_bottom)) # Remove bottom arrow
        self.wait(3)
        # # Create the animation sequence
        # self.play(
        #     Create(agent_box),
        #     Create(env_box),
        #     Write(agent_label),
        #     Write(env_label)
        # )

        # Add all nodes
        nodes = VGroup(
            hidden_states, hidden_states_text,
            observations, observations_text,
            vfe_calc, vfe_calc_text,
            updated_beliefs, updated_beliefs_text,
            preferred_states, preferred_states_text,
            efe_calc, efe_calc_text,
            sample_action, sample_action_text,
            predicted_state, predicted_state_text,
            action_node, action_text            
        )
        # self.play(Create(nodes)) # Replaced with stepwise animation

        # Add arrows and D label
        # self.play(
        #     Create(arrows),
        #     Create(d_arrow),
        #     Write(d_label)
        # ) # Replaced with stepwise animation

        # Stepwise animation of the active inference loop
        self.play(Create(hidden_states), Write(hidden_states_text))
        self.play(Create(arrows[0]))
        self.play(Create(observations), Write(observations_text))
        self.play(Create(arrows[1]))
        self.play(Create(vfe_calc), Write(vfe_calc_text))
        self.play(Create(arrows[2]))
        self.play(Create(updated_beliefs), Write(updated_beliefs_text))
        self.play(Create(arrows[3]))
        self.play(Create(preferred_states), Write(preferred_states_text))
        self.play(Create(arrows[4]))
        self.play(Create(efe_calc), Write(efe_calc_text))
        self.play(Create(arrows[5]))
        self.play(Create(sample_action), Write(sample_action_text))
        self.play(Create(arrows[6]))
        self.play(Create(action_node), Write(action_text))
        self.play(Create(arrows[8]))
        self.play(Create(arrows[7]))
        self.play(Create(predicted_state), Write(predicted_state_text))
        self.play(Create(d_arrow), Write(d_label))
        self.play(Create(arrows[9]))

        # Final pause
        self.wait(5) 