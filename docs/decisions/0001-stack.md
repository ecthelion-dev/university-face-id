# ADR 0001 — Application stack

- **Status:** proposed
- **Date:** 2026-11-06
- **Deciders:** project owner
- **Affects:** whole repository

## Context

The system needs a web UI, an API, a database, and — the part that constrains everything
else — a face-recognition pipeline. Inference is Python-native in practice: the mature
off-the-shelf libraries (InsightFace, dlib, ONNX Runtime wrappers) are Python. Meanwhile
the fastest UI development path is JavaScript/TypeScript.

Three shapes are on the table. They differ mainly in **how many runtimes** the team must
operate, not in feature capability.

## Options considered

### Option A — Next.js + FastAPI + PostgreSQL *(recommended)*
Two runtimes: TypeScript for UI, Python for API/recognition.

- Pros: inference runs in the API's own runtime, no cross-process hop for embeddings;
  FastAPI gives typed request/response models and auto-generated OpenAPI; strong library
  ecosystem for CV; clear separation lets the recognition service scale independently.
- Cons: two dependency trees, two deployment units, an API contract to keep in sync;
  more moving parts for one developer.
- Cost: highest initial setup, lowest long-term friction for ML work.

### Option B — Next.js full-stack + PostgreSQL
One runtime: UI, API routes, Prisma.

- Pros: single deploy, single language, fastest to prototype, great DX.
- Cons: face recognition cannot reasonably run in Node against the mature Python
  libraries — it becomes a separate Python service anyway, so this defers rather than
  avoids Option A. Serverless-ish request limits also fight long inference calls.
- Cost: lowest start, high rework risk once recognition lands.

### Option C — Laravel + MySQL
PHP monolith, optional Python sidecar for inference.

- Pros: batteries-included conventions, familiar if the team is PHP-first; good admin
  scaffolding (Filament) for the registrar/back-office screens.
- Cons: the core capability (face matching) sits entirely outside the framework, so the
  "batteries" don't help where it matters; vector search in MySQL is weaker than pgvector.
- Cost: medium, with a permanent language boundary for the most important feature.

## Decision

**Not yet decided.** Option A is the recommendation, but the choice should be confirmed by
the person writing the code, because operational familiarity dominates on a small team.

Deciding factors to weigh:
1. Is the team Python-comfortable, or TS-only?
2. Will inference be hosted (API) or self-run? Self-run strongly favours A.
3. Is a vector database needed at all, or is the enrolled population small enough for
   exact search in a single Postgres query?

## Consequences

Whichever is chosen, these hold:

- **Positive:** recognition stays isolated behind an internal interface, so the provider
  can change without touching the UI.
- **Negative:** picking B is expected to add a Python service later; that is not a failure,
  but it should be anticipated rather than discovered.
- **Follow-up:** once accepted, rename this file's status and scaffold `apps/*` accordingly.
- **Revisit if:** the project becomes multi-tenant with independent deployments, or
  inference moves to a vendor API (which would remove the Python requirement entirely).

## Validation

The choice is validated when a vertical slice exists: enrol a face, store an embedding,
run a 1:1 verification from the UI, and observe end-to-end latency. If that slice can be
built in under a week in the chosen stack, the decision holds.
