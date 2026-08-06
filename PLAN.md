---
title_ko: "NeetCode 500 Python 1년 암기·체화 마스터 플랜"
title_en: "NeetCode 500 Python One-Year Memorization and Mastery Plan"
version: "2.0"
document_language: ["ko", "en"]
timezone: "Asia/Seoul"
start_date: "2026-08-06"
end_date: "2027-08-05"
result_review_date: "2027-08-06"
calendar_as_of: "2026-08-06"
python_version: "3.12+"
targets:
  level_b_certified: 500
  level_c_certified: 120
  unseen_transfer_attempts: 100
  live_mock_interviews: 12
  online_assessments: 8
  long_form_tests: 3
hours:
  normal_weekly_hours: 25
  monday_to_friday_each: 4
  saturday: 3
  sunday: 2
  named_public_holiday: 3
  scheduled_total: 1292
milestones:
  kickoff_finish: "2026-08-09"
  nominal_new_problem_finish: "2027-03-28"
  recovery_deadline: "2027-04-04"
  certification_deadline: "2027-08-05"
mastery_policy:
  all_500: "LEVEL_B"
  core_120: "LEVEL_C"
  final_b_min_days_after_introduction: 90
  final_b_preferred_window_days: [90, 150]
  use_separate_universal_d120_stage: false
---

# NeetCode 500 Python 1년 암기·체화 마스터 플랜  
# NeetCode 500 Python One-Year Memorization and Mastery Plan

> **문서의 목적 / Purpose**  
> 이 파일은 학습 계획과 Codex 구현 명세의 단일 기준 문서다. 한국어 설명 바로 아래에 영어 설명을 둔다. 표와 YAML 블록은 양쪽 언어에 공통으로 적용된다.  
> This file is the single source of truth for both the study program and the Codex implementation specification. English follows the Korean text. Tables and YAML blocks apply to both languages.

> **중요한 설계 결정 / Critical design decision**  
> 모든 문제에 별도의 `D120 전체 구현`과 `최종 전체 구현`을 중복으로 요구하지 않는다. 최종 B 인증을 최초 학습 후 최소 90일, 권장 90~150일 뒤의 장기 인출 시험으로 사용한다. 이 중복 제거가 1,292시간 안에 B-500, C-120, 초면 100문제를 함께 수행하기 위한 핵심이다.  
> A separate full-code `D120` review and another full-code final audit are not required for every problem. The final Level B audit itself is the long-term retrieval test, scheduled at least 90 days—and preferably 90 to 150 days—after first exposure. Removing this duplication is essential to fit B-500, C-120, and 100 unseen problems into 1,292 hours.

---

## 0. 결론과 목표 / Decision and Goals

### 한국어

**1년 안에 가능하지만 공격적인 목표다.** 기간은 2026년 8월 6일부터 2027년 8월 5일까지이며, 공휴일을 모두 3시간으로 계산하면 총 1,292시간이다.

완료 목표는 세 층으로 나눈다.

1. **필수 목표:** 500문제 전부 Level B 인증
2. **필수 심화 목표:** 핵심 120문제 Level C 인증
3. **외부 전이 검증:** 목록 밖 초면 100문제, 라이브 모의면접 12회, 90분 OA 8회, 5시간 장시간 시험 3회

`500문제를 한 번 봄`은 완료가 아니다. 2027년 8월 5일에 `B_CERTIFIED = 500`, `C_CERTIFIED = 120`, `REVIEW_DEBT = 0`이어야 1차 목표를 완료한 것으로 판정한다.

### English

**The one-year goal is feasible, but aggressive.** The program runs from August 6, 2026 through August 5, 2027. With every named public holiday set to three study hours, the total scheduled capacity is 1,292 hours.

Completion has three layers:

1. **Required:** certify all 500 problems at Level B
2. **Required advanced mastery:** certify 120 core problems at Level C
3. **External transfer validation:** 100 unseen problems outside the memorized set, 12 live mock interviews, eight 90-minute online assessments, and three five-hour long-form tests

Merely seeing all 500 problems once does not count. On August 5, 2027, the primary goal requires `B_CERTIFIED = 500`, `C_CERTIFIED = 120`, and `REVIEW_DEBT = 0`.

### 핵심 산식 / Core arithmetic

```text
Kickoff: 5 problems
Acquisition: 33 weeks × 15 problems = 495
Total new problems: 5 + 495 = 500

Final B audit: 16 weeks × 30 + final week × 20 = 500
Final C audit: 16 weeks × 7 + final week × 8 = 120
Unseen transfer: 16 weeks × 6 + final week × 4 = 100
```

---

## 1. 달력과 확보 시간 / Calendar and Available Hours

### 1.1 기본 시간 규칙 / Base study-hour policy

| 날짜 유형 / Day type | 공부시간 / Study hours |
|---|---:|
| 월요일~금요일 / Monday–Friday | 4시간 / 4h |
| 토요일 / Saturday | 3시간 / 3h |
| 일반 일요일 / Ordinary Sunday | 2시간 / 2h |
| 명칭이 있는 공휴일·명절 연휴·대체공휴일·추후 지정 임시공휴일 / Named public, holiday-period, substitute, or later-designated temporary holiday | 3시간 / 3h |

공휴일 3시간 규칙은 요일별 기본시간보다 우선한다. 따라서 평일 공휴일은 4시간에서 3시간으로 줄고, 공휴일과 겹친 일요일은 2시간에서 3시간으로 늘어난다. 토요일 공휴일은 그대로 3시간이다.

The three-hour holiday override takes precedence over the normal weekday schedule. A weekday holiday drops from four to three hours, a named holiday on Sunday rises from two to three hours, and a Saturday holiday remains at three hours.

### 1.2 공식 달력 기준 / Official calendar basis

- 2026년 공휴일: 우주항공청 「2026년 월력요항」 발표, 2025-06-30
- 2027년 공휴일: 우주항공청 「2027년 월력요항」 발표 및 우주항공청 공고 제2026-0078호, 2026-06-29
- 2027년에는 노동절과 제헌절 및 해당 대체공휴일이 공식 월력요항에 반영되어 있다.
- 임시공휴일이 추후 지정되면 대시보드는 해당 날짜를 180분으로 덮어쓰고 총시간과 완료예측을 재계산한다.

- 2026 holidays: Korea AeroSpace Administration, *2026 Calendar Essentials*, published June 30, 2025
- 2027 holidays: Korea AeroSpace Administration, *2027 Calendar Essentials* and Notice 2026-0078, published June 29, 2026
- The official 2027 calendar includes Labor Day, Constitution Day, and their applicable substitute holidays.
- If a temporary holiday is designated later, the dashboard must override that date to 180 minutes and recalculate total capacity and completion projections.

```text
Official sources:
https://www.kasa.go.kr/prog/bbsArticle/BBSMSTR_000000000010/view.do?bbsId=BBSMSTR_000000000010&nttId=B000000001860Pe2zT3
https://www.kasa.go.kr/prog/plcyBrf/brief/kor/sub01_01_04/view.do?plcyBrfNo=431
https://www.kasa.go.kr/bbs/BBSMSTR_000000000018/view.do?nttId=B000000003234Li6nD2
```

### 1.3 전체 시간 / Total capacity

```text
Base total without holiday overrides: 1,304 hours
Holiday-adjusted total:              1,292 hours
Net adjustment:                        -12 hours
Average per target problem:           2.584 hours
```

이 평균에는 최초 학습, 복습, 최종 B 인증, C 심화, 초면 검증, 모의시험, 기록과 실패 복구가 모두 포함된다.

This average includes first learning, spaced review, final Level B audits, Level C work, unseen validation, mock exams, logging, and failure recovery.

### 1.4 요일별 시간 / Hours by weekday

| 요일 / Day | 일수 / Days | 기본 일일시간 / Base daily hours | 최종 총시간 / Final total hours |
|---|---:|---:|---:|
| 월 / Mon | 52 | 4 | 202 |
| 화 / Tue | 52 | 4 | 207 |
| 수 / Wed | 52 | 4 | 207 |
| 목 / Thu | 53 | 4 | 210 |
| 금 / Fri | 52 | 4 | 204 |
| 토 / Sat | 52 | 3 | 156 |
| 일 / Sun | 52 | 2 | 106 |
| **합계 / Total** | **365** |  | **1292** |

### 1.5 월별 시간 / Monthly capacity

