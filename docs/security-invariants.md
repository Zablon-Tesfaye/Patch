# Security invariants

1. A proposed replacement must match exactly one source span.
2. A replacement must make a non-empty change.
3. A target must resolve to a regular file under the intended repository root, not through a symlink escape.
4. Developer approval is required before a write or pull request.
5. The generated patch must be reviewed; LLM-generated code is not automatically trusted.
6. Live model-provider tests are separate from deterministic CI tests.

These preflight utilities are intended for integration into the full approval-to-commit pipeline. Their presence alone does not prove the complete GitHub write path is protected.
