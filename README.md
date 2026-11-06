# university-face-id

Face-based identification and attendance system for a university campus.

> **Status: pre-alpha — scaffolding only.** No application code exists yet.
> The technology stack and the face-recognition strategy are still open decisions.
> See [`docs/architecture.md`](docs/architecture.md) and the ADRs in [`docs/decisions/`](docs/decisions/).

## What it is

A system that recognises enrolled people (students, staff, visitors) from a camera
frame and records the resulting event: attendance for a class, entry to a building,
or a check-in at a terminal.

Two distinct problems, which are easy to confuse:

| Problem | Question | Typical use |
| --- | --- | --- |
| **Verification** (1:1) | "Is this person who they claim to be?" | ID card + face check at an exam |
| **Identification** (1:N) | "Who is this?" | Walk-through attendance, turnstile |

Identification is the harder one: accuracy degrades as the enrolled population grows,
and it has stronger privacy implications. The architecture must state which one each
screen and endpoint is doing.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — proposed system architecture, components, open decisions
- [`docs/data-model.md`](docs/data-model.md) — draft domain entities and relationships
- [`docs/decisions/`](docs/decisions/) — Architecture Decision Records (proposed / accepted / rejected)

## Repository layout (target)

```
university-face-id/
├── docs/          # architecture, data model, ADRs
├── apps/
│   ├── web/       # admin + kiosk UI          (not created yet)
│   └── api/       # application backend      (not created yet)
├── packages/      # shared types / config    (not created yet)
└── infra/         # docker compose, deploy   (not created yet)
```

Folders are created only once the corresponding decision is accepted. Committing empty
placeholder trees makes the structure look decided when it is not.

## Contributing

Nothing to build yet. Read the open decisions first, then propose a change as a new ADR
rather than picking a stack in code.

## License

MIT — see [`LICENSE`](LICENSE).