| 월 / Month | 포함 일수 / Days | 기본시간 / Base | 공휴일 적용 후 / Adjusted |
|---|---:|---:|---:|
| 2026-08 | 26 | 92h | 91h |
| 2026-09 | 30 | 108h | 106h |
| 2026-10 | 31 | 111h | 109h |
| 2026-11 | 30 | 106h | 106h |
| 2026-12 | 31 | 112h | 111h |
| 2027-01 | 31 | 109h | 108h |
| 2027-02 | 28 | 100h | 99h |
| 2027-03 | 31 | 112h | 111h |
| 2027-04 | 30 | 108h | 108h |
| 2027-05 | 31 | 109h | 106h |
| 2027-06 | 30 | 108h | 109h |
| 2027-07 | 31 | 111h | 110h |
| 2027-08 | 5 | 18h | 18h |
| **합계 / Total** | **365** | **1304h** | **1292h** |

### 1.6 계획 기간 내 공휴일 / Named holidays in the plan period

| 날짜 / Date | 요일 / Day | 공휴일 / Holiday | 기본 / Base | 적용 / Applied | 증감 / Delta |
|---|---|---|---:|---:|---:|
| 2026-08-15 | 토 / Sat | 광복절 / Liberation Day | 3h | 3h | +0h |
| 2026-08-17 | 월 / Mon | 광복절 대체공휴일 / Substitute holiday for Liberation Day | 4h | 3h | -1h |
| 2026-09-24 | 목 / Thu | 추석 연휴 / Chuseok holiday | 4h | 3h | -1h |
| 2026-09-25 | 금 / Fri | 추석 / Chuseok | 4h | 3h | -1h |
| 2026-09-26 | 토 / Sat | 추석 연휴 / Chuseok holiday | 3h | 3h | +0h |
| 2026-10-03 | 토 / Sat | 개천절 / National Foundation Day | 3h | 3h | +0h |
| 2026-10-05 | 월 / Mon | 개천절 대체공휴일 / Substitute holiday for National Foundation Day | 4h | 3h | -1h |
| 2026-10-09 | 금 / Fri | 한글날 / Hangeul Day | 4h | 3h | -1h |
| 2026-12-25 | 금 / Fri | 기독탄신일 / Christmas Day | 4h | 3h | -1h |
| 2027-01-01 | 금 / Fri | 신정 / New Year's Day | 4h | 3h | -1h |
| 2027-02-06 | 토 / Sat | 설날 연휴 / Seollal holiday | 3h | 3h | +0h |
| 2027-02-07 | 일 / Sun | 설날 / Seollal | 2h | 3h | +1h |
| 2027-02-08 | 월 / Mon | 설날 연휴 / Seollal holiday | 4h | 3h | -1h |
| 2027-02-09 | 화 / Tue | 설날 대체공휴일 / Substitute holiday for Seollal | 4h | 3h | -1h |
| 2027-03-01 | 월 / Mon | 3·1절 / Independence Movement Day | 4h | 3h | -1h |
| 2027-05-01 | 토 / Sat | 노동절 / Labor Day | 3h | 3h | +0h |
| 2027-05-03 | 월 / Mon | 노동절 대체공휴일 / Substitute holiday for Labor Day | 4h | 3h | -1h |
| 2027-05-05 | 수 / Wed | 어린이날 / Children's Day | 4h | 3h | -1h |
| 2027-05-13 | 목 / Thu | 부처님오신날 / Buddha's Birthday | 4h | 3h | -1h |
| 2027-06-06 | 일 / Sun | 현충일 / Memorial Day | 2h | 3h | +1h |
| 2027-07-17 | 토 / Sat | 제헌절 / Constitution Day | 3h | 3h | +0h |
| 2027-07-19 | 월 / Mon | 제헌절 대체공휴일 / Substitute holiday for Constitution Day | 4h | 3h | -1h |

### 1.7 단계별 시간 / Capacity by phase

| 단계 / Phase | 기간 / Dates | 일수 / Days | 시간 / Hours | 산출물 / Deliverable |
|---|---|---:|---:|---|
| Kickoff | 2026-08-06 ~ 2026-08-09 | 4 | 13h | 환경·목록·템플릿 구축 + P001–P005 / Set up the environment, freeze the lists and templates, and learn P001–P005 |
| Acquisition | 2026-08-10 ~ 2027-03-28 | 231 | 816h | 33주 × 15문제 = P006–P500 / 33 weeks × 15 new problems = P006–P500 |
| Recovery Buffer | 2027-03-29 ~ 2027-04-04 | 7 | 25h | 신규 부족·복습 부채·Red Queue 복구 / Clear new-problem deficit, review debt, and the Red Queue |
| Certification & Transfer | 2027-04-05 ~ 2027-08-01 | 119 | 422h | B-500 전수 인증 + C-120 + 초면 100 + 모의시험 / Certify B-500, C-120, 100 unseen problems, and mock exams |
| Final Closure | 2027-08-02 ~ 2027-08-05 | 4 | 16h | 마지막 실패 재시험·백업·최종 판정 준비 / Retest final failures, back up data, and prepare the final verdict |
| **Total** | 2026-08-06 ~ 2027-08-05 | **365** | **1292h** |  |


---

## 2. “외웠다”의 기준 / Definition of Mastery

`Level B`와 `Level C`는 문제 난이도가 아니라 **기억과 전이의 수준**이다. 시도 결과에는 같은 문자를 쓰지 않는다. 각 시도는 `PASS`, `RETRY`, `FAIL`로 기록한다.

`Level B` and `Level C` describe **mastery depth**, not problem difficulty. Attempt outcomes must not reuse those letters; each attempt is recorded as `PASS`, `RETRY`, or `FAIL`.

### 2.1 Level B — 면접형 재현 / Interview-ready recall

한 문제는 다음 조건을 모두 충족해야 `B_CERTIFIED`가 된다.

A problem becomes `B_CERTIFIED` only when every requirement below is met.

| 기준 / Criterion | Level B 통과 조건 / Passing condition |
|---|---|
| 단서 / Prompt | 제목과 카테고리를 숨기고 문제 설명과 제약만 제공 / Hide title and category; show only the statement and constraints |
| 패턴 인식 / Pattern recognition | Easy 60초, Medium 90초, Hard 120초 이내에 주 패턴 제시 / Identify the primary pattern within 60s, 90s, or 120s |
| 사고 설명 / Reasoning | brute force, 병목, 최적화 근거를 말로 설명 / Explain the brute-force approach, bottleneck, and optimization rationale |
| 구현 / Implementation | 힌트·이전 코드·AI·핵심 자동완성 없이 Python 전체 구현 / Write the complete Python solution without hints, prior code, AI, or core-logic autocomplete |
| 정확성 / Correctness | 직접 만든 경계조건을 포함한 테스트 통과 / Pass tests including self-generated edge cases |
| 원리 / Principle | 불변식, 재귀 반환 의미 또는 DP 상태를 설명 / Explain the invariant, recursive return meaning, or DP state |
| 복잡도 / Complexity | 시간·공간복잡도를 정확히 설명 / State correct time and space complexity |
| 시간 / Final time limit | Easy 15분, Medium 25분, Hard 45분 / 15m, 25m, or 45m |
| 간격 / Spacing | D30 이후 전체 구현 PASS 1회 + 최초 학습 90일 이후 Final B PASS 1회 / One full-code PASS at D30 or later plus a Final B PASS at least 90 days after introduction |
| 독립성 / Independence | 본 기억을 사용한 시도여야 하며 자료 열람 시 무효 / The attempt must come from memory; viewing solution material invalidates it |

Level B는 코드를 문자 단위로 복제하는 상태가 아니다. 문제 조건에서 알고리즘과 표준 Python 코드를 **재구성**하는 상태다.

Level B is not character-for-character code recitation. It is the ability to **reconstruct** the algorithm and canonical Python implementation from the problem conditions.

### 2.2 Level C — 변형 대응과 체화 / Transfer and adaptation

핵심 120문제는 Level B를 통과한 뒤 다음 조건까지 충족해야 `C_CERTIFIED`가 된다.

A core problem becomes `C_CERTIFIED` only after Level B and all conditions below are satisfied.

1. 서로 다른 변형 축 두 개 이상을 처리한다.  
   Handle at least two distinct variation axes.
2. 기존 풀이의 어떤 가정이 깨지는지 설명한다.  
   Explain which assumption in the original solution changes or breaks.
3. 상태, 불변식, 자료구조 또는 복잡도가 어떻게 달라지는지 설명한다.  
   Explain how the state, invariant, data structure, or complexity changes.
4. 최소 한 번은 변경된 조건의 코드를 직접 구현한다.  
   Implement at least one modified version in code.
