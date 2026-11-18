# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
An MCP server designed to give operational tools and AI clients bounded access to Kafka metadata. Its planned baseline provides topic discovery and consumer-lag context through authorization-aware adapters, structured responses and audit identifiers.

## Questions
- Local transport versus remote authenticated transport
- Tool granularity and context limits
- Authorization at tool boundary and backend identity

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
