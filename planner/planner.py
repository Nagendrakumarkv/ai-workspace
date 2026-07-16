import logging

from planner.plan import Plan
from planner.step import PlanStep


class RuleBasedPlanner:
    """
    Creates a simple execution plan from a user goal.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

    def create_plan(self, goal: str) -> Plan:

        self.logger.info(
            f"Creating plan for goal: {goal}"
        )

        plan = Plan(goal=goal)

        plan.add_step(
            PlanStep(
                id=1,
                description="Understand the user's request"
            )
        )

        plan.add_step(
            PlanStep(
                id=2,
                description="Determine which tools or LLM are required"
            )
        )

        plan.add_step(
            PlanStep(
                id=3,
                description="Execute the required actions"
            )
        )

        plan.add_step(
            PlanStep(
                id=4,
                description="Generate the final response"
            )
        )

        self.logger.info(
            f"Plan created with {plan.total_steps()} steps."
        )

        return plan