5. Final B 직후 면접관식 follow-up을 받아 15분 안에 수정 방향을 제시하고, 필요한 경우 30분 안에 구현한다.  
   After Final B, answer an interviewer-style follow-up within 15 minutes and implement within 30 minutes when code is required.
6. C 세션은 최소 두 번이며 14일 이상 간격을 둔다.  
   Complete at least two Level C sessions separated by 14 or more days.

권장 변형 축:

Recommended variation axes:

- 단일 쿼리 → 다중 쿼리 / single query → multiple queries
- 정적 입력 → 스트리밍·온라인 업데이트 / static input → streaming or online updates
- 존재 여부 → 개수·최적값·경로 반환 / existence → count, optimum, or path reconstruction
- 추가 공간 허용 → O(1) 또는 제한 메모리 / extra space allowed → O(1) or constrained memory
- 중복·음수·삭제·삽입 추가 / add duplicates, negatives, deletion, or insertion
- 더 강한 시간복잡도 요구 / require a stronger time bound
- 배열 표현 → 트리·그래프·구간 표현 / array representation → tree, graph, or interval representation

### 2.3 시도 결과 / Attempt outcomes

| 결과 / Result | 정의 / Definition | 조치 / Action |
|---|---|---|
| `PASS` | 도움 없이 기준 충족 / Meets the stage criteria without help | 다음 단계로 이동 / Advance |
| `RETRY` | 접근은 맞으나 사소한 오류·시간초과·설명 누락 / Correct approach with minor bug, overrun, or missing explanation | 단계 유지, 다음 날 재시험 / Keep stage and retry next day |
| `FAIL` | 패턴 실패, 잘못된 알고리즘, 힌트·정답 열람, 핵심 원리 설명 실패 / Pattern failure, wrong algorithm, hint or solution viewed, or principle not understood | 재학습 후 D1로 복귀 / Relearn and reset to D1 |

### 2.4 최종 성공 판정 / Final success gates

#### 계획 완료 / Plan completion

```text
B_CERTIFIED:        500 / 500
C_CERTIFIED:        120 / 120
REVIEW_DEBT:          0
NEW_PROBLEM_DEFICIT:  0
RED_QUEUE:            0
```

#### 면접 준비 완료 / Interview-readiness validation

```text
UNSEEN_ATTEMPTS:       100 / 100
UNSEEN_FULL_SOLVES:    >= 75 / 100
UNSEEN_MEDIUM_SOLVES:  >= 50 / 65
UNSEEN_HARD_SOLVES:    >= 8 / 20
LIVE_MOCK_PASS:        >= 10 / 12
OA_FULL_PASS:          >= 6 / 8
LONG_FORM_PASS:        >= 2 / 3
```

#### 글로벌 빅테크 코딩 강한 기준 / Strong global-big-tech coding signal

```text
UNSEEN_FULL_SOLVES: >= 80 / 100
Last 5 live mocks:  >= 4 passes
Last 4 OAs:         >= 3 full passes
No repeated failure category dominating the final 30 days
```

이 외부 검증 수치는 취업을 보장하지 않는다. 알고리즘 라운드가 더 이상 주된 약점이 아닌지를 판단하기 위한 내부 기준이다.

These external metrics do not guarantee employment. They are internal evidence that algorithmic coding is no longer the primary weakness.


---

## 3. 문제 집합 설계 / Problem-set Design

### 3.1 500문제 목록 / The fixed 500-problem set

2026년 8월 9일까지 문제 순서와 ID를 고정한다.

Freeze problem IDs and curriculum order by August 9, 2026.

| 난이도 / Difficulty | 권장 수 / Target count |
|---|---:|
| Easy | 100 |
| Medium | 320 |
| Hard | 80 |
| **합계 / Total** | **500** |

규칙:

Rules:

- 고유 LeetCode 문제 ID 기준으로 중복을 제거한다. / Deduplicate by unique LeetCode problem ID.
- 동일 문제의 대안 풀이를 별도 문제로 세지 않는다. / Alternative solutions do not count as separate problems.
- 시작 뒤 새로 추가된 문제는 500 목록에 넣지 않는다. / Do not add newly published problems after the list is frozen.
- 삭제·접근불가 문제만 동일 난이도와 동일 패턴 문제로 교체한다. / Replace only deleted or inaccessible problems with equivalent difficulty and pattern.
- 문제 제목과 태그는 복습·인증 화면에서 기본적으로 숨긴다. / Hide titles and tags by default during reviews and audits.

### 3.2 핵심 C-120 배분 / Core C-120 allocation

| 패턴군 / Pattern family | C 문제 수 / Core count |
|---|---:|
| Arrays, Hashing, Prefix Sum | 7 |
| Two Pointers | 5 |
| Sliding Window | 6 |
| Stack, Monotonic Stack/Deque | 6 |
| Binary Search | 6 |
| Linked List | 5 |
| Intervals, Sweep Line | 5 |
| Heap, Top-K | 5 |
| Trees, BST | 9 |
| Trie, String Matching | 4 |
| Backtracking | 6 |
| Graph and Grid Traversal | 7 |
| Topological Sort, Union-Find | 6 |
| Shortest Path, MST | 6 |
| Greedy | 6 |
| 1D DP | 7 |
| 2D and Grid DP | 7 |
| Subsequence and String DP | 7 |
| Advanced DP, Bitmask, Tree DP | 6 |
| Bit, Math, Fenwick, Segment Tree | 4 |
| **합계 / Total** | **120** |

C 문제 선택 기준:

Selection criteria for the Level C core:

1. 해당 패턴의 대표성이 높다. / It is a strong representative of the pattern.
2. 조건 변경 시 풀이가 의미 있게 달라진다. / Meaningful solution changes occur under modified constraints.
3. 다른 문제에 재사용할 수 있는 불변식이나 상태 정의가 있다. / It contains a reusable invariant or state definition.
4. 단순 구현 암기보다 설명과 follow-up 가치가 높다. / It has high explanation and follow-up value beyond code recall.
5. 전체 120개가 특정 주제나 난이도에 몰리지 않는다. / The 120 are balanced across topics and difficulty.
6. 각 15문제 학습 주간에 C 후보를 원칙적으로 3~4개 배치하고, 한 주 최대 5개를 넘기지 않는다. / Place three to four Level C candidates in each 15-problem acquisition week and never more than five.
7. 인증 단계의 주간 C 목표를 맞추기 위해 Final B 후보를 고를 때 자격이 된 C 문제를 우선할 수 있다. / When selecting Final B candidates, the scheduler may prioritize eligible Level C problems to satisfy the weekly Level C quota.

### 3.3 초면 100문제 풀 / The 100-problem unseen pool

```text
Easy:   15
Medium: 65
Hard:   20
Total: 100
```

초면 문제는 500문제 목록과 중복되면 안 되며, 시험 전에는 문제 본문·제목·태그를 열지 않는다. 한 번 노출된 문제는 재시험용으로는 사용할 수 있지만 `unseen` 통계에는 다시 세지 않는다.

Unseen problems must not overlap with the memorized 500. Do not open their statements, titles, or tags before the test. After first exposure, they may be reused for retesting but never counted again as unseen.

### 3.4 권장 학습 순서 / Recommended curriculum order

| 문제 범위 / Range | 주제 / Topics | 수 / Count |
|---|---|---:|
| P001–P080 | Arrays, Hashing, Sorting, Prefix Sum, Two Pointers, Sliding Window | 80 |
| P081–P155 | Stack, Queue, Monotonic Structures, Binary Search, Linked List, Intervals | 75 |
| P156–P230 | Trees, BST, Heap, Trie, Tree DFS/BFS | 75 |
| P231–P305 | Backtracking, Grid Search, Graph DFS/BFS, Topological Sort, Union-Find | 75 |
| P306–P380 | Shortest Path, MST, Advanced Graph, Greedy | 75 |
| P381–P455 | 1D DP, 2D DP, Knapsack, Subsequence DP, String DP | 75 |
| P456–P500 | Interval DP, Tree DP, Bitmask, Math, Fenwick/Segment Tree, Mixed Hard | 45 |
| **합계 / Total** |  | **500** |

각 15문제 주간은 대체로 Easy 2~4, Medium 9~11, Hard 2~3으로 구성한다. Hard 두 문제를 같은 날 배정하지 않는다.

A typical 15-problem week contains two to four Easy, nine to eleven Medium, and two to three Hard problems. Never schedule two new Hard problems on the same day.


---

## 4. 연간 단계 / Yearly Phases

