from datetime import datetime, timedelta, timezone
from uuid import uuid4
from shared.approval import Approval


def test_matching_unexpired_approval():
    finding, proposal = uuid4(), uuid4()
    approval = Approval(finding, proposal, "reviewer", datetime.now(timezone.utc) + timedelta(minutes=5))
    assert approval.valid_for(finding, proposal)
    assert not approval.valid_for(finding, uuid4())


def test_expired_approval_is_denied():
    finding, proposal = uuid4(), uuid4()
    approval = Approval(finding, proposal, "reviewer", datetime.now(timezone.utc) - timedelta(seconds=1))
    assert not approval.valid_for(finding, proposal)


def test_naive_timestamps_cannot_authorize_write():
    finding, proposal = uuid4(), uuid4()
    approval = Approval(finding, proposal, "reviewer", datetime.now())
    assert not approval.valid_for(finding, proposal)


def test_blank_reviewer_cannot_authorize_write():
    finding, proposal = uuid4(), uuid4()
    approval = Approval(finding, proposal, "  ", datetime.now(timezone.utc) + timedelta(minutes=1))
    assert not approval.valid_for(finding, proposal)
