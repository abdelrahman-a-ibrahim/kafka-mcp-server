# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Request metadata for a topic outside the principal’s scope.
- Inject instructions into a topic description.
- Return thousands of topics from the adapter.
- Make Kafka unavailable midway through a multi-tool investigation.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Read-only tools cannot mutate broker state.
- Unauthorized topic details never appear in outputs or audit payloads.
- Responses are bounded, paginated and attributable to a tool request.
- A model failure cannot widen the adapter’s permissions.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
