"""One-time approval token validation for sensitive patch operations."""

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True)
class Approval:
    finding_id: UUID
    proposal_id: UUID
    approved_by: str
    expires_at: datetime

    def valid_for(self, finding_id: UUID, proposal_id: UUID, now: datetime | None = None) -> bool:
        current = now or datetime.now(timezone.utc)
        if current.tzinfo is None or self.expires_at.tzinfo is None:
            return False
        return (bool(self.approved_by.strip()) and self.finding_id == finding_id
                and self.proposal_id == proposal_id and current < self.expires_at)
