# NeetCode 500 Bilingual Recall Dashboard Design

**Status:** Revised design, pending user review
**Decision date:** 2026-08-06
**Primary plan:** `/Users/devan/Desktop/neetcode_500_bilingual_master_plan_2026-08-06_v2.0.md`
**Product mode:** Local-first, single user, Python 3.12+, Asia/Seoul
**Readable HTML:** `docs/superpowers/specs/2026-08-06-neetcode-500-dashboard-design.html`

## 1. Product goal

Build a local HTML study application that selects and freezes 500 problems from NeetCode All, teaches them first in Korean and then in English, executes the user's Python solutions, records spoken reasoning and meaningful practice actions, uses Codex CLI for bounded coaching and evidence-based post-submission review, and teaches every answer through a qualified click-by-click animation.

The application operationalizes the master plan rather than replacing it. The one-year gates remain:

- `B_CERTIFIED = 500`
- `C_CERTIFIED = 120`
- `REVIEW_DEBT = 0`
- `NEW_PROBLEM_DEFICIT = 0`
- `RED_QUEUE = 0`
- 100 unseen attempts, 12 live mocks, eight OAs, and three long-form tests tracked separately

The application may certify that the defined process was completed. It must not claim that completing the process guarantees employment or guarantees memory retention for every person.

## 2. Approved decisions

The following decisions are frozen for implementation planning:

1. Include both Free and Pro problems because the user has a NeetCode Pro account.
2. Use global interview frequency, not a single target company, as the largest ranking factor.
3. Preserve the master plan's exact difficulty target: 100 Easy, 320 Medium, and 80 Hard.
4. Use a T-shaped curriculum: broad coverage across all required patterns, with P001–P080 forming an Array Systems concentration.
5. Keep unselected array-family problems in an `Array Depth Queue` for the next curriculum version.
6. Use an HTML interface with a local Python backend and SQLite, not Streamlit.
7. Use the approved Midnight Focus visual direction and the focused split practice layout.
8. Use Codex CLI through `codex exec`; do not require an OpenAI API key for normal local review.
9. Count nine learning encounters per problem: three coached encounters followed by six blind encounters.
10. Use Korean first, then English, with English-only Final B.
11. Support spoken explanations through browser recording and local transcription.
12. Use local `whisper.cpp` with a multilingual `small` model by default.
13. Add D365 maintenance outside the first-year 1,292-hour budget to test one-year retention.
14. Record every meaningful practice action in an append-only interaction ledger that can reconstruct the attempt without storing noisy pointer movement.
15. Grade primarily inside this application: deterministic local tests are the correctness oracle, and Codex evaluates the locked reasoning evidence. NeetCode submission is optional and never the primary grader.
16. Reveal the answer animation only after code, tests, explanation, and review are locked; every academic verdict and completed coached encounter may open it, but watching it never changes the academic result.
17. Use one declarative animation player with reusable algorithm primitives and a versioned `AnimationSpec` for each problem, not 500 unrelated JavaScript implementations.
18. Make a current, verified animation package a fail-closed scheduling prerequisite. A broken or uncertified animation can never enter the production learning flow, and a text-only fallback does not satisfy this requirement.
19. Use the fictional `Evidence-First Composite Staff Interviewer` persona for post-submission Codex review, with high standards inspired by the user-named Jane Street, Google, Anthropic, OpenAI, Hudson River Trading, and Jump Trading environments.
20. Start production learning with a qualified P001–P080 Array Systems wave instead of waiting for all 500 content packages. All 80 first-wave problems must be qualified before the first production attempt; no unqualified problem is ever scheduled.
21. Require a version-bound grader calibration certificate before Codex can issue academic recommendations. Calibration uses explicit 0–4 score anchors, a 72-case golden suite, zero false PASS on known-invalid cases, and reproducible acceptance metrics.
22. After the qualified P001–P080 release is installed, run one idle-aware background animation factory for P081–P500. It resumes from SQLite on application startup, yields to coding, tests, voice, and foreground Codex work, and never promotes or schedules an unqualified package.

### 2.1 Explicit amendments to the master plan

The user approved three intentional amendments. These are the only places where this design supersedes the supplied v2.0 plan:

1. The initial attempt, D0, and D1 are coached learning encounters. The original D1 no-AI PASS is replaced by `CoachSession.COACHED_COMPLETE`.
2. Formal blind outcomes begin at D3. D30 and Final B remain unaided full-code gates, so the Level B certification definition is unchanged.
3. The coach consumes 37.5 hours of the original 90-hour failure-recovery reserve, leaving 52.5 hours.

After encounter 3, coach mode is permanently exhausted for that problem. A later FAIL that resets the B path to D1 creates a blind D1 recovery event; it never re-enables coaching.

## 3. System architecture

```text
Local browser
  ├─ Today / Calendar / Problems / Certification / Analytics
  └─ Focused practice screen
       ├─ bilingual blind prompt
       ├─ Python code editor
       ├─ timer and attempt declarations
       └─ microphone recorder
              │
              ▼
Local Python web application
  ├─ scheduler and mastery state machine
  ├─ SQLite repositories and migrations
  ├─ append-only interaction ledger and reconstruction verifier
  ├─ deterministic Python test runner
  ├─ audio conversion and whisper.cpp adapter
  ├─ Codex CLI coach/reviewer adapter
  ├─ animation qualification, unlock, and session services
  ├─ idle-aware animation factory and durable job lease
  ├─ export, backup, and restore
  └─ static HTML/CSS/JavaScript assets
              │
              ▼
Local data
  ├─ tracker.sqlite3
  ├─ curated problem snapshot
  ├─ bilingual problem cards
  ├─ content-addressed animation packages and certificates
  ├─ persistent animation build queue and event history
  ├─ user code submissions
  ├─ retained Final B/C audio
  └─ CSV / JSON / Markdown backups
```

### 3.1 Application stack

- FastAPI for the local HTTP application and typed API boundary
- Jinja2 for server-rendered shells where appropriate
- HTML, CSS, and small vanilla-JavaScript modules for interaction
- CodeMirror 6 bundled into local static assets for the Python editor
- SQLAlchemy 2 and Alembic for SQLite persistence and migrations
- Pydantic models at process and API boundaries
- pytest, Ruff, and mypy for verification
- Playwright for a small set of critical browser-flow tests
- `whisper.cpp` and FFmpeg as local executables managed by explicit setup checks
- Codex CLI non-interactive mode for structured coaching and review

No frontend or model asset may depend on a CDN at runtime. After initial dependency and speech-model installation, core study functions must work offline except Codex review, which depends on the user's Codex authentication and service availability.

## 4. Problem-set selection and freezing

### 4.1 Source policy

The selection source is the NeetCode All catalog as observed on 2026-08-06. The current UI reports 973 problems: 224 Easy, 600 Medium, and 149 Hard. The selected dataset is a checked-in snapshot, not a runtime scrape.

The application stores minimal source metadata and original pedagogical material:

- NeetCode identifier and source URL
- canonical LeetCode identifier when available
- title, difficulty, category, and Free/Pro status at snapshot time
- company-ranking evidence permitted by the user's account
- selection score and reason
- original Korean and English paraphrases written for this curriculum
- original tests and explanations written for this curriculum

The repository must not copy NeetCode videos, official explanations, official hidden tests, or long verbatim problem statements.

### 4.2 Selection pipeline

1. Import the authenticated Pro catalog snapshot through an explicit one-time curator workflow.
2. Deduplicate by canonical LeetCode ID. Alternative solutions never count as separate problems.
3. Use the complete NeetCode 250 as the prerequisite spine when an item remains accessible and has a valid canonical ID.
4. Add 250 distinct NeetCode All problems to fill the remaining curriculum and difficulty quotas.
5. Enforce the final difficulty counts exactly: 100 Easy, 320 Medium, and 80 Hard.
6. Enforce coverage of every required pattern family and the master plan's C-120 allocation.
7. Order problems by prerequisite relationships, not by raw frequency alone.
8. Freeze P001–P500 IDs, order, source snapshot, and selection evidence.
9. Permit replacement only when a problem becomes deleted or inaccessible; the replacement must match difficulty and primary pattern.

Because NeetCode 250 currently contains 60 Easy, 155 Medium, and 35 Hard problems, the extension set targets 40 Easy, 165 Medium, and 45 Hard.

### 4.3 Global-frequency ranking

