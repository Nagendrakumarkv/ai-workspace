from planner.planner import RuleBasedPlanner


def test_create_plan():

    planner = RuleBasedPlanner()

    plan = planner.create_plan("Demo Goal")

    assert plan.goal == "Demo Goal"

    assert plan.total_steps() == 4

    assert plan.steps[0].description == "Understand the user's request"