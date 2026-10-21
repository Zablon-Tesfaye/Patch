"""Stable, collision-resistant GitHub branch names for fix proposals."""

from uuid import UUID


def fix_branch(finding_id: UUID, proposal_id: UUID) -> str:
    return f"patch/fix-{finding_id.hex[:12]}-{proposal_id.hex[:12]}"
