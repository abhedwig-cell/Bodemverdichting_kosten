# Colleague review session v0.1

**Status:** REVIEW_PLAN  
**Audience:** WENR/WUR project colleagues and invited domain reviewers  
**Purpose:** make the current Status-A-light architecture reviewable without asking colleagues to reverse-engineer the legacy workbook lineage.

## 1. Review objective

The first colleague review is not intended to approve a finished application or a fully quantified Tollebeek result.

The review question is whether the current scientific and data architecture is a defensible foundation for the next stage:

`theory → conceptual model → formal model → data model → implementation → evidence/qualification → generated artifact`

The desired outcome is a small set of explicit decisions and objections before the project proceeds to the first spatial source model and later to application development.

## 2. What reviewers receive beforehand

Send a compact review package rather than the full legacy workbook history.

Minimum pre-read:

1. `00_colleague_reader_guide.md`;
2. `18_status_a_light_checkpoint_v0_1.md`;
3. generated Tollebeek review workbook v0.2;
4. one link to the repository root for reviewers who want to inspect detail.

Optional, by reviewer role:

- soil/hydrology: `02_theoretical_framework.md`, `04_formal_model.md` and relevant theory/evidence rows;
- data/software: `05_data_model.md`, `06_implementation.md`, `17_formal_traceability_register_v0_1.md`;
- evidence/method review: `07_evidence_and_qualification.md`, `evidence/`, `15_traceability_matrix_v0_1.md`;
- Tollebeek/water-system expertise: `11_tollebeek_vertical_slice_v0_2.md`, `13_tollebeek_evidence_baseline_v0_1.md`.

## 3. What reviewers are explicitly not asked to do

The review should not become a line-by-line audit of old Excel tabs.

Reviewers are not asked to:

- validate every historical source in one meeting;
- approve current Tollebeek impact numbers, because those do not yet exist;
- choose convenience defaults for missing geometry, drainage, transfer or pump operation;
- judge user-interface design for an application that has not yet been built;
- interpret a software test PASS as proof of empirical physical validity.

## 4. Recommended participants

Aim for a small group with complementary roles rather than a large presentation audience.

Suggested roles:

- project lead / decision owner;
- soil physics / compaction expert;
- hydrology / SWAP modeller;
- water-system or drainage expert;
- economic / valuation colleague;
- data/software colleague;
- optional external domain reviewer for the pilot case.

A participant may cover more than one role.

## 5. Review questions

Ask reviewers to prepare comments under six questions.

### R1. Causal decomposition

Is the separation `soil state → response → attribution → transfer → valuation` scientifically appropriate, and are important pathways missing or incorrectly combined?

### R2. Counterfactual / reference state

Is the matched current/reference logic a defensible way to isolate effects attributable to compaction? Which reference-state choices require additional scientific rules?

### R3. Data-model semantics

Are the main entities, row grains, IDs and null semantics understandable and scientifically meaningful? Are there objects currently hidden inside one table that should be separate entities?

### R4. Evidence discipline

Is the separation between source, evidence item, project claim and qualification useful and sufficiently strict? Are any current claims stronger than their evidence allows?

### R5. Current data gates

Are the currently blocked inputs real scientific prerequisites, or are some unnecessarily strict? Are any important blockers missing?

### R6. Traceability / reproducibility

Can a reviewer move from a project claim to the formal equation, dataset, code, test and supporting evidence without having to infer hidden meaning?

## 6. Suggested 90-minute session

| Time | Topic | Output |
|---|---|---|
| 0–10 min | Why the project is being restructured | shared scope and review rules |
| 10–25 min | Causal and conceptual model | objections / missing pathways |
| 25–40 min | Current-reference attribution and formal model | decisions on scientific semantics |
| 40–55 min | Data model + workbook contract | entity/grain/field feedback |
| 55–70 min | Evidence/qualification + traceability | challenged claims and evidence gaps |
| 70–82 min | Tollebeek vertical slice and current data gates | confirm next empirical milestone |
| 82–90 min | Decision recap | agreed actions, owners and unresolved questions |

If there is less time, prioritise R1, R2, R4 and R5. Application/UI discussion should be deferred.

## 7. How to record review outcomes

Every substantive review point should end in one of four dispositions:

- `ACCEPT` — current architecture/claim is accepted for the present maturity level;
- `CHANGE` — architecture, documentation, schema or code needs a defined change;
- `EVIDENCE_REQUIRED` — no design change yet; additional evidence is needed;
- `OPEN_QUESTION` — disagreement or uncertainty remains and needs a separate decision surface.

Do not silently modify scientific meaning after the meeting. Record the disposition and then implement it through normal repository changes and review.

## 8. Minimal review record

For each substantive item capture:

```text
review_item_id
review_question
reviewer / role
comment
affected layer(s)
disposition
owner
next action
evidence or dependency
status
```

The review record itself can later become a canonical governance dataset if repeated review cycles justify it.

## 9. What counts as success for this review

The review is successful if colleagues can independently explain:

1. why the project separates state, response, attribution, transfer and valuation;
2. why current/reference is matched;
3. why Excel is an interface rather than the source of scientific meaning;
4. why a sourced number is not automatically an admitted parameter;
5. which Tollebeek capabilities are structurally ready and which remain data-gated;
6. what the next scientific milestone is.

Agreement on every detail is not required. Visible disagreement with an explicit next action is preferable to implicit agreement based on hidden assumptions.

## 10. Decision boundary after the review

Do not treat the session as permission to start full application development automatically.

The preferred next scientific milestone remains the first spatial source model with real current/reference inputs. Application development should proceed only where it can consume the same canonical schema and qualified datasets without inventing parallel meaning.

`REVIEW_SESSION_V0_1 = READY_FOR_USE`