Frequency is the largest scoring component but cannot override hard coverage, difficulty, or prerequisite constraints.

```text
selection_score =
    0.50 × normalized_interview_frequency
  + 0.20 × normalized_company_breadth
  + 0.20 × pattern_representativeness_and_transfer
  + 0.10 × curriculum_and_variation_value
```

- `normalized_interview_frequency` is the mean normalized rank percentile across company lists in which the problem appears.
- `normalized_company_breadth` is the number of distinct tagged companies divided by the maximum observed breadth in the snapshot.
- `pattern_representativeness_and_transfer` is a curator score from 0–100 based on reusable invariants, states, and algorithmic structure.
- `curriculum_and_variation_value` is a curator score from 0–100 based on prerequisite fit, non-duplication, bilingual prompt stability, and Level C follow-up value.

All component values, the final score, and the reason for inclusion must be stored so the frozen set is auditable.

### 4.4 Array Systems concentration

P001–P080 is a connected curriculum covering arrays, hashing, sorting, prefix sums, two pointers, and sliding windows. It is not defined as “the first 80 of the 175 Arrays & Hashing bucket.” Problems are selected from the union of these related families, deduplicated, and ordered by prerequisite.

All eligible but unselected problems in that union enter `Array Depth Queue`. Its size is computed after the authenticated snapshot is deduplicated; it is not hard-coded as 95.

P001–P080 is also the first production content wave. Every one of the 80 problems must have a semantically aligned bilingual card, deterministic tests, canonical answer, qualified animation package, and current qualification certificate before the first real attempt may start. The learner completes the three coached encounters for all 80 in prerequisite order before any new P081 problem is introduced. Due D3-and-later reviews continue on their canonical dates and may overlap later content expansion.

P081–P500 remain frozen from the beginning but do not block Wave 1. After the first 80 complete their coached phase, each later problem becomes introduction-eligible only when its own full content package is qualified and its prerequisite problems are eligible. There is no fixed later-wave size. Final product content completion still requires 500 of 500 qualified packages.

### 4.5 C-120 selection

C-120 remains a subset of the frozen 500 and follows the master plan's exact pattern-family allocation. Candidates must have:

- strong pattern representativeness
- at least two meaningful variation axes
- a reusable invariant, recursive contract, or state definition
- high explanation and interviewer follow-up value
- balanced topic and difficulty coverage

## 5. Bilingual content policy

Each selected problem has a bilingual blind card with:

- `statement_ko` and `statement_en`
- `constraints_ko` and `constraints_en`
- original examples
- stable input/output contract
- hidden title and hidden pattern metadata
- source URL available only outside an active blind attempt

Korean and English cards must express equivalent semantics. A validation test compares structured constraints and test adapters rather than relying on text similarity.

During blind review, the UI shows the assigned language only. The user cannot reveal the alternate language, title, tags, prior code, or canonical card without invalidating the attempt.

## 6. Nine-encounter learning protocol

The original master plan has eight named stages from D0 through Final B, but its first-learning budget already contains an initial attempt before D0 reconstruction. Counting that initial attempt separately produces nine actual encounters without adding another full-code stage.

| Encounter | Timing | Language | Work | Mode | Formal result |
|---:|---|---|---|---|---|
| 1 | Initial exposure | Korean | Understand, propose approach, begin implementation | Codex coach | `COACHED_COMPLETE` |
| 2 | D0 | Korean | Reconstruct the full solution | Codex coach | `COACHED_COMPLETE` |
| 3 | D1 | English | Full implementation from the English card | Codex coach | `COACHED_COMPLETE` |
| 4 | D3 | English | 3–5 minute trigger, invariant/state, complexity, and skeleton recall | Blind | `PASS/RETRY/FAIL` |
| 5 | D7 | Random Korean or English | Timed full implementation | Blind | `PASS/RETRY/FAIL` |
| 6 | D14 | English | 4–6 minute boundary, counterexample, and critical-loop recall | Blind | `PASS/RETRY/FAIL` |
| 7 | D30 | English | Title- and tag-hidden full implementation | Blind | `PASS/RETRY/FAIL` |
| 8 | D60 | Random Korean or English | 5–8 minute explanation, alternative, and likely follow-up | Blind | `PASS/RETRY/FAIL` |
| 9 | Final B, D+90 to D+150 | English | Interview-style full implementation and explanation | Blind | `PASS/RETRY/FAIL` |

The first three encounters are learning events, not certification attempts. `COACHED_COMPLETE` is a `CoachSession` status and is not added to the master plan's `ReviewEvent.result` enum. Formal `PASS`, `RETRY`, and `FAIL` outcomes begin at D3. D3 is not scheduled until all three coach sessions are complete.

Level B still requires an unaided D30-or-later full-code PASS and an unaided Final B PASS at least 90 days after introduction. No universal D120 full-code event is created.

For C-120:

- C1 is combined with D30.
- C2 is combined with D60.
- Final C follows Final B immediately.
- All C work is blind and cannot use the coach.

## 7. Codex coach mode

### 7.1 Scope and budget

Coach mode is available only for encounters 1–3. Each encounter permits one accepted direction check with a 90-second reading-and-response budget. Across 500 problems this reallocates 37.5 hours from the 90-hour failure-recovery reserve, leaving 52.5 hours of explicit recovery reserve.

The UI may initiate the one check after at least eight seconds of inactivity and sufficient new content. The request is asynchronous and tied to a content hash. If the user changes the code or explanation before the response arrives, the response is stale and must not be displayed or counted.

### 7.2 Allowed response

The coach returns strict structured output:

```text
direction: ON_TRACK | NEEDS_DETAIL | RETHINK
reason: one short sentence
socratic_question: one short question
forbidden_content_detected: boolean
```

The coach must not provide:

- the algorithm or pattern name when the user has not already named it
- solution code or code completion
- pseudocode
- the canonical invariant or DP state
- a counterexample that directly reveals the solution
- references to prior submissions or canonical solution cards

Any response that violates this contract is suppressed, logged as a system error, and does not consume the encounter's accepted check.

### 7.3 Blind lockout

At D3 and later, coach controls, endpoints, keyboard shortcuts, and background triggers are disabled server-side. Hiding a button in the browser is insufficient. Post-submission Codex review is allowed only after code, tests, spoken explanation, timing, and declarations are locked.

## 8. Deterministic code execution

The test runner, not Codex, is the correctness oracle.

- Execute Python 3.12 submissions in a fresh temporary directory.
- Run Python in isolated mode with a fixed import path and a problem-specific adapter.
- Apply wall-clock timeout, process-group termination, output-size limits, and conservative CPU and memory limits where the host supports them.
- Do not expose canonical solutions to the submission process.
- Store stdout, stderr, exit status, duration, and individual test results.
- Require user-authored boundary cases in addition to curriculum tests.
- Treat infrastructure failure as `SYSTEM_ERROR`, never as `FAIL`.

This runner is intended only for the local single user's own code. It is not a security boundary for executing code submitted by strangers and must not be exposed as a public service.

## 9. Codex CLI review

The Python backend invokes Codex without a shell, using an argument array and prompt on stdin. A review run uses:

- `codex exec`
- `--ephemeral`
- `--sandbox read-only`
- approval policy `never`
- `--output-schema` with a checked-in JSON Schema
- `--color never`
- a fresh temporary Git repository containing only the locked evaluation bundle

The bundle contains:

- bilingual problem contract for the assigned language
- submitted code
- deterministic test results
- locked written and spoken explanations
- timing and pattern-recognition measurements
- hint, prior-code, AI, and source-view declarations
- rubric for the current stage

The reviewer returns structured fields for correctness reasoning, invariant/state, complexity, boundary coverage, explanation quality, prohibited assistance, and a recommended `PASS`, `RETRY`, or `FAIL`. The backend owns the final transition and applies deterministic gates before accepting the recommendation. A failing deterministic test cannot be overturned by Codex.

If Codex is unavailable, unauthenticated, rate-limited, times out, or returns invalid JSON, the attempt becomes `PENDING_AI_REVIEW`. Its stage does not advance and it does not become `FAIL`. One automatic retry is permitted; further retry is manual.

### 9.1 Evidence-First Composite Staff Interviewer

