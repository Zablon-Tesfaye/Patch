from shared.audit import append_event, verify_chain


def test_audit_chain_detects_tampering():
    first = append_event("", {"action": "scan"})
    second = append_event(first["hash"], {"action": "approve"})
    assert verify_chain([first, second])
    second["event"]["action"] = "reject"
    assert not verify_chain([first, second])
