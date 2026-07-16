import logging

from planner.executor import PlanExecutor
from planner.plan import Plan
from planner.service import PlannerService


class AgentService:
    """
    Coordinates planning and execution.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.planner = PlannerService()

        self.executor = PlanExecutor()

    def create_execution_plan(
        self,
        goal: str,
    ) -> Plan:

        self.logger.info(
            "Creating execution plan."
        )

        plan = self.planner.create_plan(goal)

        return self.executor.execute(plan)