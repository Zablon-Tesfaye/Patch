from shared.redaction import redact


def test_redacts_authorization_header():
    assert "abc123" not in redact("Authorization: Bearer abc123")


def test_redacts_token_assignment():
    assert "secretvalue" not in redact("token=secretvalue")