Post-submission review uses a fictional composite persona named `Evidence-First Composite Staff Interviewer`. It combines the rigorous engineering bar the user wants to associate with Jane Street, Google, Anthropic, OpenAI, Hudson River Trading, and Jump Trading. It does not impersonate an employee, claim inside information, or claim that its rubric is an official hiring process of any named company.

The persona is strict but calibrated. It applies proof, performance, testing, maintainability, epistemic calibration, and concise communication standards at the level appropriate to the problem difficulty and encounter. It does not demand staff-level system design for an Easy algorithm problem and does not penalize a correct alternative merely because it differs from a preferred style.

The primary reviewer receives only the current locked evaluation bundle. It cannot see the user's name, prior attempts, prior grades, open weaknesses, scheduler state, canonical solution, or another reviewer's verdict. This prevents history and expectation bias. Its rules are:

- cite exact code lines, test cases, transcript spans, or declarations for every material claim
- distinguish observed facts, valid deductions, missing evidence, and uncertainty
- never infer knowledge that the locked evidence does not demonstrate
- ignore effort, elapsed study history, and stylistic preference when assigning the academic recommendation
- assess the stage-specific contract rather than applying one undifferentiated full-code rubric
- return feedback calmly and concretely in Korean first and English second
- identify one demonstrated strength, one highest-leverage weakness, and one bounded next drill

The structured response contains the recommendation, deterministic-gate acknowledgement, evidence references, rubric scores for correctness reasoning, invariant/state, complexity, boundary coverage, code quality, test design, and spoken explanation, confidence, uncertainty reasons, the strength, the weakness, and the next drill.

### 9.2 Review decision pipeline

Review proceeds in three logically isolated steps:

1. **Evidence extraction:** index only facts and citations from the locked bundle.
2. **Rubric evaluation:** apply the versioned rubric for the current problem, difficulty, format, language, and encounter.
3. **Recommendation:** produce `PASS`, `RETRY`, or `FAIL` with confidence and cited reasons.

The backend then applies deterministic policy:

- required deterministic tests failing, a prohibited-assistance violation, or a materially incorrect core algorithm prevents `PASS`
- passing tests with a meaningful invariant, complexity, boundary, or explanation deficiency produces `RETRY` when the stage requires that dimension
- `PASS` requires every hard gate and the stage-specific rubric threshold
- coached encounters use formative feedback but end only as `COACHED_COMPLETE`; they never receive an academic result

Final B, Final C, and any low-confidence or internally inconsistent recommendation receive an independent blind shadow review. The shadow reviewer uses the same bundle and rubric but cannot see the first verdict. Agreement permits backend finalization. Material disagreement becomes `NEEDS_SECOND_REVIEW`; it never becomes an automatic `FAIL`. From that queue the user may request one fresh paired review whose two reviewers are again isolated from each other and the prior verdicts. If the fresh pair still materially disagrees, the attempt closes as `SYSTEM_ERROR` without an academic result and the same stage is rescheduled from the locked prompt contract.

The local application remains the primary grading surface. After the verdict and answer-animation unlock, the user may open the source problem and manually record an external NeetCode result for comparison. The application does not automate submission to NeetCode, and an external result cannot overwrite the immutable local evidence or verdict.

### 9.3 Grader calibration and qualification

The persona description alone is not a grading standard. Academic review is enabled only when the exact grader configuration has a current `GraderQualificationCertificate` produced from a locked golden suite.

Every rubric dimension uses the same anchored 0–4 scale:

| Score | Observable meaning |
|---:|---|
| 0 | Missing, non-responsive, or contradicted by the locked evidence |
| 1 | Major misconception that invalidates the required reasoning |
| 2 | Partially correct but contains a material gap for the current encounter |
| 3 | Correct, complete, and interview-ready for the current encounter |
| 4 | Exceptionally rigorous and concise, with no factual error; never required for PASS |

`RubricVersion` contains an explicit encounter matrix. It maps every academic encounter to one of four profiles and marks each dimension as `REQUIRED`, `SECONDARY`, or `NOT_SCORED`:

- `COMPACT_RECALL`: D3, D14, and compact D365; trigger/approach, invariant or state, stage-required skeleton or counterexample, and complexity are required as applicable to the encounter
- `FULL_IMPLEMENTATION`: D7, D30, Final B, and full D365; correctness reasoning, invariant/state, complexity, boundary coverage, and explanation are required; code quality and test design are secondary
- `EXPLANATION_FOLLOWUP`: D60; invariant/state, alternative, likely follow-up, complexity, boundary reasoning, and communication are required
- `C_VARIATION`: C1, C2, and Final C; variation modeling, transfer of the invariant/state, correctness reasoning, complexity, and explanation are required

Outcome mapping is deterministic after the test and assistance gates:

- `PASS`: all deterministic gates pass, every required dimension is at least 3, every secondary dimension is at least 2, and there is no critical factual contradiction
- `RETRY`: deterministic correctness gates pass and no critical dimension is 0 or 1, but at least one required dimension is below 3 or one secondary dimension is below 2
- `FAIL`: a required deterministic correctness gate fails, prohibited assistance invalidates a blind attempt, the core algorithm is materially wrong, or any critical required dimension is scored 0 or 1
- coached encounters receive the same anchored formative fields where applicable but never map them to an academic outcome

The initial golden suite contains 72 immutable evaluation bundles: 18 per profile, with six expected `PASS`, six expected `RETRY`, and six expected `FAIL`. Across the complete suite it covers Korean and English, Easy/Medium/Hard, every required pattern family, valid alternative solutions, misleading-but-plausible explanations, boundary failures, complexity mismatches, and assistance violations. Each case stores expected dimension ranges, expected outcome, hard-gate facts, and source-cited adjudication notes. Golden bundles are calibration fixtures and never appear as the user's live attempt.

Initial qualification and any configuration change run the complete suite twice. Both runs must satisfy all of the following:

- 100% agreement on deterministic and assistance hard gates
- zero false `PASS` among golden `FAIL` and assistance-violation cases
- at least 17 of 18 exact outcomes in each profile
- quadratic-weighted Cohen's kappa of at least 0.80 against the golden outcomes
- mean absolute dimension-score error no greater than 0.40 on the 0–4 scale; a score inside the case's accepted range has zero error, otherwise error is its distance to the nearest range boundary
- at least 95% exact-outcome agreement between the two calibration runs
- 100% of material findings point to a valid code, test, transcript, or declaration evidence reference

The certificate binds the requested and observable model metadata, Codex CLI version, reviewer prompt hash, output-schema hash, rubric version, evidence-bundle builder version, calibration-suite version, and aggregate metrics. A change to any bound value revokes the certificate and requires full qualification.

To detect drift behind an unchanged model identifier, a rotating 24-case canary runs every 30 days. It must preserve 100% hard-gate accuracy, zero false `PASS`, at least 22 of 24 exact outcomes, and valid evidence citations. A passing canary renews the unchanged configuration for another 30 days but never beyond its 90-day full-requalification deadline. A failed canary immediately revokes the grader certificate and requires the full 72-case qualification. A complete two-run qualification is mandatory every 90 days.

Without a current certificate, Codex may not issue a new academic recommendation. Already locked attempts remain `PENDING_AI_REVIEW`; deterministic test evidence is preserved, and no attempt becomes `FAIL` because calibration is missing or expired. Revocation or expiry blocks future recommendations but never rewrites a historical review that completed while its certificate was valid.

## 10. Spoken explanations

### 10.1 Capture and transcription

1. The browser requests microphone permission with `getUserMedia({ audio: true })`.
2. `MediaRecorder` captures an audio format supported by the current browser.
3. The backend stores the upload in an attempt-scoped temporary directory.
4. FFmpeg converts it to 16 kHz mono 16-bit PCM WAV.
5. `whisper.cpp` transcribes locally with the multilingual `small` model.
6. The current session language is passed explicitly as Korean or English.
7. The UI shows audio playback, raw transcript, and any user corrections.
8. The user confirms the transcript before submission is locked.

Codex reviews the confirmed transcript, not raw audio. The original transcript, corrected transcript, and correction diff are retained so corrections cannot silently add reasoning that was not spoken. Substantive correction requires rerecording in certification modes.

### 10.2 Explanation prompts

Each full-code session records three bounded segments:

1. pattern choice and brute-force bottleneck
2. invariant, recursive contract, or DP state and correctness
3. time/space complexity and boundary cases

Compact sessions record only the stage-specific explanation required by the schedule.

### 10.3 Retention and fallback

