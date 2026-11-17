# Kafka MCP Operations Lab

**Bounded operational context for AI tools**

> Status: foundation only / implementation not started. Independent educational project by Abdelrahman Ahmed. This repository is not a reconstruction of employer systems, a production deployment or proof of completed work.

## The engineering challenge

Expose synthetic Kafka metadata and consumer-lag summaries through an MCP server. Begin with read-only tools and a deterministic client. Add model integration only after validating permissions, bounded outputs and failure handling.

This is a capstone for an experienced engineer. The goal is to defend tradeoffs, investigate failure and produce reproducible evidence, not just get a happy-path demo running.

**Technical focus:** MCP · Kafka · Python · Tool contracts · AI-assisted investigation.

## What exists in this first commit

- A project-specific architecture brief and decision questions.
- Five implementation milestones with explicit review gates.
- Failure experiments and acceptance criteria.
- Typed Python interface scaffolds. Methods deliberately raise `NotImplementedError`.
- One synthetic scenario fixture; it is an input, not a successful output or benchmark.
- Evidence and journal templates, an issue template, and syntax/JSON foundation checks.

## What you will build

1. Define tool input/output contracts, an allowlisted topic catalog and a threat model. Use synthetic descriptions that can contain hostile instructions.
2. Implement a deterministic Kafka adapter and authorization boundary; keep read-only metadata access as the baseline.
3. Implement the MCP server using a deliberately selected, pinned SDK/protocol version. Add pagination, timeouts, structured errors and audit identifiers.
4. Test allowed and denied principals, tool discovery, invalid inputs, huge metadata responses and backend outages with a deterministic client.
5. Optionally connect a model and evaluate tool selection against a fixed question set. Keep untrusted metadata separate from execution authority.

## Start here

1. Read [the architecture brief](docs/architecture.md) and record the first decision in [ADR 0001](docs/adr/0001-system-boundaries.md).
2. Inspect [the synthetic scenario](examples/scenario.json) and [the interface boundary](src/kafka_mcp_operations_lab/interfaces.py).
3. Run the foundation checks from the repository root:

   ```sh
   python3 tools/check_foundation.py
   ```

   Python 3.9+ is sufficient for these standard-library checks. They parse Python and JSON; they do **not** validate runtime behavior, deployment safety, protocol compliance or completion.
4. Create a feature branch, implement milestone 1 and add behavior tests before adapters.
5. Follow [the milestone backlog](docs/milestones.md). Select and pin implementation dependencies when you introduce them; none are installed by this scaffold.
6. Complete [the failure lab](docs/failure-lab.md), gather [evidence](docs/evidence/README.md) and review [acceptance criteria](docs/acceptance.md).

There is deliberately no `deploy`, `apply`, paid API call, installed cloud SDK or working runtime in this initial commit.

## Architecture at a glance

```text
Deterministic client / optional model -> MCP server -> Kafka adapter
                                             |
                                      policy / audit / output bounds
```

This is a proposed lab architecture. [The design brief](docs/architecture.md) identifies decisions still to make.

## Learning prerequisites

- `kafka-messaging-platform-lab` (a suggested learning prerequisite; no runtime dependency is wired in)

Repositories are separate and can evolve independently. If you connect them later, exchange versioned fixtures or contracts; do not rely on sibling-relative imports. You can implement a standalone synthetic adapter first.

## What makes this substantial

- Local transport versus remote authenticated transport
- Tool granularity and context limits
- Authorization at tool boundary and backend identity

You must explain what happens on retries, partial failure, concurrent operations and recovery. Record what your test environment cannot prove. No result is accepted simply because a dashboard is green.

## Definition of done

- Read-only tools cannot mutate broker state.
- Unauthorized topic details never appear in outputs or audit payloads.
- Responses are bounded, paginated and attributable to a tool request.
- A model failure cannot widen the adapter’s permissions.

Also supply installation/reproduction instructions, dependency versions, meaningful behavior tests, cleanup instructions, an architecture decision log and evidence from a repeatable demonstration. A checklist or syntax check alone does not satisfy completion.

## Advanced extensions

- Documented remote authorization flow
- Schema/consumer metadata resource catalog
- Prompt-injection evaluation suite
- Explicitly approved sandbox-only mutation experiment

Extensions follow a working baseline; they are not requirements for the first milestone.

## Boundaries and costs

Use fictional services, synthetic inputs and a disposable sandbox. Do not copy employer repositories, runbooks, tickets, customer data, credentials or internal architecture. Real cloud/provider adapters are future work and may incur costs; [the operations plan](docs/operations.md) must identify account, region, budget, resource inventory and teardown before deployment. Budget alerts notify; they do not constitute a hard spending cap.

## Publishable evidence, when earned

A completed lab may support a portfolio case study labeled **independent project**. Share your original code, sanitized diagrams, measured results and a failure/recovery write-up. Employer experience and personal lab evidence remain separate. Never copy illustrative fixture values into a results claim.

## Primary references

- https://modelcontextprotocol.io/
- https://github.com/modelcontextprotocol/modelcontextprotocol/security
- https://kafka.apache.org/documentation/

Read current official documentation when selecting SDKs, images, tool versions and integrations. The scaffold intentionally does not guess compatible version combinations.

## Repository map

- `src/kafka_mcp_operations_lab/interfaces.py`
- `examples/scenario.json`
- `docs/architecture.md`
- `docs/milestones.md`
- `docs/failure-lab.md`
- `docs/acceptance.md`
- `docs/learning-journal.md`
- `docs/evidence/README.md`
- `docs/operations.md` — local/cloud boundaries and teardown plan.
- `docs/adr/` — decisions and alternatives.
- `tools/check_foundation.py` — syntax and fixture integrity only.

## Working agreement

Keep commits focused: `docs`, `feat`, `test`, `fix`, `ops`. Work on a feature branch and merge only after the milestone review. Consult [CONTRIBUTING.md](CONTRIBUTING.md). No open-source license has been chosen yet; see [NOTICE.md](NOTICE.md).
