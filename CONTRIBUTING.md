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