- Normal D0–D60 audio is deleted after transcription is confirmed and the attempt is finalized.
- Final B and Final C audio is retained for audit and included in backup manifests.
- Transcripts, durations, and correction metadata remain structured records.
- A microphone or transcription failure exposes a typed-explanation fallback and records `voice_unavailable`; infrastructure failure cannot cause an academic `FAIL`.

## 11. User interface

### 11.1 Visual direction

Use the approved Midnight Focus design:

- dark navy surfaces rather than pure black
- restrained blue action color
- high-contrast code with lower-contrast surrounding chrome
- minimal information during blind work
- keyboard-first controls
- responsive layout with the voice panel moving below the editor on narrower screens

### 11.2 Required screens

**Today**

- planned and actual minutes
- holiday status
- Wave 1 content readiness and grader-certificate status before the first production start
- priority-sorted queue
- separate coach, B, C, unseen, and mock items
- estimated remaining time

**Practice**

- assigned bilingual blind card
- title, tags, source, alternate language, prior code, and canonical notes hidden
- timer and pattern-recognition timer
- CodeMirror Python editor
- user-authored tests and deterministic test results
- voice recording and transcript confirmation
- visible `Recording`/`Synced` ledger state without showing noisy event counts
- coach meter only for encounters 1–3
- post-lock Codex review and immutable verdict evidence
- post-verdict answer animation with one logical step per click

**Calendar**

- planned versus actual time
- public-holiday overrides
- due, completed, failed, and certified counts
- Green, Yellow, and Red state

**Problems**

- frozen P001–P500 list
- selection score and evidence
- B/C target and current state
- next review date
- content qualification state and blocking reason for every problem
- bilingual card and source links outside blind attempts
- Array Depth Queue as a separate non-scheduled view

**Certification**

- eligible Final B queue
- C1, C2, and Final C queues
- controlled unseen reveal
- mock schedule
- pending AI-review queue
- grader qualification, expiry, drift-canary, and full-renewal status

**Analytics**

- progress funnels
- per-problem attempt timelines with like-for-like deltas between comparable attempts
- evidence-backed weakness history and user-controlled weakness confirmation or dismissal
- explainable problem and weakness filters for manual cherry-picking
- pass rates by pattern, difficulty, language, and encounter
- coach-direction distribution and subsequent blind performance
- failure categories and Red Queue
- average coding, recognition, and speaking times
- budget burn and projected dates
- unseen and mock results
- D365 maintenance status after the first year

### 11.3 Post-verdict answer animation

Every frozen problem has a Korean-first and English-capable answer animation. The server never sends its spec, canonical code, pattern metadata, or derived assets to an active blind attempt. The unlock occurs only after the submission, tests, explanation, declarations, and review are immutable. `PASS`, `RETRY`, and `FAIL` may all open the explanation. A coached encounter may open it only after its locked formative review and `COACHED_COMPLETE`. The animation is a learning artifact, not a grading input.

The approved interaction is a focused single-screen progressive reveal:

1. Show the data structure and one short sentence for the current state.
2. Advance exactly one logical state change when the user selects **Next step** or presses the documented key.
3. Reveal only the currently relevant code line when the visual concept becomes clear.
4. Offer **More detail** to expand the current main step into two to four microsteps without changing the main-step count.
5. Reveal the complete canonical code, complexity, and edge-case summary only at the final main step.

Each problem contains six to ten main conceptual steps. There is no autoplay. Previous, next, restart, language switch, detail expansion, keyboard focus, and reduced-motion behavior are deterministic. The default start is always step 1, even when an open weakness highlights a later related step.

The player is one reusable renderer backed by declarative `AnimationSpec` data. Reusable primitives cover arrays, pointers, hash maps, linked lists, stacks, queues, trees, tries, graphs, union-find, heaps, intervals, matrices, dynamic programming, backtracking, and bit operations. A problem spec may compose primitives and state transitions but may not execute arbitrary JavaScript. Codex may draft a spec, but only reviewed, qualified content is eligible for scheduling.

Watching, skipping, replaying, expanding details, or changing animation language never changes `PASS`, mastery, certification, or the next canonical schedule item. It produces learning analytics only. A later voluntary drill must be created explicitly through `PracticeRequest`.

### 11.4 Idle-aware background animation factory

P001–P080 is produced and qualified before the first production release. After that release, starting the local application also resumes a durable, single-worker factory for P081–P500. The application UI becomes available immediately; factory startup never blocks Today, an existing attempt, or a due review.

The worker processes the earliest prerequisite-ready problem and persists every transition in SQLite:

```text
WAITING_CONTENT ──dependency ready──> QUEUED
QUEUED → DRAFTING → VALIDATING → QUALIFIED
DRAFTING or VALIDATING ──failure──> RETRY_WAIT ──not_before──> DRAFTING
DRAFTING or VALIDATING ──failure after retry 3──> BLOCKED
```

`WAITING_CONTENT` means the bilingual card, semantic contract, canonical answer, deterministic tests, or prerequisites are not yet complete; it consumes no failure attempt and becomes `QUEUED` when the dependency event arrives. `DRAFTING` uses the isolated animation-authoring adapter and only frozen curriculum artifacts, never learner attempts, transcripts, weaknesses, or grader history. `VALIDATING` performs the complete schema, semantic, replay, bilingual, viewport, accessibility, prohibited-content, and renderer qualification suite. Only successful validation creates an `AnimationQualificationCertificate` and atomically promotes the package to `QUALIFIED`.

The factory is idle-aware rather than continuously competitive. A foreground activity lease is held while any of the following is true:

- an `IN_PROGRESS` attempt is visible in the focused practice page, or editor input was received within the last 30 seconds
- a deterministic test run is active
- recording, FFmpeg conversion, or whisper.cpp transcription is active
- a foreground Codex coach, primary review, shadow review, or grader-calibration run is active

The worker starts a stage only after the lease has been clear for 30 seconds. If foreground work begins during a background stage, the worker requests cooperative cancellation, terminates its child process after a five-second grace period when necessary, saves the last durable checkpoint, and returns the job to its prior runnable state. Foreground preemption does not increment the failure count. One SQLite-backed global lease, renewed every 15 seconds and expired after 60 seconds without a heartbeat, prevents two application processes from building simultaneously and allows safe crash recovery.

Real build failures use exact bounded backoff with at most three retries: 1 minute after the first failed execution, 4 minutes after the second, and 16 minutes after the third. If the third retry also fails—the fourth consecutive failed execution—the job becomes `BLOCKED`, its evidence and repair reason remain visible, and the factory continues with the next eligible problem. A content correction or explicit retry event creates a new runnable transition; it does not erase the failures. Rate limits and temporary Codex unavailability follow the same durable retry path, while missing content remains `WAITING_CONTENT`.

The global header shows a quiet status such as `Animation Factory · 126/500 · P127 validating`, plus `paused for practice`, `waiting for content`, `retry scheduled`, `blocked`, or `500/500 complete` when applicable. It never opens a modal, steals editor focus, auto-plays an explanation, or inserts an unqualified problem into the study queue. The worker stops when all 500 current packages qualify and automatically re-enqueues only packages invalidated by a later contract, answer, test, player, application-build, or compatibility change.

## 12. Data model additions

The master plan's original models remain the base. The implementation adds or separates the following concepts.

### 12.1 `SelectionEvidence`

- `problem_id`
- `snapshot_date`
- `free_or_pro`
- `company_count`
- `normalized_frequency`
- `normalized_company_breadth`
- `pattern_transfer_score`
- `curriculum_variation_score`
- `final_selection_score`
- `selection_reason`
- `replacement_for_problem_id`

### 12.2 `ProblemText`

- `problem_id`
- `language: KO | EN`
- `statement`
- `constraints`
- `examples_json`
- `content_version`
- `semantic_contract_hash`

### 12.3 `CoachSession`

- `attempt_id`
- `encounter: INTRO | D0_COACHED | D1_COACHED`
- `content_hash`
- `requested_at`
- `completed_at`
- `direction`
- `reason`
- `socratic_question`
- `forbidden_content_detected`
- `status: COACHED_COMPLETE | STALE | SYSTEM_ERROR | ABANDONED`
- `duration_seconds`

### 12.4 `CodeSubmission` and `TestRun`

`CodeSubmission` stores immutable code snapshots, language, editor timestamps, and assistance declarations. `TestRun` stores the exact adapter version, test manifest hash, per-test results, process output, resource limits, and duration.