| 단계 / Phase | 기간 / Dates | 주요 목표 / Main objective |
|---|---|---|
| Kickoff | 2026-08-06 ~ 2026-08-09 | 시스템 구축, 500·C120·초면 풀 고정, P001–P005 / Set up the system, freeze the 500/C120/unseen pools, learn P001–P005 |
| Acquisition | 2026-08-10 ~ 2027-03-28 | 매주 신규 15개 + B 복습 + C1/C2 / 15 new per week plus Level B review and C1/C2 work |
| Recovery Buffer | 2027-03-29 ~ 2027-04-04 | 신규 부족·복습 부채·Red Queue를 0으로 / Clear all deficits, debt, and Red Queue |
| Certification & Transfer | 2027-04-05 ~ 2027-08-01 | B500 최종, C120 최종, 초면100, 모의시험 / Final B500, final C120, unseen100, and mock exams |
| Final Closure | 2027-08-02 ~ 2027-08-05 | 마지막 재시험, 데이터 백업, 결과 확정 / Final retests, backup, and verdict |
| Result Review | 2027-08-06 | 다음 400문제 진행 여부 결정 / Decide whether to proceed with the next 400 |

### 4.1 Kickoff 체크리스트 / Kickoff checklist

- [ ] P001–P500 문제 ID와 순서 고정 / Freeze P001–P500 IDs and order
- [ ] `core_c = true`인 120문제 지정 / Mark exactly 120 problems as `core_c = true`
- [ ] 초면 100문제 풀을 별도 파일에 잠금 / Lock the unseen pool in a separate file
- [ ] Python 표준 템플릿 저장소 생성 / Create the canonical Python template repository
- [ ] SQLite와 백업 경로 생성 / Create the SQLite database and backup path
- [ ] 공휴일 예외 22개 입력 / Enter the 22 named holiday exceptions
- [ ] P001–P005 D0 완료 / Complete D0 for P001–P005
- [ ] 자동 테스트로 총 1,292시간 확인 / Verify 1,292 total hours by automated test

### 4.2 신규 문제 주간 분배 / Weekly new-problem distribution

| 요일 / Day | 신규 / New | 역할 / Role |
|---|---:|---|
| 월 / Mon | 3 | 신규 + 예정 복습 / New learning plus due reviews |
| 화 / Tue | 2 | 복습 집중 / Review-heavy day |
| 수 / Wed | 3 | 신규 + 예정 복습 / New learning plus due reviews |
| 목 / Thu | 2 | 복습 집중 / Review-heavy day |
| 금 / Fri | 3 | 신규 + 약점 보완 / New learning plus weakness repair |
| 토 / Sat | 2 | 신규 마감 + Red Queue / Finish new quota plus Red Queue |
| 일 / Sun | 0 | 혼합 시험, 부채 청산, 주간 결산 / Mixed test, debt clearing, weekly review |
| **합계 / Total** | **15** |  |

공휴일 때문에 3문제 평일이 3시간으로 줄면 신규를 2개로 줄이고, 같은 주의 비공휴일 2문제 날을 3개로 올린다. 주간 15개를 유지하되 복습 부채가 생기면 신규보다 복습을 우선한다.

When a three-problem weekday becomes a three-hour holiday, reduce it to two new problems and raise a non-holiday two-problem day in the same week to three. Preserve the weekly target of 15 only when doing so does not create review debt.

### 4.3 정확한 신규 학습 달력 / Exact acquisition calendar

| 구간 / Week | 날짜 / Dates | 문제 범위 / Problems | 신규 / New | 누계 / Cumulative |
|---|---|---|---:|---:|
| K00 | 2026-08-06 ~ 2026-08-09 | P001–P005 | 5 | 5 |
| W01 | 2026-08-10 ~ 2026-08-16 | P006–P020 | 15 | 20 |
| W02 | 2026-08-17 ~ 2026-08-23 | P021–P035 | 15 | 35 |
| W03 | 2026-08-24 ~ 2026-08-30 | P036–P050 | 15 | 50 |
| W04 | 2026-08-31 ~ 2026-09-06 | P051–P065 | 15 | 65 |
| W05 | 2026-09-07 ~ 2026-09-13 | P066–P080 | 15 | 80 |
| W06 | 2026-09-14 ~ 2026-09-20 | P081–P095 | 15 | 95 |
| W07 | 2026-09-21 ~ 2026-09-27 | P096–P110 | 15 | 110 |
| W08 | 2026-09-28 ~ 2026-10-04 | P111–P125 | 15 | 125 |
| W09 | 2026-10-05 ~ 2026-10-11 | P126–P140 | 15 | 140 |
| W10 | 2026-10-12 ~ 2026-10-18 | P141–P155 | 15 | 155 |
| W11 | 2026-10-19 ~ 2026-10-25 | P156–P170 | 15 | 170 |
| W12 | 2026-10-26 ~ 2026-11-01 | P171–P185 | 15 | 185 |
| W13 | 2026-11-02 ~ 2026-11-08 | P186–P200 | 15 | 200 |
| W14 | 2026-11-09 ~ 2026-11-15 | P201–P215 | 15 | 215 |
| W15 | 2026-11-16 ~ 2026-11-22 | P216–P230 | 15 | 230 |
| W16 | 2026-11-23 ~ 2026-11-29 | P231–P245 | 15 | 245 |
| W17 | 2026-11-30 ~ 2026-12-06 | P246–P260 | 15 | 260 |
| W18 | 2026-12-07 ~ 2026-12-13 | P261–P275 | 15 | 275 |
| W19 | 2026-12-14 ~ 2026-12-20 | P276–P290 | 15 | 290 |
| W20 | 2026-12-21 ~ 2026-12-27 | P291–P305 | 15 | 305 |
| W21 | 2026-12-28 ~ 2027-01-03 | P306–P320 | 15 | 320 |
| W22 | 2027-01-04 ~ 2027-01-10 | P321–P335 | 15 | 335 |
| W23 | 2027-01-11 ~ 2027-01-17 | P336–P350 | 15 | 350 |
| W24 | 2027-01-18 ~ 2027-01-24 | P351–P365 | 15 | 365 |
| W25 | 2027-01-25 ~ 2027-01-31 | P366–P380 | 15 | 380 |
| W26 | 2027-02-01 ~ 2027-02-07 | P381–P395 | 15 | 395 |
| W27 | 2027-02-08 ~ 2027-02-14 | P396–P410 | 15 | 410 |
| W28 | 2027-02-15 ~ 2027-02-21 | P411–P425 | 15 | 425 |
| W29 | 2027-02-22 ~ 2027-02-28 | P426–P440 | 15 | 440 |
| W30 | 2027-03-01 ~ 2027-03-07 | P441–P455 | 15 | 455 |
| W31 | 2027-03-08 ~ 2027-03-14 | P456–P470 | 15 | 470 |
| W32 | 2027-03-15 ~ 2027-03-21 | P471–P485 | 15 | 485 |
| W33 | 2027-03-22 ~ 2027-03-28 | P486–P500 | 15 | 500 |


### 4.4 공휴일 조정 주간 / Holiday-adjusted acquisition weeks

| 주차 / Week | 공휴일 / Holidays | 월 / Mon | 화 / Tue | 수 / Wed | 목 / Thu | 금 / Fri | 토 / Sat | 일 / Sun | 합계 / Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| W02 | 2026-08-17 | 2 | 3 | 3 | 2 | 3 | 2 | 0 | 15 |
| W07 | 2026-09-24~26 | 3 | 3 | 3 | 2 | 2 | 2 | 0 | 15 |
| W09 | 2026-10-05, 10-09 | 2 | 3 | 3 | 3 | 2 | 2 | 0 | 15 |
| W20 | 2026-12-25 | 3 | 3 | 3 | 2 | 2 | 2 | 0 | 15 |
| W21 | 2027-01-01 | 3 | 3 | 3 | 2 | 2 | 2 | 0 | 15 |
| W27 | 2027-02-08~09 | 2 | 2 | 3 | 3 | 3 | 2 | 0 | 15 |
| W30 | 2027-03-01 | 2 | 3 | 3 | 2 | 3 | 2 | 0 | 15 |

토요일 공휴일은 기본 3시간과 같으므로 일별 신규 수를 바꾸지 않는다. 일요일과 겹친 설날은 신규를 추가하지 않고 복습 안정성에 추가 1시간을 사용한다.

Saturday holidays already match the normal three-hour schedule and do not change the daily new count. The named Seollal holiday on Sunday adds one hour for review stability rather than new learning.


---

## 5. 하루 운영 방식 / Daily Operating Model

### 5.1 3문제 평일, 4시간 / Three-new-problem weekday, four hours

