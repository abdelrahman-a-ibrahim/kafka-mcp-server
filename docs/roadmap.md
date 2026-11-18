# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Define tool input/output contracts, an allowlisted topic catalog and a threat model. Use synthetic descriptions that can contain hostile instructions.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Implement a deterministic Kafka adapter and authorization boundary; keep read-only metadata access as the baseline.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Implement the MCP server using a deliberately selected, pinned SDK/protocol version. Add pagination, timeouts, structured errors and audit identifiers.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Test allowed and denied principals, tool discovery, invalid inputs, huge metadata responses and backend outages with a deterministic client.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Optionally connect a model and evaluate tool selection against a fixed question set. Keep untrusted metadata separate from execution authority.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Documented remote authorization flow
- Schema/consumer metadata resource catalog
- Prompt-injection evaluation suite
- Explicitly approved sandbox-only mutation extension

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