### 12.5 `VoiceExplanation`

- `attempt_id`
- `segment_kind`
- `audio_path` when retained
- `raw_transcript`
- `confirmed_transcript`
- `correction_diff`
- `language`
- `duration_seconds`
- `transcriber_version`
- `model_hash`
- `retention_policy`

### 12.6 `CodexReview`

- `attempt_id`
- `review_kind: COACH | PRIMARY_POST_SUBMISSION | SHADOW_POST_SUBMISSION`
- `input_bundle_hash`
- `schema_version`
- `rubric_version_id`
- `grader_qualification_certificate_id` for academic recommendations
- `codex_thread_id` when emitted
- `raw_result_json`
- rubric fields
- `recommended_result`
- `started_at`, `completed_at`, and `duration_seconds`
- `status: COMPLETE | PENDING | SYSTEM_ERROR`; disagreement is represented on `Attempt.lifecycle_status`, not on either immutable review row

### 12.7 State representation

B progress and C progress are derived separately from immutable events. They are not represented by a single mutable enum that forces C1/C2 to occur after B certification. Cached status fields may exist for display, but event history remains the source of truth.

### 12.8 `ScheduleItem` and `Attempt`

`ScheduleItem` represents work the curriculum requires. It stores `problem_id`, stage, due time in UTC, the Asia/Seoul study date, source, priority tier, current status, and the attempt that created the next item. An overdue item remains overdue; it is never silently moved or replaced.

The scheduler cannot create an introduction item for an unqualified problem. Before the first production attempt it also requires the P001–P080 all-or-nothing Wave 1 gate and a current grader certificate. After Wave 1 begins, reviews for qualified problems continue normally; the new-problem generator blocks P081 until all first-wave problems have completed encounter 3, then applies per-problem content and prerequisite eligibility.

`Attempt` is the central learning-history row. One row is created every time the user actually starts a problem, including coached encounters, blind encounters, recovery work, C certification, D365 maintenance, and optional user-selected drills.

Required fields are:

- `problem_id`, optional `schedule_item_id`, and optional `practice_request_id`
- monotonically increasing `sequence_no` per problem
- encounter, study mode, prompt language, and `FULL | COMPACT` format
- lifecycle status: `IN_PROGRESS | PENDING_AI_REVIEW | NEEDS_SECOND_REVIEW | FINALIZED | ABANDONED | SYSTEM_ERROR`
- academic result when applicable: `PASS | RETRY | FAIL`; it remains `NULL` for coached encounters, whose completion is recorded by `CoachSession.status = COACHED_COMPLETE`
- start, lock, and finalization timestamps in UTC plus the Asia/Seoul study date
- active duration, assistance declaration, assistance-violation flag, and semantic-contract hash

The attempt may change while it is in progress. Once finalized, its academic fields and locked artifacts are append-only. A correction creates an audit event instead of rewriting the historical record. Database constraints reject duplicate `(problem_id, sequence_no)` values, blind PASS with an assistance violation, an academic result on a coached encounter, and an academic result on a system-error attempt.

### 12.9 `AttemptMetrics`

`AttemptMetrics` is a one-to-one, query-friendly summary of an attempt. Query-critical metrics are normal columns rather than opaque JSON:

- pattern-recognition, coding, debugging, and speaking seconds
- tests passed, tests total, first-run pass, and deterministic-run count
- submission count, code-edit count, and syntax/runtime/wrong-answer counts
- explanation scores for approach, invariant, complexity, and edge cases

Blind-pass streak and other cross-attempt values are derived by SQL views rather than stored in this row. The analytics UI never presents a compact attempt as if it were directly faster than a full-code attempt. Time deltas use the previous comparable attempt and label format, language, and coached/blind mode. Raw history remains visible even when a summarized trend is shown.

### 12.10 `WeaknessType`, `WeaknessObservation`, and `WeaknessStatusEvent`

Weaknesses are evidence-backed observations, not a single mutable label on a problem.

`WeaknessType` defines the stable taxonomy and the recommended drill. The initial taxonomy is:

- pattern recognition
- data-structure choice
- invariant reasoning
- complexity analysis
- boundary cases
- implementation accuracy
- test design
- English comprehension
- time management
- explanation clarity

`WeaknessObservation` records `attempt_id`, `problem_id`, type, severity from 1 to 3, source, confidence, a compact evidence reference, and the recommended drill. Sources are `TEST_RUN`, `CODEX_REVIEW`, `SELF_CHECK`, `TIMER`, or `RULE_ENGINE`. Flexible supporting details may use JSON, but evidence needed for filtering stays normalized.

`WeaknessStatusEvent` appends `CONFIRMED`, `DISMISSED`, `IMPROVING`, `RESOLVED`, or `REOPENED` events. It records the responsible attempt or user action and never deletes the original observation. This allows the UI to show when a weakness first appeared, how often it recurred, which attempt resolved it, and whether it later returned.

Codex may propose a weakness, but the UI identifies its source and confidence. Deterministic tests remain the correctness oracle, and the user can dismiss an inaccurate AI observation without destroying the audit trail.

### 12.11 `PracticeRequest` for cherry-picking

The user can filter and select a problem or one of its open weaknesses to create a `PracticeRequest`. It stores the selected problem, target weakness, requested language, requested format, requested drill, creation time, and completion state. The resulting attempt links back to the request.

A manual request does not alter the canonical nine-encounter schedule or erase review debt. Queue ordering is explainable and stable:

1. required due and overdue work
2. Red Queue and recent FAIL recovery
3. unresolved severe or recurring weaknesses
4. measured regression
5. voluntary user cherry-picks

When there is no required debt, a voluntary request can be started immediately. Suggested drills are weakness-specific: trigger recall for pattern recognition, a two-minute invariant explanation, boundary-test design, full implementation, complexity analysis, or English prompt paraphrasing.

### 12.12 Derived SQLite views

Analytics read from deterministic SQL views rather than asking Codex to invent a mastery score:

- `v_attempt_timeline`: every attempt, artifact status, metrics, and deltas from the previous comparable attempt
- `v_problem_progress`: latest stage/result, next due item, blind pass rate and streak, first-versus-latest comparable timing, and open weakness count
- `v_open_weaknesses`: latest status, recurrence count, maximum severity, last-seen date, supporting attempts, and recommended drill
- `v_practice_candidates`: one explainable row per eligible problem with priority tier, reason codes, target weakness, and suggested mode
- `v_pattern_risk`: unresolved and recurring weaknesses grouped across pattern, difficulty, language, and blind stage
- `v_content_readiness`: Wave 1 80-of-80 status, first-wave coached completion, later eligible/blocked counts, and final 500-of-500 status
- `v_animation_factory`: qualified count, one active job, queued/waiting/retry/blocked counts, next eligible problem, pause reason, lease health, and latest build evidence
- `v_grader_health`: active configuration hash, certificate status and expiry, latest canary/full-run metrics, and the exact reason academic review is enabled or blocked

The problem detail page exposes the underlying attempts behind every trend and recommendation. No chart or recommendation is accepted as evidence unless the user can drill down to the source attempt, test failure, transcript rubric, or review observation.

### 12.13 SQLite durability and transaction rules

- Enable `foreign_keys=ON`, `journal_mode=WAL`, `synchronous=FULL`, and a 5-second busy timeout for every application connection.
- Store timestamps in UTC and store the derived Asia/Seoul study date separately for calendar queries.
- Normalize fields used for filters and constraints. Use JSON only for versioned rubrics, per-test payloads, and compact supporting evidence.
- Index schedule due/status, attempts by problem/sequence and study date, weakness type/status lookup, and practice-request state.
- Finalize one attempt in a single `BEGIN IMMEDIATE` transaction: lock the submission, attach the accepted test run and transcript, store the Codex review, append weakness observations/status events, assign the outcome, and create the next schedule item.
- If Codex review is unavailable, first preserve the already locked artifacts in a short transaction and set `PENDING_AI_REVIEW` without an academic outcome. A later successful retry performs the atomic academic-finalization transaction; it does not rerun or rewrite the user's submission.
- Use Alembic migrations and record the application/schema version in every export manifest.
- Run `PRAGMA integrity_check` during verified backup/restore. Back up the database with the SQLite backup API so committed WAL-backed state, the retained-audio manifest, and content hashes form one consistent snapshot.

