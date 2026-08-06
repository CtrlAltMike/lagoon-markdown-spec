# Contributing

Changes should keep the written specification, JSON Schema, examples, and
shipping Lagoon behavior aligned.

For a normative change:

1. Explain the interoperability problem it solves.
2. State whether existing v1 readers can safely ignore the change.
3. Update the specification and schema together.
4. Add or update a minimal example.
5. Verify the result against the current Lagoon reader and writer.

Editorial clarifications that do not change conformance may remain in version
1. Changes to required paths, validation rules, or field meanings require a
new integer format version.

## Agentic contributions

Contributions created or assisted by AI agents are welcome and are evaluated
under the same technical standards as human-authored contributions.

The submitting human remains responsible for:

- verifying technical accuracy and interoperability claims;
- validating examples, schemas, and generated artifacts;
- ensuring the contribution's provenance and license permit its submission;
- disclosing material agent assistance in the pull-request description; and
- responding to review feedback and correcting defects.

An agent's output is supporting work, not evidence by itself. Normative changes
must still cite reproducible behavior, published standards, or testable
implementations as appropriate.
