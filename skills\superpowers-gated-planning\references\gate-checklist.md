# Gate Checklist

Use this checklist whenever `superpowers-gated-planning` is active. It exists to keep thinking, design, planning, and implementation in separate gates.

## Intent Gate

The request is gated when the user asks to:

- create or build a project, feature, app, skill, plugin, script, workflow, automation, document, or generated artifact;
- modify behavior or files;
- fix a bug;
- refactor code or docs;
- scaffold files or folders;
- install, update, remove, or configure dependencies;
- package deliverables;
- execute an implementation plan;
- make commits for implementation work.

The request is not gated when the user only asks for:

- a direct conceptual answer;
- a translation;
- a summary;
- an explanation of existing code;
- a status update;
- a non-mutating read-only inspection.

If uncertain, treat the request as gated. Ambiguous approval should stop and ask instead of moving forward.

## Brainstorm Gate

Passes only when the thread clearly identifies:

- the user's goal;
- intended scope;
- delivery shape;
- relevant constraints;
- success criteria;
- risks or boundaries that could affect the solution.

If missing, say:

> We are missing the brainstorming gate, so I will not start implementation yet. I will continue by clarifying the requirement one question at a time.

Then ask exactly one clarifying question and wait.

## Design Gate

Passes only when:

- 2-3 viable approaches were presented;
- trade-offs were explained;
- one approach was recommended;
- the user explicitly approved the design direction.

Baseline rationalization to reject: `按1选项` selects an approach only. It approves a design direction, not implementation. After the user chooses an option, continue to the Plan Gate.

If missing, say:

> We are missing the design approval gate, so I will not start implementation yet. I will present the viable approaches and ask you to approve the design direction first.

Then present approaches and wait for design approval.

## Plan Gate

Passes only when a concrete implementation plan exists and includes:

- exact files to create or modify;
- task-by-task steps;
- test or validation commands;
- expected validation output;
- delivery artifacts;
- commit points or commit boundaries, when commits are part of the work.

The plan is not implementation approval. Do not combine plan plus implementation for efficiency, speed, momentum, or convenience.

If missing, say:

> We are missing the implementation plan gate, so I will not start implementation yet. I will write the implementation plan first.

Then use the `writing-plans` workflow and stop before implementation.

## Execution Approval Gate

Passes only when the user explicitly approves implementation after reviewing the plan. Each gate needs separate explicit confirmation: design approval does not approve planning, and plan approval does not approve execution unless the user clearly says to begin implementation.

Examples that pass:

- `execute`
- `start implementation`
- `confirm, write code`
- `按计划实现`
- `确认动代码`
- `继续执行`

Examples that do not pass:

- `下一步`
- `next step`
- `go on`
- `continue`
- `looks good` when said before the implementation plan exists;
- `按1选项`
- choosing an option or design direction;
- vague interest without permission to touch files;
- questions about the plan.

Baseline rationalization to reject: `下一步` is not execution approval. It advances the conversation only.

Proactive autonomy never overrides a user planning or approval gate. If approval is ambiguous, stop and ask whether the user wants implementation to begin.

If missing, say:

> The plan is ready, but execution approval is still missing. I will wait for your explicit confirmation before touching implementation files.

Then ask for execution approval and wait.

## Implementation Actions

These actions count as implementation and require all gates to pass:

- creating source, test, documentation, config, or asset files;
- editing source, test, documentation, config, or asset files;
- deleting or moving project files;
- generating scaffolding;
- adding, removing, updating, or installing dependencies;
- changing configuration used by the final project;
- running commands that mutate project state;
- running formatters that write to project files;
- writing tests that will become part of the project;
- packaging final deliverables;
- committing implementation work.

Harmless edits, tests, scaffolding, config changes, dependency changes, and commits are implementation. "Just a quick test", "just a placeholder", "just a config tweak", and "just a harmless commit" are not exceptions.

These actions are allowed before execution approval:

- reading files;
- inspecting directories;
- checking git status;
- reading documentation;
- writing design documents;
- writing implementation plans;
- asking questions;
- summarizing trade-offs.

## Recovery Rule

When a gate fails, recover into the missing gate. Do not skip ahead. Do not implement "just a small part." Do not create placeholder implementation files. Do not package or commit implementation work early.

If the user attempts to skip gates, name the missing gate briefly and resume there. If the user gives ambiguous approval, stop and ask for explicit confirmation instead of inferring permission.
