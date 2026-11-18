"""Initial application boundary for Kafka MCP Server.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class KafkaOperations:
    def list_topics(self, principal: str, limit: int) -> list:
        """Return only authorized topic metadata with a bounded response."""
        raise NotImplementedError("Runtime implementation is in development.")

    def describe_lag(self, principal: str, group_id: str) -> dict:
        """Return lag context without consuming or exposing message payloads."""
        raise NotImplementedError("Runtime implementation is in development.")
