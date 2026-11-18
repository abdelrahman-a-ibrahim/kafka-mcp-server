# Kafka MCP Server

A read-only MCP interface for Kafka metadata and consumer-lag investigation with scoped tool access.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

An MCP server designed to give operational tools and AI clients bounded access to Kafka metadata. Its planned baseline provides topic discovery and consumer-lag context through authorization-aware adapters, structured responses and audit identifiers.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Read-only topic discovery and consumer-lag tools.
- Principal-scoped authorization and metadata filtering.
- Bounded, paginated tool responses with structured errors.
- Timeout handling, audit identifiers and deterministic client verification.
- Optional AI client integration evaluated against known operational questions.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Deterministic client / optional model -> MCP server -> Kafka adapter
                                             |
                                      policy / audit / output bounds
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

MCP · Kafka · Python · Tool contracts · AI-assisted investigation.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/kafka-mcp-server.git
cd kafka-mcp-server
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/kafka_mcp_server/interfaces.py`](src/kafka_mcp_server/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Read-only tools cannot mutate broker state.
- Unauthorized topic details never appear in outputs or audit payloads.
- Responses are bounded, paginated and attributable to a tool request.
- A model failure cannot widen the adapter’s permissions.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/kafka_mcp_server/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://modelcontextprotocol.io/
- https://github.com/modelcontextprotocol/modelcontextprotocol/security
- https://kafka.apache.org/documentation/
