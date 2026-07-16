import logging

from planner.plan import Plan
from planner.planner import RuleBasedPlanner


class PlannerService:
    """
    Entry point for creating execution plans.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.planner = RuleBasedPlanner()

    def create_plan(self, goal: str) -> Plan:

        self.logger.info(
            "PlannerService received a planning request."
        )

        plan = self.planner.create_plan(goal)

        self.logger.info(
            "PlannerService successfully created a plan."
        )

        return plan