### 12.14 `InteractionEvent`, `EditorCheckpoint`, and reconstruction

Every meaningful action inside a practice attempt is appended to `InteractionEvent`. The server assigns a monotonic `event_seq` per attempt and stores the client monotonic elapsed time, server UTC receipt time, event type, versioned payload, and relevant before/after content hashes. The event taxonomy includes:

- editor insert, delete, replace, paste, cut, undo, and redo operations
- run request, user-test creation/change, test result view, and runtime error view
- timer start, pause, resume, and expiry
- window focus, blur, reconnect, and idle boundary
- voice record, stop, replay, transcript confirmation, and correction
- coach request, stale response, accepted response, and suppression
- declaration change, lock request, submission, review receipt, and verdict acknowledgement
- answer unlock request, animation open, main-step navigation, detail expansion, language change, restart, and completion
- source-link open and manually recorded external result after verdict

Raw pointer coordinates, mouse movement, hover noise, scrolling pixels, and every physical keydown are not retained. Editor changes are semantic document operations. Transport may batch a burst, but the batch preserves every ordered operation and its offset/text payload. Sensitive browser or operating-system activity outside the practice page is never collected.

`EditorCheckpoint` stores a complete code snapshot at attempt start, every accepted run, focus loss, submission lock, and at least every 30 active seconds. Each checkpoint records the last included event sequence and its code hash. Replaying editor operations from the preceding checkpoint must reproduce the next checkpoint byte-for-byte.

The browser maintains a persistent local outbox until the server acknowledges an event watermark. Finalization is blocked while the outbox has unacknowledged events. A ledger interruption shows `Recording paused`, preserves the attempt locally, and resumes idempotently; it never silently drops actions or produces an academic outcome from a partial history.

### 12.15 `AnimationSpec` and `AnimationQualificationCertificate`

`AnimationSpec` is a versioned declarative document containing:

- `problem_id`, spec version, semantic-contract hash, and canonical-solution hash
- Korean and English title, narration, complexity, and edge-case content
- six to ten ordered main scenes and optional two-to-four-step detail expansions
- primitive instances, visual state, allowed transitions, emphasis, code references, and weakness tags
- final canonical code references and reduced-motion/accessibility annotations

The content package is content-addressed and read-only. It cannot contain executable script, external URLs, or runtime network dependencies. The player validates the schema again before rendering even though only certified packages should reach it.

`AnimationQualificationCertificate` binds a problem/spec version to its semantic-contract hash, canonical-solution hash, player/runtime version, application build, supported viewport and accessibility matrix, forward/back/detail replay trace hash, test-manifest hash, issue time, and `QUALIFIED | REVOKED` status.

Production learning first becomes `WAVE_1_READY` when all P001–P080 packages have valid certificates for the shipped player and application build and the grader has a current qualification certificate. P081–P500 do not block this first start, but an individual later problem remains ineligible until its own package and prerequisites qualify. The final product state `CONTENT_500_COMPLETE` still requires 500 of 500 current packages. Any change to a problem contract, answer, spec, player, browser-runtime compatibility boundary, or relevant application code invalidates the affected certificate and requires complete requalification.

### 12.16 `ExplanationUnlockEvent` and `AnimationViewSession`

`ExplanationUnlockEvent` records the immutable attempt, academic verdict or `COACHED_COMPLETE`, qualified spec hash, unlock time, and policy version. The backend rejects unlock while the attempt is active, coached feedback is unresolved, review is pending, or the certificate does not match the current contract and runtime.

`AnimationViewSession` records the unlocked attempt and spec version, language, open/close time, furthest main step, detail steps opened, completion, replay count, and active viewing duration. Step actions remain available in the general interaction ledger. These records support explanation-quality analytics but are excluded from academic state transitions.

### 12.17 Grader calibration records

`RubricVersion` stores the immutable 0–4 score anchors, encounter-to-profile matrix, required/secondary dimensions, hard-gate policy, outcome mapping, and content hash.

`CalibrationCase` stores the golden bundle hash, profile, language, difficulty, pattern tags, expected dimension ranges, expected academic result, hard-gate facts, adjudication evidence, and suite version. A case cannot be edited after it participates in a qualification run; correction creates a new suite version.

`CalibrationRun` stores the grader configuration hash, suite or canary version, run kind, start/end times, every case result and evidence-validation result, exact-outcome rate by profile, hard-gate rate, false-PASS count, quadratic-weighted kappa, range-aware dimension-score error, run-to-run stability when applicable, and `PASS | FAIL` status.

`GraderQualificationCertificate` stores all bound version/hash fields, qualifying run IDs, issue time, 30-day expiry, 90-day full-requalification deadline, aggregate metrics, and `QUALIFIED | REVOKED | EXPIRED` status. Every `CodexReview` references the certificate used for that recommendation. Database constraints reject a new academic recommendation with a missing, revoked, expired, or configuration-mismatched certificate while preserving reviews completed under a certificate that was valid at review time.

### 12.18 `AnimationBuildJob`, `AnimationBuildEvent`, and factory lease

`AnimationBuildJob` has one current row per problem and target content version. It stores `problem_id`, target semantic-contract/canonical-answer/test/player/application hashes, priority and prerequisite readiness, `state`, durable stage checkpoint, `failure_count`, `not_before`, `lease_owner`, `lease_expires_at`, last error code/evidence reference, and created/updated/completed timestamps. Its state is `QUEUED | WAITING_CONTENT | DRAFTING | VALIDATING | RETRY_WAIT | BLOCKED | QUALIFIED`.

`AnimationBuildEvent` is the append-only source of truth for every enqueue, dependency wait/release, lease acquisition/renewal/expiry, stage start/checkpoint/preemption, failure, retry schedule, block, qualification, promotion, invalidation, and completion. A singleton `AnimationFactoryLease` enforces the 15-second heartbeat and 60-second expiry. Startup reclaims only expired work, validates the checkpoint and target hashes, and resumes deterministically; it never assumes an interrupted draft was qualified.

## 13. Outcomes and state transitions

- Coach sessions never emit `PASS`, `RETRY`, or `FAIL`.
- Blind sessions use only `PASS`, `RETRY`, or `FAIL`.
- `PASS` advances to the next blind stage.
- `RETRY` keeps the current stage and schedules the next day.
- `FAIL` schedules relearning and resets the blind B path to a blind D1 recovery event according to the master plan. Coach mode is never restored.
- Two FAILs within 30 days enter Red Queue.
- Any hint, source view, alternate-language reveal, prior-code view, or live AI assistance during a blind attempt prevents PASS.
- System errors never advance or academically fail an attempt.
- Missed events remain overdue and are never silently shifted or deleted.
- Answer-animation unlock requires a finalized academic verdict or locked `COACHED_COMPLETE` review and a matching current qualification certificate.
- Animation viewing is downstream of the immutable review and never mutates academic state or the canonical schedule.
- Animation build jobs advance independently of academic attempts. `QUALIFIED` is reachable only through a successful current validation certificate; `BLOCKED`, `RETRY_WAIT`, `WAITING_CONTENT`, and foreground preemption never create an academic result or scheduling eligibility.

## 14. One-year and longer maintenance

The nine encounters are the first-year learning and certification protocol. They create strong conditions for durable memory but do not prove 365-day retention because Final B occurs at D+90 to D+150.

Every problem therefore receives a D365 maintenance event based on its original introduction date. Because the earliest introduction is 2026-08-06, the earliest D365 event is 2027-08-06, outside the first-year budget.

- C-120 receives an English blind full-code D365 test.
- B-only problems receive a 3–5 minute blind compact test.
- A compact-test miss immediately schedules a blind full-code test.
- A full-code miss starts the `+1d → +3d → +7d → +30d` recovery sequence.
- `MAINTAINED_FULL` schedules the next maintenance event 365 days later.
- `MAINTAINED_COMPACT` schedules the next maintenance event 180 days later.

D365 results are reported separately as `MAINTAINED_COMPACT`, `MAINTAINED_FULL`, or `MAINTENANCE_FAILED`; they do not rewrite historical B/C certification results.

## 15. Security, privacy, and reliability