```text
00:00–01:10  Due and overdue reviews                    70m
01:10–01:55  New problem 1                              45m
01:55–02:40  New problem 2                              45m
02:40–03:25  New problem 3                              45m
03:25–03:50  C1/C2 variation task or Red Queue          25m
03:50–04:00  Log, score, and generate next queue        10m
```

### 5.2 2문제 평일, 4시간 / Two-new-problem weekday, four hours

```text
00:00–01:40  Due, overdue, and Red Queue reviews        100m
01:40–02:25  New problem 1                               45m
02:25–03:10  New problem 2                               45m
03:10–03:45  C1/C2, failure repair, or template recall  35m
03:45–04:00  Log and next-queue generation               15m
```

### 5.3 토요일, 3시간 / Saturday, three hours

```text
00:00–01:00  Due reviews and Red Queue                   60m
01:00–01:45  New problem 1                               45m
01:45–02:30  New problem 2                               45m
02:30–02:50  Weekly pattern weakness drill               20m
02:50–03:00  Log                                         10m
```

### 5.4 일반 일요일, 2시간 / Ordinary Sunday, two hours

```text
00:00–00:50  Overdue and failed-problem reviews          50m
00:50–01:35  Tag-hidden mixed recall test                45m
01:35–01:50  Weekly metrics and failure analysis         15m
01:50–02:00  Generate next week's queue                  10m
```

### 5.5 공휴일, 3시간 / Named public holiday, three hours

```text
00:00–01:10  Due and overdue reviews                    70m
01:10–01:55  New/audit item 1                           45m
01:55–02:40  New/audit item 2                           45m
02:40–02:55  C task, failure repair, or compact recall  15m
02:55–03:00  Log                                         5m
```

일요일 공휴일에는 신규를 넣지 않고 혼합 시험과 Red Queue에 추가 1시간을 사용한다.

On a named Sunday holiday, do not add new problems; use the extra hour for mixed testing and Red Queue work.

### 5.6 최초 학습 시간 상한 / First-learning time caps

| 난이도 / Difficulty | 자력 시도 / Solo attempt | 해설 후 D0 포함 전체 / Total including D0 |
|---|---:|---:|
| Easy | 15~20분 | 25~35분 |
| Medium | 25~30분 | 40~50분 |
| Hard | 35~45분 | 65~80분 |

상한을 넘기면 더 오래 버티는 대신 힌트 또는 해설을 확인하고, 자료를 닫은 뒤 D0를 처음부터 재구성한다. 해설을 보며 타이핑한 코드는 D0로 인정하지 않는다.

When the cap is reached, inspect a hint or explanation rather than extending an unproductive struggle. Then close all material and reconstruct D0 from scratch. Typing while looking at the solution does not count as D0.


---

## 6. 복습과 기억 스케줄 / Review and Retrieval Schedule

### 6.1 B-500 복습 단계 / Level B review stages

| 단계 / Stage | 시점 / Timing | 방식 / Mode | 목표 / Goal |
|---|---:|---|---|
| D0 | 당일 / Same day | 전체 코드 / Full code | 해설을 닫고 대표 풀이 재구성 / Reconstruct after closing the explanation |
| D1 | +1일 | 전체 코드 / Full code | 기억에서 구현 / Implement from memory |
| D3 | +3일 | 3~5분 압축 인출 / 3–5m compact recall | Trigger, invariant/state, complexity, skeleton |
| D7 | +7일 | 전체 코드 / Full code | 제한시간 재현 / Timed reproduction |
| D14 | +14일 | 4~6분 압축 인출 / 4–6m compact recall | Boundaries, counterexample, critical loop |
| D30 | +30일 | 전체 코드 / Full code | 제목·태그 비공개 구현 / Title- and tag-hidden implementation |
| D60 | +60일 | 5~8분 압축 인출 / 5–8m compact recall | Explanation, alternative, likely follow-up |
| Final B | 최소 +90일 / At least +90d | 전체 코드 / Full code | 최종 Level B 인증 / Final Level B certification |

`Final B`는 가능하면 D+90~D+150에 배치한다. 별도의 보편적 D120 전체 구현은 생성하지 않는다. Final B가 장기기억 시험을 담당한다.

Schedule Final B within D+90 to D+150 whenever possible. Do not generate a universal separate full-code D120 event; Final B serves as the long-term retention test.

### 6.2 C-120 단계 / Level C stages

| 단계 / Stage | 권장 시점 / Timing | 작업 / Task |
|---|---|---|
| C1 | D30과 결합 / Merge with D30 | 첫 번째 변형의 가정 변화와 풀이 차이를 10~15분 분석 / Analyze the first variation and solution delta in 10–15m |
| C2 | D60과 결합 / Merge with D60 | 두 번째 변형을 15~25분 내 설계 또는 구현 / Design or implement a second variation in 15–25m |
| Final C | Final B 직후 / Immediately after Final B | 면접관식 follow-up, 코드 수정 포함 20~30분 / Interview-style follow-up, including code modification, 20–30m |

### 6.3 일일 큐 우선순위 / Daily queue priority

```text
1. Failed yesterday
2. Overdue Final B or Final C
3. Other overdue full-code reviews
4. Due Final B
5. Due D30 / D7 / D1 full-code reviews
6. Due C1 / C2
7. Due compact reviews D3 / D14 / D60
8. Planned new problems
9. Optional extra practice
```

### 6.4 Red Queue / Red Queue

다음 중 하나면 Red Queue에 들어간다.

Enter the Red Queue when any condition below occurs.

- 30일 안에 `FAIL` 두 번 / Two `FAIL` results within 30 days
- D30 이후 `FAIL` / A `FAIL` at D30 or later
- 같은 오류 유형 세 번 / The same failure type occurs three times
- 코드는 나오지만 불변식·상태를 설명하지 못함 / Code is recalled but the invariant or state cannot be explained
- 원본 문구가 바뀌면 패턴을 못 찾음 / Pattern recognition fails when wording changes

재시험:

Retest sequence:

```text
Relearn today → +1d → +3d → +7d → +14d → +30d
```

### 6.5 신규 중단 조건 / Conditions that pause new learning

```text
Review debt > 15
or New problem deficit > 5
or D30 pass rate < 75% over the latest 30 attempts
or Red Queue > 30
or Planned study time missed by > 8 hours over rolling 14 days
```

조건이 해소될 때까지 신규를 중단한다. 신규 숫자를 유지하면서 복습 부채를 숨기는 것은 허용하지 않는다.

Pause new learning until the condition is cleared. Maintaining the new-problem count while hiding review debt is not allowed.


---

## 7. 인증·전이 단계 / Certification and Transfer Phase

2027년 4월 5일부터 신규 500 목록의 학습은 중단한다. 17주 동안 매주 B 인증, C 심화, 초면 문제를 동시에 수행한다.

Stop acquiring new problems from the memorized 500 on April 5, 2027. For 17 weeks, run Level B audits, Level C follow-ups, and unseen transfer tests in parallel.

### 7.1 최종 문제 선택 규칙 / Final selection rules

1. Final B는 최초 학습 후 90일이 지난 문제만 선택한다.  
   Select only problems at least 90 days past introduction.
2. 가능한 한 D+90~D+150 범위의 문제를 먼저 선택한다.  
   Prioritize problems within the D+90 to D+150 window.
3. 동일 주차에 난이도와 패턴을 층화해 배치한다.  
   Stratify difficulty and pattern within each week.
4. 제목과 태그는 숨긴다.  
   Hide titles and tags.
5. 동일 문제의 Final B와 Final C는 같은 세션에서 연속 수행할 수 있다.  
   Final B and Final C for the same problem may run consecutively in one session.
6. 고정 난수 시드 `20260806`을 사용하되, 90일 자격 제약을 먼저 적용한다.  
   Use fixed seed `20260806`, but apply the 90-day eligibility constraint first.

### 7.2 주간 기본량 / Default weekly load

```text
Final B audits: 30
Final C follow-ups: 7
Unseen problems: 6
Plus scheduled live mock, OA, or long-form test
```

마지막 주는 B 20, C 8, 초면 4로 조정한다.

The final week uses 20 Level B audits, eight Level C follow-ups, and four unseen problems.

### 7.3 17주 인증 달력 / Seventeen-week certification calendar

