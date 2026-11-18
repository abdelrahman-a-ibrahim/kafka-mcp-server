# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Read-only tools cannot mutate broker state.
- Unauthorized topic details never appear in outputs or audit payloads.
- Responses are bounded, paginated and attributable to a tool request.
- A model failure cannot widen the adapter’s permissions.

## Failure coverage
- Request metadata for a topic outside the principal’s scope.
- Inject instructions into a topic description.
- Return thousands of topics from the adapter.
- Make Kafka unavailable midway through a multi-tool investigation.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
