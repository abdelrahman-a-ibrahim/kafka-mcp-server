# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
An MCP server designed to give operational tools and AI clients bounded access to Kafka metadata. Its planned baseline provides topic discovery and consumer-lag context through authorization-aware adapters, structured responses and audit identifiers.

## Target capabilities
- Define tool input/output contracts, an allowlisted topic catalog and a threat model. Use synthetic descriptions that can contain hostile instructions.
- Implement a deterministic Kafka adapter and authorization boundary; keep read-only metadata access as the baseline.
- Implement the MCP server using a deliberately selected, pinned SDK/protocol version. Add pagination, timeouts, structured errors and audit identifiers.
- Test allowed and denied principals, tool discovery, invalid inputs, huge metadata responses and backend outages with a deterministic client.
- Optionally connect a model and evaluate tool selection against a fixed question set. Keep untrusted metadata separate from execution authority.

## Acceptance criteria
- Read-only tools cannot mutate broker state.
- Unauthorized topic details never appear in outputs or audit payloads.
- Responses are bounded, paginated and attributable to a tool request.
- A model failure cannot widen the adapter’s permissions.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
