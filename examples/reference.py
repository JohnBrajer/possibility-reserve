"""Compact reference implementation of John Brajer's Possibility Reserve spine."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class Status(str, Enum):
    ACTIVE = "active"
    WATCH = "watch"
    DORMANT = "dormant"
    DEEP_DORMANT = "deep_dormant"
    REJECTED_CURRENT_MODEL = "rejected_current_model"
    DEAD_HARD_CONSTRAINT = "dead_hard_constraint"


@dataclass
class Possibility:
    id: str
    status: Status = Status.ACTIVE
    failure_conditions: Mapping[str, Any] = field(default_factory=dict)
    reactivation_conditions: Mapping[str, Any] = field(default_factory=dict)


def eligible_for_reactivation(possibility: Possibility, state: Mapping[str, Any]) -> bool:
    if possibility.status not in {
        Status.DORMANT,
        Status.DEEP_DORMANT,
        Status.REJECTED_CURRENT_MODEL,
    }:
        return False
    return bool(possibility.reactivation_conditions) and all(
        state.get(key) == expected
        for key, expected in possibility.reactivation_conditions.items()
    )


if __name__ == "__main__":
    p = Possibility(
        id="branch-a",
        status=Status.DORMANT,
        failure_conditions={"tool_available": False},
        reactivation_conditions={"tool_available": True},
    )
    print(eligible_for_reactivation(p, {"tool_available": True}))
