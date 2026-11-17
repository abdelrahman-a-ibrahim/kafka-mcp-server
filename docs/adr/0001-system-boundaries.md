# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Expose synthetic Kafka metadata and consumer-lag summaries through an MCP server. Begin with read-only tools and a deterministic client. Add model integration only after validating permissions, bounded outputs and failure handling.

## Decision questions
- Local transport versus remote authenticated transport
- Tool granularity and context limits
- Authorization at tool boundary and backend identity

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
