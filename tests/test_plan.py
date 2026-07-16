from planner.plan import Plan
from planner.step import PlanStep


def test_plan():

    plan = Plan(goal="Demo")

    plan.add_step(
        PlanStep(
            id=1,
            description="Step 1"
        )
    )

    assert plan.total_steps() == 1