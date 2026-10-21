"""Independent checks for whether a proposal may enter review."""

from shared.schema import FixProposal, Finding


def validate_proposal_binding(finding: Finding, proposal: FixProposal) -> None:
    if proposal.finding_id != finding.finding_id:
        raise ValueError("Proposal belongs to a different finding")
    if not proposal.patches:
        raise ValueError("Proposal contains no patch")
    for patch in proposal.patches:
        if patch.file != finding.file:
            raise ValueError("Patch target differs from verified finding")
        if not patch.search or finding.vulnerable_code.count(patch.search) != 1:
            raise ValueError("Patch is not anchored uniquely to verified vulnerable code")
