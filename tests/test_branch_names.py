from uuid import uuid4
from shared.branch_names import fix_branch


def test_proposal_specific_branch_names():
    finding = uuid4()
    assert fix_branch(finding, uuid4()) != fix_branch(finding, uuid4())
