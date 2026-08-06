# NeetCode 500 Bilingual Recall Dashboard Design

**Status:** Revised design, pending user review
**Decision date:** 2026-08-06
**Primary plan:** `/Users/devan/Desktop/neetcode_500_bilingual_master_plan_2026-08-06_v2.0.md`
**Product mode:** Local-first, single user, Python 3.12+, Asia/Seoul
**Readable HTML:** `docs/superpowers/specs/2026-08-06-neetcode-500-dashboard-design.html`

## 1. Product goal

Build a local HTML study application that selects and freezes 500 problems from NeetCode All, teaches them first in Korean and then in English, executes the user's Python solutions, records spoken reasoning, and uses Codex CLI for bounded coaching and post-submission review.

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
  ├─ deterministic Python test runner
  ├─ audio conversion and whisper.cpp adapter
  ├─ Codex CLI coach/reviewer adapter
  ├─ export, backup, and restore
  └─ static HTML/CSS/JavaScript assets
              │
              ▼
Local data
  ├─ tracker.sqlite3
  ├─ curated problem snapshot
  ├─ bilingual problem cards
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

The reviewer returns structured fields for correctness reasoning, invariant/state, complexity, boundary coverage, explanation quality, prohibited assistance, and a recommended `PASS`, `RETRY`, or `FAIL`. The backend owns the final transition and applies deterministic gates before accepting the recommendation.

If Codex is unavailable, unauthenticated, rate-limited, times out, or returns invalid JSON, the attempt becomes `PENDING_AI_REVIEW`. Its stage does not advance and it does not become `FAIL`. One automatic retry is permitted; further retry is manual.

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
- coach meter only for encounters 1–3
- post-lock Codex review and immutable verdict evidence

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
- bilingual card and source links outside blind attempts
- Array Depth Queue as a separate non-scheduled view

**Certification**

- eligible Final B queue
- C1, C2, and Final C queues
- controlled unseen reveal
- mock schedule
- pending AI-review queue

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
- `review_kind: COACH | POST_SUBMISSION`
- `input_bundle_hash`
- `schema_version`
- `codex_thread_id` when emitted
- `raw_result_json`
- rubric fields
- `recommended_result`
- `started_at`, `completed_at`, and `duration_seconds`
- `status: COMPLETE | PENDING | SYSTEM_ERROR`

### 12.7 State representation

B progress and C progress are derived separately from immutable events. They are not represented by a single mutable enum that forces C1/C2 to occur after B certification. Cached status fields may exist for display, but event history remains the source of truth.

### 12.8 `ScheduleItem` and `Attempt`

`ScheduleItem` represents work the curriculum requires. It stores `problem_id`, stage, due time in UTC, the Asia/Seoul study date, source, priority tier, current status, and the attempt that created the next item. An overdue item remains overdue; it is never silently moved or replaced.

`Attempt` is the central learning-history row. One row is created every time the user actually starts a problem, including coached encounters, blind encounters, recovery work, C certification, D365 maintenance, and optional user-selected drills.

Required fields are:

- `problem_id`, optional `schedule_item_id`, and optional `practice_request_id`
- monotonically increasing `sequence_no` per problem
- encounter, study mode, prompt language, and `FULL | COMPACT` format
- lifecycle status: `IN_PROGRESS | PENDING_AI_REVIEW | FINALIZED | ABANDONED | SYSTEM_ERROR`
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
- A public or multi-user deployment requires a separate threat model and a real untrusted-code sandbox; it is outside this design.

## 16. Error handling

| Failure | User-visible behavior | State effect |
|---|---|---|
| Codex unavailable or rate-limited | Review marked pending with retry action | No stage advance; no FAIL |
| Codex schema violation | One automatic retry, then manual queue | No stage advance; no FAIL |
| Coach response leaks forbidden content | Response suppressed and incident logged | Check remains available |
| Python timeout or memory limit | Deterministic failed test with captured reason | Normal rubric applies |
| Test-runner infrastructure failure | System-error banner and retry | No stage advance; no FAIL |
| Microphone denied | Typed explanation fallback | `voice_unavailable` recorded |
| Transcription failure | Replay, rerecord, or typed fallback | No academic penalty |
| Bilingual contract mismatch | Problem blocked from scheduling | Curator repair required |
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

### Browser flows

- start and resume an attempt
- focused split layout at desktop and narrow widths
- coach indicator visible only when allowed
- blind reveal protections
- microphone and typed fallback paths
- immutable submission lock and verdict display

### Backup and restore

- export and re-import preserve every timestamp and event
- retained audio and manifests restore correctly
- restore verification failure blocks the completion gate

## 18. Delivery decomposition

The product is delivered as independently testable slices:

1. **Foundation:** copy the supplied v2.0 master plan byte-for-byte to repository-root `PLAN.md`, then add repository configuration, calendar, immutable events, SQLite, migrations, and backups.
2. **Frozen curriculum:** authenticated curator import, scoring, validation, P001–P500, C-120, Array Depth Queue, and bilingual card schema.
3. **Blind practice:** Midnight Focus UI, scheduler, CodeMirror editor, deterministic tests, and PASS/RETRY/FAIL transitions.
4. **Codex integration:** bounded coach sessions, post-submission structured review, pending-review recovery, and leakage enforcement.
5. **Voice:** browser capture, local conversion/transcription, transcript confirmation, retention, and fallback.
6. **Certification and analytics:** B/C workflows, unseen and mocks, risk projections, budget burn, and exports.
7. **Long-term maintenance:** D365 queue and second-year maintenance analytics.

The implementation-planning phase should produce one detailed plan per slice or tightly coupled group of slices. Each slice must leave a runnable, tested application state.

## 19. Acceptance criteria

The design is implemented when all of the following are demonstrably true:

- A validated, auditable set of 500 unique problems is frozen with exact difficulty and C-120 quotas.
- Every selected problem has semantically aligned original Korean and English blind cards.
- The user can complete three coached encounters and six server-enforced blind encounters.
- Coach output is bounded, asynchronous, hash-validated, and incapable of appearing during blind stages.
- Python tests run deterministically and remain the correctness oracle.
- Codex CLI returns schema-validated post-submission review without direct API-key configuration.
- Korean and English spoken explanations can be recorded and transcribed locally.
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
- AI hints during blind certification
- Copying or redistributing NeetCode's protected explanations, videos, or test corpus
- Guaranteeing employment or guaranteeing human memory outcomes
- Adding a universal D120 full-code review
- Expanding beyond the frozen 500 before B-500 and C-120 completion
