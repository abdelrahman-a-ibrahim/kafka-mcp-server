# Implementation backlog

Status: all milestones unstarted. Check a task only when its evidence exists.

## M1 — Design and contracts

Define tool input/output contracts, an allowlisted topic catalog and a threat model. Use synthetic descriptions that can contain hostile instructions.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M2 — Build the first path

Implement a deterministic Kafka adapter and authorization boundary; keep read-only metadata access as the baseline.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M3 — Integrate deliberately

Implement the MCP server using a deliberately selected, pinned SDK/protocol version. Add pagination, timeouts, structured errors and audit identifiers.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M4 — Handle failure

Test allowed and denied principals, tool discovery, invalid inputs, huge metadata responses and backend outages with a deterministic client.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M5 — Demonstrate and operate

Optionally connect a model and evaluate tool selection against a fixed question set. Keep untrusted metadata separate from execution authority.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