| 주차 / Week | 날짜 / Dates | Final B | Final C | Unseen | 추가 시험 / Additional assessment |
|---|---|---:|---:|---:|---|
| A01 | 2027-04-05 ~ 2027-04-11 | 30 | 7 | 6 | 45m live mock |
| A02 | 2027-04-12 ~ 2027-04-18 | 30 | 7 | 6 | 45m live mock |
| A03 | 2027-04-19 ~ 2027-04-25 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A04 | 2027-04-26 ~ 2027-05-02 | 30 | 7 | 6 | 45m live mock |
| A05 | 2027-05-03 ~ 2027-05-09 | 30 | 7 | 6 | 5h long-form test |
| A06 | 2027-05-10 ~ 2027-05-16 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A07 | 2027-05-17 ~ 2027-05-23 | 30 | 7 | 6 | 45m live mock |
| A08 | 2027-05-24 ~ 2027-05-30 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A09 | 2027-05-31 ~ 2027-06-06 | 30 | 7 | 6 | 90m OA |
| A10 | 2027-06-07 ~ 2027-06-13 | 30 | 7 | 6 | 45m live mock |
| A11 | 2027-06-14 ~ 2027-06-20 | 30 | 7 | 6 | 5h long-form test |
| A12 | 2027-06-21 ~ 2027-06-27 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A13 | 2027-06-28 ~ 2027-07-04 | 30 | 7 | 6 | 45m live mock |
| A14 | 2027-07-05 ~ 2027-07-11 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A15 | 2027-07-12 ~ 2027-07-18 | 30 | 7 | 6 | 45m live mock + 90m OA |
| A16 | 2027-07-19 ~ 2027-07-25 | 30 | 7 | 6 | 5h long-form test |
| A17 | 2027-07-26 ~ 2027-08-01 | 20 | 8 | 4 | 90m OA |
| **합계 / Total** |  | **500** | **120** | **100** | **12 live + 8 OA + 3 long-form** |


### 7.4 일반 인증 주의 일별 기본안 / Default daily layout in a certification week

| 요일 / Day | Final B | Final C | Unseen | 비고 / Notes |
|---|---:|---:|---:|---|
| 월~금 / Mon–Fri | 4/day | 1/day on selected days | 1/day on selected days | 난이도 가중치로 재배치 / Rebalance by difficulty weight |
| 토 / Sat | 6 | 1 | 1 | Red Queue 포함 / Include Red Queue |
| 일 / Sun | 4 | 1 | 0 | 주간 실패 재시험 / Weekly retests |
| **주간 / Weekly** | **30** | **7** | **6** |  |

문제 수는 기본값이다. Hard가 많은 날은 다음 가중치로 같은 주 안에서 재배치한다.

Counts are defaults. Rebalance within the same week using these weights when Hard problems cluster.

```text
Final B weight: Easy 1.0, Medium 1.7, Hard 3.0
Unseen weight:  Easy 1.0, Medium 1.8, Hard 3.2
```

### 7.5 초면 문제 평가 / Unseen-problem scoring

`FULL_SOLVE` 조건:

A result counts as `FULL_SOLVE` only when all conditions below are met.

- 시간 안에 올바른 알고리즘과 실행 가능한 코드 완성 / Complete the correct algorithm and executable code within time
- 핵심 테스트 통과 / Pass core tests
- 복잡도 설명 / Explain complexity
- 치명적인 힌트 없음 / No decisive hint

시간:

Time limits:

```text
Easy:   15 minutes
Medium: 30 minutes
Hard:   50 minutes
```

Hard에서 완전 구현은 실패했지만 올바른 상태·불변식·복잡도와 핵심 의사코드를 제시하면 `STRONG_PARTIAL`로 별도 기록한다. `STRONG_PARTIAL`은 75/100 또는 80/100 완전 풀이 수에는 포함하지 않는다.

For a Hard problem, a correct state definition, invariant, complexity, and core pseudocode without complete implementation is recorded separately as `STRONG_PARTIAL`. It does not count toward the 75/100 or 80/100 full-solve gates.

### 7.6 모의시험 통과 기준 / Mock-exam pass criteria

| 시험 / Assessment | 구성 / Format | PASS 기준 / Passing gate |
|---|---|---|
| Live mock | 45분, Medium + follow-up, 말하면서 코딩 / 45m, Medium plus follow-up, think aloud | 작은 힌트 1회 이하, 실행 코드, 테스트·복잡도 설명 / At most one small hint, executable code, tests and complexity |
| OA | 90분, 2문제 / 90m, two problems | 두 문제 핵심 테스트 완전 통과 / Both problems pass core tests |
| Long-form | 5시간, 5문제 혼합 / 5h, five mixed problems | 최소 3문제 완전 통과, 한 문제에 90분 초과 금지 / At least three full solves; no single problem over 90m |


---

## 8. 1,292시간 예산 / The 1,292-Hour Budget

이 시간표는 단순한 날짜 합계가 아니라 작업별 예산까지 맞춘다.

This is not only a calendar sum; it also allocates capacity by work type.

| 작업 / Workstream | 시간 / Hours | 설명 / Notes |
|---|---:|---|
| 최초 학습과 D0 / First learning and D0 | 390 | Easy/Medium/Hard 가중 평균 / Weighted difficulty average |
| B 복습 D1~D60 / Level B reviews D1–D60 | 408 | 전체 코드와 압축 인출 혼합 / Mix of full-code and compact recall |
| Final B 500 / Final B audits | 188 | 난이도 가중 평균 / Difficulty-weighted average |
| C1, C2, Final C 120 / Level C work | 96 | 문제당 평균 48분 추가 / Average 48 extra minutes per core problem |
| 초면 100 / 100 unseen problems | 48 | 문제당 평균 28.8분 / Average 28.8 minutes |
| 모의시험 / Mock assessments | 36 | 12 live + 8 OA + 3 long-form |
| 기록·백업·주간 분석 / Logging, backup, analysis | 36 | 하루 평균 약 6분 / Roughly six minutes per day |
| 실패 복구 예비시간 / Failure-recovery reserve | 90 | Red Queue, 결석, 과도한 Hard / Red Queue, missed days, hard-problem overruns |
| **합계 / Total** | **1,292** |  |

세부 산정 기준:

Detailed budgeting assumptions:

```text
First learning + D0:
  100 Easy × 30m + 320 Medium × 45m + 80 Hard × 75m = 390h

B reviews D1–D60:
  D1 80h + D3 25h + D7 100h + D14 33h + D30 125h + D60 45h = 408h

Final B:
  100 Easy × 12m + 320 Medium × 22m + 80 Hard × 38m = 188h

Mock assessments:
  12 × 45m + 8 × 90m + 3 × 300m = 36h
```

이 값은 개별 문제의 강제 제한이 아니라 전체 포트폴리오 예산이다. 한 Hard 문제가 예산을 넘을 수 있지만, 반복적으로 초과하면 예측 완료일과 위험 상태에 반영한다.

These are portfolio-level budgets, not rigid limits for each individual problem. A particular Hard problem may exceed its envelope, but repeated overruns must affect projections and risk status.

대시보드는 각 예산의 실제 소비량을 보여줘야 한다. `최초 학습 + B복습`이 예상보다 빠르게 예산을 소모하면, 500개 숫자를 억지로 유지하지 말고 위험 상태를 표시한다.

The dashboard must expose actual consumption against each budget. If first learning and Level B reviews burn capacity faster than planned, it must flag risk instead of silently forcing the 500-problem count.

### 8.1 주간 상태 / Weekly health states

#### Green

```text
Review debt <= 5
New problem deficit <= 2
Rolling D30 pass rate >= 85%
Red Queue <= 15
Rolling 14-day hour deficit <= 3h
```

#### Yellow

```text
Review debt 6–15
or New problem deficit 3–5
or Rolling D30 pass rate 75–84%
or Red Queue 16–30
or Rolling 14-day hour deficit 3–8h
```

조치: 다음 신규 2개 슬롯을 복습으로 전환하고, 일요일을 전부 복구에 사용한다.

Action: convert the next two new-problem slots to review and use Sunday entirely for recovery.

#### Red

```text
Review debt > 15
or New problem deficit > 5
or Rolling D30 pass rate < 75%
or Red Queue > 30
or Rolling 14-day hour deficit > 8h
```

조치: 신규를 중단하고 예측 완료일을 재계산한다. 2027년 2월 28일 이후 Red 상태가 7일 넘게 지속되면 `ONE_YEAR_TARGET_AT_RISK = true`로 표시한다.

Action: pause new learning and recalculate the projected completion date. If Red persists for more than seven days after February 28, 2027, set `ONE_YEAR_TARGET_AT_RISK = true`.


---

## 9. Python 표준화 / Python Standardization

500개의 독립 코드를 외우지 않는다. 약 40~60개의 표준 템플릿과 500개의 문제별 차이를 기억한다.

