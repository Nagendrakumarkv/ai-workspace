from dataclasses import dataclass, field

from planner.step import PlanStep

from planner.step import StepStatus


@dataclass
class Plan:
    """
    Represents the complete execution plan.
    """

    goal: str

    steps: list[PlanStep] = field(default_factory=list)

    def add_step(self, step: PlanStep):

        self.steps.append(step)

    def completed_steps(self) -> int:

        return sum(
            step.status == StepStatus.COMPLETED
            for step in self.steps
        )

    def total_steps(self) -> int:

        return len(self.steps)