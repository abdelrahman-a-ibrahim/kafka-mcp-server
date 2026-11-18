# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
An MCP server designed to give operational tools and AI clients bounded access to Kafka metadata. Its planned baseline provides topic discovery and consumer-lag context through authorization-aware adapters, structured responses and audit identifiers.

## Component view
```text
Deterministic client / optional model -> MCP server -> Kafka adapter
                                             |
                                      policy / audit / output bounds
```

## Design decisions
- Local transport versus remote authenticated transport
- Tool granularity and context limits
- Authorization at tool boundary and backend identity

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/kafka_mcp_server/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