Do not memorize 500 independent code blobs. Memorize roughly 40 to 60 canonical templates plus the problem-specific differences across 500 problems.

필수 템플릿:

Required templates:

- Hash Map, Counter, Prefix Sum, Difference Array
- Two Pointers, Fixed and Variable Sliding Window
- Stack, Queue, Deque, Monotonic Stack and Deque
- Binary Search on index and answer
- Linked-list reverse, dummy-node patterns, fast/slow pointers
- Heap, Top-K, merge-k
- Tree DFS/BFS, BST, LCA
- Trie and string search
- Backtracking: choose → recurse → unchoose
- Graph DFS/BFS, topological sort, Union-Find
- Dijkstra, 0-1 BFS, Bellman-Ford, Floyd-Warshall, MST
- 1D/2D DP, knapsack, LIS, LCS, string DP
- Interval DP, tree DP, bitmask DP
- Fenwick Tree and Segment Tree

각 템플릿에서 함수 시그니처, 변수명, 구간 표현, 방문 처리 시점, 종료 조건과 반환값 의미를 고정한다. 예외가 필요한 문제만 차이를 카드에 기록한다.

For every template, standardize function signatures, variable names, interval conventions, visitation timing, termination rules, and return-value meaning. Record only genuine exceptions in the problem card.

### 9.1 문제 카드 / Problem card

```markdown
# P001 — Problem Title

- LeetCode ID:
- Difficulty:
- Primary Pattern:
- Secondary Pattern:
- Mastery Target: B | C
- Canonical Solution Version:

## Trigger
What wording and constraints activate this pattern?

## Brute Force and Bottleneck
What is the simplest approach, and why is it too slow or too large?

## Invariant / State
What remains true, or what exactly does the state represent?

## Transition
How does the algorithm move to the next state?

## Why Correct
Why does the solution guarantee the answer?

## Complexity
- Time:
- Space:

## Boundaries
- Empty input:
- Length one:
- Duplicates:
- Negative values:
- Maximum input:

## Main Trap
My most likely failure point.

## Minimal Counterexample
The smallest input that breaks the wrong approach.

## Python Skeleton
Only the critical reusable structure.

## C Variations
- Variation 1:
- Broken assumption:
- Solution delta:
- Variation 2:
- Broken assumption:
- Solution delta:
```

### 9.2 AI와 자동완성 / AI and autocomplete

허용:

Allowed:

- 최초 자력 시도 후 해설 비교 / Compare explanations after the first solo attempt
- 테스트 생성과 실패 원인 분석 / Generate tests and analyze failures
- 대표 풀이 안정성 검토 / Review canonical-solution stability
- 카드 초안 생성 / Draft problem cards

금지:

Forbidden:

- D1 이후 기억 시험 중 코드 생성 / Code generation during retrieval from D1 onward
- Final B, Final C, unseen, mock exams / Final B, Final C, unseen tests, and mocks
- 이전 답안을 보며 타이핑 / Typing while viewing prior code
- 핵심 알고리즘 자동완성 / Autocomplete that generates core algorithm logic

자료를 보는 순간 해당 시도는 `PASS`가 될 수 없다.

Once solution material is viewed, the attempt cannot receive `PASS`.


---

## 10. Codex용 로컬 대시보드 명세 / Local Dashboard Specification for Codex

### 10.1 제품 목표 / Product goal

한 명이 로컬에서 사용하는 학습 운영 도구를 만든다. 핵심은 화려한 UI가 아니라 다음이다.

Build a local, single-user study operations tool. The priorities are not visual polish but the following:

1. 오늘 해야 할 일을 자동 계산 / Automatically calculate today's work
2. 복습 부채와 실패를 숨기지 않음 / Never hide review debt or failures
3. B-500과 C-120을 별도 추적 / Track B-500 and C-120 separately
4. 공휴일과 실제 공부시간을 반영해 완료일 예측 / Forecast completion from holidays and actual logged time
5. 초면 문제와 모의시험을 암기 목록과 분리 / Keep unseen tests and mocks separate from the memorized set

### 10.2 권장 MVP 스택 / Recommended MVP stack

```text
Python 3.12+
Streamlit
SQLite
SQLModel or SQLAlchemy
Alembic
pytest
Ruff
mypy
CSV / JSON / Markdown export
```

전제:

Constraints:

- local-first and single-user
- no login
- core functions work offline
- one SQLite file can back up all structured data
- Markdown solution cards remain Git-friendly files
- all date calculations use Asia/Seoul

### 10.3 권장 저장소 구조 / Suggested repository structure

```text
neetcode-500-dashboard/
├── README.md
├── PLAN.md                         # this file
├── pyproject.toml
├── app.py
├── src/
│   └── neetcode_tracker/
│       ├── calendar_engine.py
│       ├── scheduler.py
│       ├── mastery.py
│       ├── projections.py
│       ├── models.py
│       ├── repositories.py
│       ├── services.py
│       └── ui/
│           ├── today.py
│           ├── calendar.py
│           ├── problems.py
│           ├── reviews.py
│           ├── certification.py
│           └── analytics.py
├── data/
│   ├── tracker.sqlite3
│   ├── problems.csv
│   ├── unseen_pool.csv
│   └── holidays.yaml
├── cards/
│   └── P001-problem-slug.md
├── tests/
│   ├── test_calendar_engine.py
│   ├── test_scheduler.py
│   ├── test_mastery.py
│   ├── test_projections.py
│   └── test_import_export.py
└── backups/
```

### 10.4 데이터 모델 / Data model

#### Problem

```text
id: str                         # P001..P500
leetcode_id: int
slug: str
title: str
difficulty: EASY | MEDIUM | HARD
primary_pattern: str
secondary_pattern: str | null
curriculum_order: int
mastery_target: B | C
core_c: bool
canonical_solution_path: str
introduced_on: date | null
current_stage: UNSEEN | D0 | D1 | D3 | D7 | D14 | D30 | D60 | B_READY | B_CERTIFIED | C1 | C2 | C_CERTIFIED | RED
next_review_on: date | null
last_reviewed_on: date | null
b_certified_on: date | null
c_certified_on: date | null
fail_count: int
red_queue: bool
```

#### ReviewEvent

```text
id: int
problem_id: str
kind: D0 | D1 | D3 | D7 | D14 | D30 | D60 | FINAL_B | C1 | C2 | FINAL_C | RED_RETEST
scheduled_date: date
started_at: datetime | null
completed_at: datetime | null
result: PASS | RETRY | FAIL | null
duration_seconds: int | null
hint_used: bool
code_viewed: bool
ai_used: bool
tests_passed: bool
complexity_explained: bool
invariant_explained: bool
boundary_cases_count: int
pattern_recognition_seconds: int | null
failure_type: str | null
notes: str | null
```

#### VariationEvent

```text
id: int
problem_id: str
review_event_id: int
variation_axis: str
changed_condition: str
broken_assumption: str
solution_delta: str
code_required: bool
code_passed: bool
duration_seconds: int
result: PASS | RETRY | FAIL
```

#### UnseenAttempt

```text
id: int
external_problem_id: str
source: str
difficulty: EASY | MEDIUM | HARD
attempted_on: date
first_exposure: bool
result: FULL_SOLVE | STRONG_PARTIAL | FAIL
duration_seconds: int
hint_count: int
tests_passed: bool
notes: str | null
```

#### MockSession

```text
id: int
kind: LIVE_45 | OA_90 | LONG_300
scheduled_date: date
completed_on: date | null
result: PASS | FAIL | null
problems_attempted: int
problems_solved: int
notes: str | null
```

#### StudyDay

```text
date: date
planned_minutes: int
actual_minutes: int
is_named_public_holiday: bool
holiday_name_ko: str | null
holiday_name_en: str | null
new_target: int
new_completed: int
reviews_due: int
reviews_completed: int
status: GREEN | YELLOW | RED
notes: str | null
```

#### CalendarException

```text
date: date
kind: PUBLIC_HOLIDAY | SUBSTITUTE_HOLIDAY | TEMPORARY_HOLIDAY | MANUAL_OVERRIDE
name_ko: str
name_en: str
planned_minutes: int            # default 180
source: str
source_as_of: date
active: bool
```

### 10.5 필수 화면 / Required screens

#### Today

- 오늘 계획시간과 실제시간 / planned and actual minutes
- 공휴일 여부 / holiday status
- 우선순위가 적용된 오늘 큐 / priority-sorted daily queue
- 신규, B복습, C복습, unseen, mock 분리 / separate new, B, C, unseen, and mock work
- 타이머와 PASS/RETRY/FAIL 입력 / timer and outcome input
- 남은 예상시간 / estimated time remaining

