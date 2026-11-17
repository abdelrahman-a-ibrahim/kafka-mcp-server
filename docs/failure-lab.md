# Failure lab

These are planned experiments, not observed results. Begin with disposable local fixtures. For each experiment establish a baseline, inject one fault, record timestamps, verify invariants and perform cleanup.

## Project-specific experiments
1. Request metadata for a topic outside the principal’s scope.
2. Inject instructions into a topic description.
3. Return thousands of topics from the adapter.
4. Make Kafka unavailable midway through a multi-tool investigation.

## Experiment record
Copy this block for each run:

- Experiment / commit:
- Date, platform and tool versions:
- Input dataset and deterministic seed where applicable:
- Expected invariant:
- Hypothesis:
- Exact fault and injection command:
- Start/end timestamps:
- Observed behavior and raw output location:
- Lost/duplicate/rejected operations, if applicable:
- Recovery steps and elapsed time:
- Pass/fail against the stated invariant:
- Environment limits / what this does not prove:
- Residual resources and cleanup result:

## Stop conditions
Stop when the fault escapes the disposable boundary, the evidence cannot identify the affected resources, or the planned resource/cost allowance is exceeded. Do not conduct these experiments on shared production systems.
