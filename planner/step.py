from dataclasses import dataclass, field
from enum import Enum


class StepStatus(Enum):
    """
    Represents the current state of a plan step.
    """

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class PlanStep:
    """
    Represents one step inside a plan.
    """

    id: int

    description: str

    status: StepStatus = StepStatus.PENDING

    tool: str | None = None

    result: str | None = None