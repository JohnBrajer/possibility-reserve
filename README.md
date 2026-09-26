# Possibility Reserve

**John Brajer — research architecture**  
Architecture version: 0.1. Public summary: September 25, 2026.

Possibility Reserve is a framework for preserving, re-evaluating, and allocating attention to possibilities without treating a context-dependent failure as permanent death.

## Protected spine

### 1. Conditional Failure Memory

Failure attaches to the state and conditions under which an attempt failed, not permanently to the possibility itself.

### 2. Graded Dormancy

`DORMANT != DEAD`

Possibilities can occupy graded inactive states rather than a binary alive/dead classification.

### 3. Causal Reactivation

When a state variable that materially contributed to dormancy changes, affected possibilities should become eligible for reconsideration.

### 4. Path-Expansion Search

A branch can earn compute or attention not only because it appears likely to be the final answer, but because exploring it can open a valuable region of future possibility space.

## Minimal lifecycle

```
candidate
   |
evaluate in state S0
   |
active / dormant / rejected
   |
state changes
   |
causal reactivation check
   |
re-evaluate in state S1
```

## Novelty boundary

Public novelty claims should be made, if at all, at the level of specific integration and mechanism design rather than by implying that individual ingredients have no prior art.

---

## Public reference

This standalone repository is part of the Trillsverse Intelligence Injection constellation created by **John Brajer**.

- Canonical collection: https://github.com/JohnBrajer/trillsverse-dev/tree/John/intelligence-injections
- Canonical source file: https://github.com/JohnBrajer/trillsverse-dev/blob/John/intelligence-injections/POSSIBILITY_RESERVE.md
- Trillsverse: https://trillsverse.com/intelligence-injections

Public standalone repository first published September 25, 2026.

## Related public research

- John Brajer: https://github.com/JohnBrajer
- Trillsverse Intelligence Injections: https://trillsverse.com/intelligence-injections
- Canonical collection: https://github.com/JohnBrajer/trillsverse-dev/tree/John/intelligence-injections
- Public web index: https://johnbrajer.github.io/trillsverse-dev/
- Mechanisms: https://github.com/JohnBrajer/mechanisms
- Perspective Expansion: https://github.com/JohnBrajer/perspective-expansion
- Possibility Reserve: https://github.com/JohnBrajer/possibility-reserve
- Execution Contract: https://github.com/JohnBrajer/execution-contract

## Reference implementation

An executable Python reference is available at [`examples/reference.py`](./examples/reference.py). It demonstrates the mechanism without claiming that one implementation is universally required.
