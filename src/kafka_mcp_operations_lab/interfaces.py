"""Proposed application boundary for Kafka MCP Operations Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class KafkaOperations:
    def list_topics(self, principal: str, limit: int) -> list:
        """Return only authorized topic metadata with a bounded response."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def describe_lag(self, principal: str, group_id: str) -> dict:
        """Return lag context without consuming or exposing message payloads."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