- Bind the application to localhost by default.
- Do not add login for the local MVP.
- Never expose Codex auth files, API credentials, environment dumps, or model paths to the browser.
- Launch subprocesses without a shell and with explicit argument arrays.
- Keep canonical cards and tests outside submission execution directories.
- Use content hashes to make attempts, tests, transcripts, and reviews reproducible.
- Keep audio local; no speech cloud API is required.
- Store the speech model outside Git and verify its hash.
- Back up the SQLite database, retained certification audio, cards, and manifest atomically.
- Verify restore into a fresh temporary directory before marking a backup valid.
- Build animation packages in a staging area, qualify them completely, then promote the package index atomically. Partial content is never visible to the scheduler.
- Run at most one background animation stage at a time, under the SQLite factory lease, and give editor, tests, voice, foreground Codex, and calibration work exclusive foreground priority.
- Keep factory input limited to frozen curriculum artifacts. Learner code, attempts, transcripts, weakness history, and academic review output are not animation-authoring inputs.
- Retain the current and last-known-good qualified package generations. On corruption or hash mismatch, restore the last-known-good generation and re-run qualification before enabling study.
- Before a problem is eligible, an isolated renderer preflight verifies its pinned package against the current player, application build, browser-runtime compatibility boundary, and semantic contract without sending canonical content to the active blind page.
- Pin the qualified spec hash to the attempt before it starts so later content deployment cannot change the explanation attached to that attempt.
- Fail closed: if neither the current nor last-known-good package qualifies, pause new study before an attempt begins and require repair. Do not offer a text-only completion path for missing animation.

No software can promise that storage, the operating system, or browser hardware will never fail. The enforceable guarantee is stronger than a best-effort fallback: an unqualified or damaged explanation is never represented as `READY`, never starts a production attempt, never counts as completed learning, and never causes an academic result.

- A public or multi-user deployment requires a separate threat model and a real untrusted-code sandbox; it is outside this design.

## 16. Error handling

| Failure | User-visible behavior | State effect |
|---|---|---|
| Codex unavailable or rate-limited | Review marked pending with retry action | No stage advance; no FAIL |
| Codex schema violation | One automatic retry, then manual queue | No stage advance; no FAIL |
| Grader certificate missing, expired, revoked, or mismatched | Academic review controls disabled; calibration action shown | Locked attempt remains `PENDING_AI_REVIEW`; no academic result |
| Calibration or drift canary below threshold | Grader status turns red and full qualification is required | Certificate revoked; no new academic recommendation |
| Coach response leaks forbidden content | Response suppressed and incident logged | Check remains available |
| Python timeout or memory limit | Deterministic failed test with captured reason | Normal rubric applies |
| Test-runner infrastructure failure | System-error banner and retry | No stage advance; no FAIL |
| Microphone denied | Typed explanation fallback | `voice_unavailable` recorded |
| Transcription failure | Replay, rerecord, or typed fallback | No academic penalty |
| Bilingual contract mismatch | Problem blocked from scheduling | Curator repair required |
| P001–P080 only partially qualified | Content progress remains visible but production Start is disabled | No real attempt until Wave 1 is 80 of 80 |
| Foreground practice begins during an animation build | Header changes to `paused for practice`; worker checkpoints and yields within the cancellation boundary | Job returns to its prior runnable state; failure count unchanged |
| Animation source content or prerequisite missing | Factory shows `waiting for content` and proceeds to the next eligible problem | Job remains `WAITING_CONTENT`; no retry count and no scheduling eligibility |
| Background build fails on the initial execution and all three retries | Problem and evidence appear in the blocked repair queue while later eligible work continues | Job becomes `BLOCKED`; no certificate and no academic effect |
| Factory process or app exits mid-stage | Next startup reclaims the expired lease and validates the last checkpoint | Interrupted draft is resumed or restarted, never promoted implicitly |
| Interaction ledger not acknowledged | `Recording paused`; persistent local outbox retries idempotently | Lock/finalization blocked; no partial outcome |
| Animation certificate missing or stale | Problem absent from eligible queue | No attempt can start |
| Animation package hash or preflight mismatch | Restore last-known-good and requalify; otherwise show operational repair state | New study paused before attempt start; no text fallback and no academic result |
| Shadow-review disagreement | Evidence and both review IDs shown; one fresh isolated pair is available | `NEEDS_SECOND_REVIEW`; repeat disagreement becomes non-academic `SYSTEM_ERROR` and reschedules the same stage |
| Backup verification failure | Red operational alert | Completion gate remains false |

## 17. Verification strategy

Implementation follows test-driven development. Required test groups include:

### Calendar and budget

- every date, public-holiday override, capacity total, and milestone arithmetic from the master plan
- coach budget of 37.5 hours and remaining recovery reserve of 52.5 hours
- D365 events never enter the first-year 1,292-hour budget

### Selection

- exactly 500 unique canonical IDs
- exact 100/320/80 difficulty counts
- complete required-pattern coverage
- exact C-120 allocation
- NC250 spine contains no duplicates in the extension set
- every selected item has auditable scoring components
- P001–P080 satisfies the Array Systems prerequisite graph
- Wave 1 remains disabled at 79 of 80 qualified and becomes ready only at 80 of 80 with a current grader certificate
- no P081 introduction is generated before all P001–P080 coached encounters are complete
- a later problem is never introduced before its content certificate and prerequisite eligibility

### Bilingual content

- KO and EN records exist for every selected problem
- structured constraints, adapters, and tests share a semantic contract hash
- alternate language and identifying metadata remain inaccessible during blind attempts

### Coach and blind enforcement

- coach is available only for encounters 1–3
- only one accepted non-stale check is possible per coached encounter
- stale content-hash responses are discarded
- forbidden response content is suppressed
- no server endpoint can invoke coach at D3 or later
- post-submission review receives only locked artifacts

### Scheduler and mastery

- the nine encounters map to three coach sessions and six blind stages
- no universal D120 event is generated
- Final B cannot occur before D+90
- D30 and Final B must be unaided full-code passes
- C1, C2, and Final C gates remain separate from B state
- RETRY, FAIL, Red Queue, overdue ordering, and pause-new rules match the master plan

### SQLite history and weakness analytics

- finalizing an attempt is atomic and a forced failure leaves no partial academic outcome
- finalized attempts and locked artifacts cannot be overwritten through normal repositories
- correction, dismissal, resolution, and reopening actions append audit events
- timeline deltas compare only explicitly labeled, comparable attempts
- every weakness recommendation drills down to at least one source observation and attempt
- a manual cherry-pick never deletes, delays, or outranks required overdue work
- derived views reproduce the same result after export, restore, and migration
- foreign-key, uniqueness, CHECK-constraint, WAL backup, and integrity-check paths are tested

### Interaction ledger and reconstruction

- every defined editor, test, timer, focus, voice, coach, submit, review, reveal, animation, and post-verdict source action produces the correct versioned event
- raw pointer movement and activity outside the practice page are never captured
- batched editor operations preserve order and replay exactly across insert, delete, paste, undo, and redo
- reconstruction from each checkpoint reaches the next checkpoint's byte-identical code hash
- reconnect and duplicate delivery remain idempotent and event sequences have no silent gaps
- unacknowledged outbox events survive browser reload and block finalization until synchronized

### Code runner

- syntax errors, runtime errors, wrong answers, timeouts, output overflow, and successful tests
- process-group cleanup after timeout
- canonical artifacts are absent from the execution directory
- infrastructure errors do not become academic FAILs

### Voice

- microphone-unavailable fallback
- supported-format negotiation
- deterministic conversion-command construction
- Korean and English transcription routing
- transcript correction audit
- audio deletion and Final B/C retention policies

### Codex adapter

- exact subprocess argument construction
- JSON Schema parsing
- timeout, nonzero exit, rate limit, malformed result, pending retry, and successful review
- evaluation bundle excludes secrets and canonical solutions
- the primary and shadow reviewers receive no history, weakness labels, user identity, or prior verdict
- every material rubric finding has a resolvable code, test, transcript, or declaration evidence reference
- deterministic-test failure and assistance gates cannot be overridden by the recommendation
- stage-specific fixtures distinguish correct `PASS`, conceptually incomplete `RETRY`, incorrect `FAIL`, and low-confidence `NEEDS_SECOND_REVIEW`
- a fresh paired review remains mutually blind, and repeated disagreement produces non-academic `SYSTEM_ERROR` plus the same-stage replacement item
- coached encounters receive formative feedback but never an academic outcome

### Grader calibration

