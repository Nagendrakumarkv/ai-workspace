import logging

from planner.plan import Plan
from planner.step import StepStatus


class PlanExecutor:
    """
    Executes a plan step by step.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def execute(self, plan: Plan):
        self.logger.info("Starting plan execution.")

        for step in plan.steps:
            self.logger.info(f"Executing Step {step.id}")

            step.status = StepStatus.RUNNING

            try:
                step.result = (
                    f"Successfully executed: {step.description}"
                )

                step.status = StepStatus.COMPLETED

                self.logger.info(
                    f"Step {step.id} completed."
                )

            except Exception as error:
                step.result = str(error)

                step.status = StepStatus.FAILED

                self.logger.exception(error)

        self.logger.info("Plan execution completed.")

        return plan