#### Calendar

- 일별 계획·실제시간 / planned and actual time per day
- 공휴일 180분 override / holiday override
- 신규·복습·실패·인증 수 / new, review, failure, and certification counts
- Green/Yellow/Red / status color

#### Problems

- 500문제 목록 / all 500 problems
- B/C 목표, 현재 단계, 다음 복습일 / mastery target, stage, next review
- 패턴·난이도·상태 필터 / filters
- 문제 카드 링크 / card link

#### Certification

- Final B 자격 문제: `introduced_on + 90 days <= today` / eligible Final B problems
- C1/C2/Final C 큐 / Level C queues
- 초면 문제 잠금 해제 / controlled unseen-pool reveal
- 모의시험 일정 / mock schedule

#### Analytics

- Seen, D30, B-certified, C-certified / progress funnels
- 패턴별·난이도별 통과율 / pass rates by pattern and difficulty
- 실패 유형 / failure categories
- 평균 구현시간과 패턴 인식시간 / average implementation and recognition time
- 시간예산 소비량 / budget burn
- 예상 신규 종료일과 최종 인증일 / projected completion dates
- unseen and mock results / external validation metrics

### 10.6 스케줄러 규칙 / Scheduler rules

```text
1. Generate due reviews from stage transitions.
2. Never create duplicate events for the same problem, kind, and date.
3. Do not generate a universal full-code D120 event.
4. Final B eligibility starts at introduced_on + 90 days.
5. Prefer Final B candidates between D+90 and D+150.
6. A RETRY keeps the current stage and creates a next-day event.
7. A FAIL creates a relearn task and resets the B path to D1.
8. Two FAILs within 30 days set red_queue = true.
9. Final C requires B_CERTIFIED and completed C1 and C2.
10. New work is always lower priority than overdue review.
11. Named holidays override planned_minutes to 180.
12. Missed events remain overdue; never silently delete or shift history.
13. Recalculate projections whenever hours, holidays, or outcomes change.
```

### 10.7 완료일 예측 / Projection model

최소한 다음 두 예측을 분리한다.

Maintain at least two separate projections.

```text
projected_new_problem_finish_date
projected_b500_c120_certification_date
```

예측에는 최근 28일 실제 처리속도, 남은 시간예산, 난이도 가중치, Red Queue, 미완료 C 작업, 공휴일을 반영한다.

The forecast must incorporate the rolling 28-day throughput, remaining hour budget, difficulty weights, Red Queue, unfinished Level C work, and holiday overrides.

### 10.8 필수 자동 테스트 / Minimum automated tests

```text
- 2026-08-06 is Thursday in Asia/Seoul.
- The plan has 365 study days through 2027-08-05 inclusive.
- Base capacity is 1,304 hours.
- Holiday-adjusted capacity is 1,292 hours.
- 2026-08-17 is 180 minutes, not 240.
- 2027-02-07 is 180 minutes, not 120.
- 2027-05-03 is the substitute holiday for Labor Day and is 180 minutes.
- 2027-07-19 is the substitute holiday for Constitution Day and is 180 minutes.
- Kickoff 5 + 33 × 15 equals 500.
- Final B: 16 × 30 + 20 equals 500.
- Final C: 16 × 7 + 8 equals 120.
- Unseen: 16 × 6 + 4 equals 100.
- No Final B event is scheduled before introduction + 90 days.
- No universal D120 full-code event is generated.
- RETRY does not advance the stage.
- FAIL resets the B path to D1 and schedules relearning.
- Final C cannot pass before B, C1, and C2 pass.
- Overdue reviews sort before new problems.
- Export and re-import preserve every event and timestamp.
```

### 10.9 구현 단계 / Suggested implementation phases

- [ ] **Phase 1:** repository, configuration, database, and calendar engine
- [ ] **Phase 2:** 500-problem and holiday import with validation
- [ ] **Phase 3:** review-state machine and daily scheduler
- [ ] **Phase 4:** Today, Calendar, and Problems screens
- [ ] **Phase 5:** B/C certification and variation-event workflow
- [ ] **Phase 6:** unseen pool and mock-session workflow
- [ ] **Phase 7:** analytics, risk states, and projections
- [ ] **Phase 8:** export, backup, restore, documentation, and end-to-end tests

각 단계는 실패하는 테스트를 먼저 만들고, 최소 구현으로 통과시킨 뒤 커밋한다.

For each phase, write a failing test first, implement the minimum change to pass it, verify the full test suite, and commit.


---

## 11. Codex에 바로 전달할 지시문 / Ready-to-Paste Codex Instruction

### 한국어

```text
이 저장소의 PLAN.md를 단일 기준 문서로 사용하라.

목표는 2026-08-06부터 2027-08-05까지 NeetCode 500문제를 Level B로,
그중 핵심 120문제를 Level C로 관리하고, 초면 100문제와 모의시험을 추적하는
로컬 단일 사용자 대시보드를 만드는 것이다.

PLAN.md의 날짜, 시간, 공휴일, B/C 정의, 문제 수, 상태 전이, 완료 기준을 임의로 바꾸지 마라.
먼저 저장소를 조사한 뒤 다음 순서로 진행하라.

1. PLAN.md 요구사항을 구현 가능한 작업으로 분해한 상세 implementation plan을 작성한다.
2. calendar engine과 데이터 모델부터 테스트 주도로 구현한다.
3. 매 작업 뒤 테스트, 타입 검사, lint를 실행한다.
4. 완료를 주장하기 전에 전체 테스트 결과와 요구사항 체크리스트를 제시한다.
5. UI보다 스케줄 정확성, 데이터 무결성, 백업 가능성을 우선한다.
6. 핵심 기능은 인터넷 없이 동작해야 한다.
7. 불명확한 사소한 선택은 PLAN.md의 YAGNI 원칙에 맞춰 가장 단순한 안을 선택하고 기록한다.
```

### English

```text
Use PLAN.md as the single source of truth for this repository.

Build a local, single-user dashboard that manages 500 NeetCode problems at Level B,
120 core problems at Level C, 100 unseen transfer problems, and mock assessments
from 2026-08-06 through 2027-08-05.

Do not silently change the dates, hours, holidays, Level B/Level C definitions,
problem counts, state transitions, or completion gates in PLAN.md.
Proceed in this order:

1. Inspect the repository and write a detailed implementation plan that maps every PLAN.md requirement to testable tasks.
2. Implement the calendar engine and data model first, using test-driven development.
3. Run tests, type checking, and linting after every task.
4. Before claiming completion, show the full verification output and a requirement-by-requirement checklist.
5. Prioritize scheduling correctness, data integrity, and backup over UI polish.
6. Core functionality must work without internet access.
7. For minor ambiguities, choose the simplest YAGNI-compliant option and document the decision.
```


---

## 12. 최종 체크리스트 / Final Checklist

### 2027-03-28

```text
SEEN = 500 / 500
New problem deficit <= 5
Review debt is recoverable within the buffer week
```

### 2027-04-04

```text
NEW_PROBLEM_DEFICIT = 0
REVIEW_DEBT = 0
RED_QUEUE = 0 or explicitly scheduled within certification capacity
C1/C2 schedule complete for every eligible core problem
```

### 2027-08-05 — 필수 완료 / Required completion

```text
B_CERTIFIED = 500 / 500
C_CERTIFIED = 120 / 120
REVIEW_DEBT = 0
NEW_PROBLEM_DEFICIT = 0
RED_QUEUE = 0
Database backup verified
Markdown/CSV/JSON export verified
```

### 2027-08-05 — 외부 전이 검증 / External transfer validation

```text
UNSEEN_ATTEMPTS = 100 / 100
LIVE_MOCKS = 12 / 12
ONLINE_ASSESSMENTS = 8 / 8
LONG_FORM_TESTS = 3 / 3
Readiness thresholds evaluated without changing historical results
```

### 2027-08-06

B-500과 C-120이 완료되면 다음 400문제를 별도 버전의 계획으로 시작한다. 완료되지 않았다면 문제 수를 늘리지 않고 남은 인증과 실패 복구부터 끝낸다.

If B-500 and C-120 are complete, start the next 400 problems under a separate versioned plan. If they are incomplete, do not expand the set; finish remaining certifications and failure recovery first.

---

## 13. 가장 중요한 한 문장 / The One Rule That Matters Most

> **그날 예정된 기억 인출을 먼저 끝내고, 남은 시간으로 신규 문제를 진행한다.**  
> **Complete the retrieval work due today before using the remaining time for new problems.**
