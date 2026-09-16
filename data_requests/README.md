# Data requests

This directory stores canonical requests for missing inputs, derivations, model configurations and scientific decisions that block or constrain project capabilities.

`data_request_register.csv` is a governance/readiness register. It is not a table of scientific input values.

For each request it records:

- what prerequisite is needed;
- which capability it constrains;
- whether the prerequisite is external data, a derived input, a scientific decision or model configuration;
- current readiness status;
- already relevant evidence and claims;
- minimum acceptance criteria;
- the blocking reason and next bounded action.

A request with `PARTIAL_EVIDENCE` means that useful context or method evidence exists, but the required project input itself is not yet admitted. `MISSING` means the canonical project state does not yet contain enough linked material to treat the prerequisite as partially ready.

Blank evidence or claim links remain blank. They are never interpreted as zero, absence of relevance, or automatic permission to invent a value.

The current v0.1 register is deliberately bounded to the first matched CURRENT/REFERENCE source-model experiment. Transfer, pump dispatch and cost inputs remain separate later-stage gates.