- all 0–4 anchors and encounter profile assignments are schema-validated and content-addressed
- the 72-case suite contains exactly 18 cases per profile and six expected outcomes of each class per profile
- qualification runs compute profile accuracy, hard-gate accuracy, false-PASS count, quadratic-weighted kappa, range-aware dimension-score error, evidence-reference validity, and repeated-run stability from stored case results
- threshold boundary fixtures prove that 16/18 profile agreement fails while 17/18 passes, any false PASS fails, kappa below 0.80 fails, error above 0.40 fails, and stability below 95% fails
- certificate binding and invalidation cover model metadata, CLI, prompt, schema, rubric, bundle builder, and calibration suite
- the 30-day rotating canary and 90-day complete renewal revoke on failure or expiry
- a missing, expired, revoked, or mismatched certificate cannot create a `CodexReview` academic recommendation and leaves the attempt pending

### Answer-animation qualification

- all 500 specs pass schema, semantic-contract, canonical-answer, test-manifest, Korean/English parity, and prohibited-content checks
- every main step and detail step replays deterministically forward, backward, restart, and language-switch paths
- every step performs one declared logical transition; complete code appears only in the final main step
- renderer traces and screenshots pass at 360, 768, and 1440 CSS-pixel widths, keyboard-only navigation, reduced motion, and screen-reader labeling
- the complete 500-spec sweep produces zero uncaught exceptions, console errors, missing assets, overflow failures, and external network requests
- specs cannot execute arbitrary JavaScript or reveal canonical data through an active blind endpoint
- certificate invalidation covers contract, answer, tests, player, application build, and compatibility changes
- atomic promotion, current-package corruption, last-known-good restoration, and dual-generation failure are exercised
- no problem can enter an eligible queue without a matching certificate; `WAVE_1_READY` requires P001–P080 at 80 of 80, while `CONTENT_500_COMPLETE` requires 500 of 500
- unlock is rejected before immutable review, permitted after every academic verdict and locked `COACHED_COMPLETE`, and animation viewing never changes mastery or scheduling

### Background animation factory

- application startup returns the study UI without waiting for the factory and resumes the earliest durable eligible P081–P500 job
- two concurrent application processes still execute at most one background stage through lease heartbeat, expiry, and reclaim tests
- editor activity, tests, voice conversion/transcription, every foreground Codex review, and calibration preempt background work; a preemption never increments `failure_count`
- `WAITING_CONTENT` wakes only from a matching dependency event, and the worker skips it while continuing with other eligible problems
- retry timing is exactly 1, 4, and 16 minutes; failure of the third retry produces `BLOCKED` and the next eligible job proceeds
- crashes at every stage checkpoint reconstruct the same target hashes and never produce a certificate without the full validation suite
- the header status derives from SQLite after reload and accurately reports qualified, active, waiting, retry, and blocked counts
- reaching 500 current certificates stops the worker; invalidating one bound hash re-enqueues exactly the affected package
- scheduler property tests prove that no factory state except current `QUALIFIED` can make a problem eligible

### Browser flows

- start and resume an attempt
- focused split layout at desktop and narrow widths
- coach indicator visible only when allowed
- blind reveal protections
- microphone and typed fallback paths
- immutable submission lock and verdict display
- interaction-ledger sync and `Recording paused` recovery
- post-verdict animation progression, detail expansion, previous/restart, language switch, keyboard navigation, and final-code reveal

### Backup and restore

- export and re-import preserve every timestamp and event
- retained audio and manifests restore correctly
- restore verification failure blocks the completion gate

## 18. Delivery decomposition

The product is delivered as independently testable slices. Development preview may use fixtures, but production learning remains disabled until P001–P080 reach 80-of-80 content qualification and the grader configuration is qualified:

1. **Foundation:** copy the supplied v2.0 master plan byte-for-byte to repository-root `PLAN.md`, then add repository configuration, calendar, immutable events, SQLite, migrations, and backups.
2. **Frozen curriculum:** authenticated curator import, scoring, validation, P001–P500, C-120, Array Depth Queue, bilingual cards, canonical answers, and deterministic test contracts.
3. **Practice evidence:** Midnight Focus UI, scheduler, CodeMirror editor, interaction outbox, checkpoints, reconstruction, and deterministic tests.
4. **Codex integration:** bounded coach sessions, the composite evidence-first reviewer, 0–4 rubrics, golden calibration suite, grader certificates, drift renewal, blind shadow review, pending-review recovery, leakage enforcement, and PASS/RETRY/FAIL policy.
5. **Voice:** browser capture, local conversion/transcription, transcript confirmation, retention, and fallback.
6. **Qualified explanations:** reusable animation player and primitives, P001–P080 first-wave certification, the idle-aware durable P081–P500 factory, later per-problem expansion to all 500, last-known-good recovery, server-side reveal gate, and view analytics.
7. **Certification and analytics:** B/C workflows, unseen and mocks, weakness analytics, risk projections, budget burn, and exports.
8. **Long-term maintenance:** D365 queue and second-year maintenance analytics.

The implementation-planning phase should produce one detailed plan per slice or tightly coupled group of slices. Each slice must leave a runnable, tested application state.

## 19. Acceptance criteria

The design is implemented when all of the following are demonstrably true:

- A validated, auditable set of 500 unique problems is frozen with exact difficulty and C-120 quotas.
- Every selected problem has semantically aligned original Korean and English blind cards.
- The user can complete three coached encounters and six server-enforced blind encounters.
- Coach output is bounded, asynchronous, hash-validated, and incapable of appearing during blind stages.
- Python tests run deterministically and remain the correctness oracle.
- Codex CLI returns schema-validated, evidence-cited post-submission review without direct API-key configuration, and its recommendation cannot override deterministic gates.
- Codex academic recommendations remain disabled until the exact grader configuration passes the 72-case qualification thresholds and has a current certificate; version drift or expiry returns locked attempts to pending review without an academic penalty.
- Final B, Final C, low-confidence, and conflicting cases receive a history-blind independent review; disagreement cannot create an academic result and unresolved repeat disagreement reschedules the same stage as `SYSTEM_ERROR`.
- Korean and English spoken explanations can be recorded and transcribed locally.
- Every meaningful practice action is durably ordered, acknowledged, and reconstructable from checkpoints; missing events prevent finalization.
- P001–P080 reach 80-of-80 bilingual content and animation qualification before the first production attempt, and all 80 complete the coached phase before a new P081 problem is introduced.
- P081–P500 can expand without blocking the first wave, but each problem remains unschedulable until its own content and prerequisites qualify; final content completion requires 500 of 500.
- Starting the app resumes exactly one durable P081–P500 animation worker, active practice preempts it without consuming a retry, failure of the initial execution and all three retries blocks only that job, and the UI exposes its evidence-backed progress without interrupting study.
- No active blind attempt can fetch answer-animation content, and every finalized verdict can open its pinned click-by-click explanation without changing the result.
- Current-package corruption restores a verified last-known-good package before study; loss of both qualified generations pauses new study rather than exposing a broken or text-only explanation.
- D30 and Final B certification gates match the master plan and cannot be bypassed.
- Today, Calendar, Problems, Certification, and Analytics expose debt, failures, and budget risk without hiding them.
- Every problem exposes its complete attempt timeline, comparable progress deltas, and evidence-backed open/resolved weakness history.
- The user can filter by weakness, pattern, difficulty, language, stage, last result, and due state, then create an auditable manual practice request.
- Every practice recommendation explains its priority and links to the attempts or observations that produced it.
- Export, backup, restore, and retained-audio verification pass.
- D365 maintenance is scheduled outside the first-year budget.
- The full automated test, type-check, lint, and browser-smoke suites pass with fresh output.

## 20. Non-goals

- Public hosting or multi-user accounts
- Executing untrusted third-party code safely
- Live per-keystroke Codex calls
- Recording raw pointer movement, operating-system activity, or unrelated browser behavior
- AI hints during blind certification
- Automated submission to NeetCode or treating an external NeetCode result as the local academic oracle
- Shipping 500 independent executable animation scripts or accepting text-only fallback for an unqualified animation
- Running an always-on animation generator that competes with active coding, tests, speech processing, or foreground Codex work
- Copying or redistributing NeetCode's protected explanations, videos, or test corpus
- Guaranteeing employment or guaranteeing human memory outcomes
- Adding a universal D120 full-code review
- Expanding beyond the frozen 500 before B-500 and C-120 completion
