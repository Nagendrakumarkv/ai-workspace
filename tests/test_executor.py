from planner.executor import PlanExecutor
from planner.planner import RuleBasedPlanner
from planner.step import StepStatus


def test_executor():

    planner = RuleBasedPlanner()

    executor = PlanExecutor()

    plan = planner.create_plan("Demo")

    executor.execute(plan)

    for step in plan.steps:

        assert step.status == StepStatus.COMPLETED