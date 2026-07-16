from planner.service import PlannerService


def test_planner_service():

    service = PlannerService()

    plan = service.create_plan("Hello")

    assert plan.goal == "Hello"

    assert plan.total_steps() == 4