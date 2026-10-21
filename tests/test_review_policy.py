import json
from pathlib import Path
import pytest
from shared.schema import Finding, FixProposal
from shared.review_policy import validate_proposal_binding


def test_rejects_mismatched_finding():
    base = Path(__file__).parent / "fixtures"
    finding = Finding.model_validate_json((base / "example_sql_injection_finding.json").read_text())
    proposal = FixProposal.model_validate_json((base / "example_fix_proposal.json").read_text())
    if proposal.finding_id != finding.finding_id:
        with pytest.raises(ValueError, match="different finding"):
            validate_proposal_binding(finding, proposal)
