# Python Coding 목적 교정

Python Coding의 목적은 코딩테스트에서 쓰는 Python 문법·자료구조·표준 라이브러리를
문서 검색 없이 빠르고 정확하게 사용하는 자동화입니다. Python Basic은 기초 문법,
후속 NeetCode 250은 알고리즘 패턴과 C 레벨 인증을 담당합니다.

앞선 재평가에서는 문제 다양성을 알고리즘 범위로 잘못 해석해 48개 반복 슬롯에
트리·그래프·DP·백트래킹 등을 넣었습니다. 이 변경을 철회하고 같은 48개 ID를
Python 사용법 드릴로 다시 작성했습니다. 별도 Algorithm Bridge 과정을 새로 만들지 않았습니다.

## 실제 변경

| 문제 ID | Python 훈련 내용 |
|---|---|
| CI0022–0027 | 정렬 key, 동률 안정성, casefold, None 처리, itemgetter, in-place sort, 인덱스 정렬 |
| CI0122–0127 | enumerate 시작값, zip_longest, 별표 unpacking, zip→dict, yield 지연 실행, next 기본값 |
| CI0242–0247 | 슬라이스 대입, 얕은/행별 복사, 음수 pop 인덱스, 확장 슬라이스, 삽입 순서 중복 제거 |
| CI0362–0367 | deque.popleft, maxlen, rotate, extendleft, stack pop/underflow, FIFO 일부 소비 |
| CI0422–0427 | 중첩 enumerate, 행 복사 후 셀 수정, zip 전치, 객체 동일성, chain 평탄화, 독립 행 생성 |
| CI0482–0487 | Counter.subtract와 교집합, defaultdict(set), get의 None/누락 구분, pop 존재 여부, 집합 대칭 차 |
| CI0642–0647 | heappushpop/heapreplace 차이, nsmallest/nlargest key, merge+islice, push/peek/pop |
| CI0782–0787 | bisect lo/hi, insort_right key, 중복 구간 삭제, ceil 질의, record key, 구간 슬라이스 |

모든 교체 문제의 복습 목표는 150~300초 범위입니다. 처음 배우는 API는 설명을
먼저 학습하고, 시간을 측정할 때는 자료를 닫고 다시 구현합니다. 지정한 연산을
어떻게 Python으로 표현하는지가 주된 판단 대상입니다.

48개 ID는 유지하고 함수·파일 이름은 `_fluency_`와 새 과제 이름으로 바꿨습니다.
기존에 고친 잘못된 인수, OR/AND 분기, 원본 보존, 0 방향 정수 나눗셈,
동률 규칙 등의 개선은 유지했습니다. Basic 820개의 내용은 이번 교정에서 바꾸지 않았습니다.

## 반복과 진도

이전의 '240개 핵심 + 560개 선택' 정책은 철회했습니다. Python Coding 800개는
전체가 자동화 드릴이며 같은 계약의 반복도 인출 훈련으로 사용합니다.
테스트 중복 수는 감사 정보이며 반복을 불필요하다고 판정하는 근거로 쓰지 않습니다.

운영은 10문제 배치, 최초 통과율 85% 이상, 무작위 cold audit 90% 이상,
문서 검색 없이 도구를 쓰는지를 기준으로 합니다. 기존 계획의 날짜와 시간 예산은
이번 목적 교정 때문에 임의로 변경하지 않았습니다.

[전체 학습 경로](../../STUDY_PATH.md)와 [Coding 인덱스](../../python_coding/INDEX.md)는
800개 전체를 안내합니다. [전수 검사 JSON](2026-09-05-problem-bank.json)의 study_role은
`automation_drill`이며 같은 계약의 대표 ID는 비교·복습에만 사용합니다.

## 검증 범위

- 48개의 독립 참조 구현으로 144개 공개 검증식과 48개 추가 기대값을 실행합니다.
- 각 참조 구현이 지정된 Python API·문법을 사용하는지 확인합니다.
- sort/복사, Counter 연산, zip 길이, iterator 재소비, heap 결합 연산, bisect key 등을
  잘못 선택한 구현을 거부하는 반례를 포함합니다.
- 작은 입력 전체 조합에서 heap 결과, bisect 구간, deque 경계를 단순한 기대값과 대조합니다.
- 원본 보존과 명시적으로 원본을 바꿔야 하는 두 과제(CI0026, CI0242)를 구분합니다.
- 전체 은행의 문서·시그니처·테스트 일치, 재생성 일관성, 사용자 풀이 보존을 확인합니다.

공개 assert와 AST 검사는 숨은 전체 채점이나 장기 기억 인증을 대신하지 않습니다.
이번 검증은 문제의 Python 계약과 대표 오답을 확인하기 위한 것입니다.

검증 결과: 전체 회귀 테스트 36개와 Coding 800개 구조 검사가 통과했습니다.
재생성 계획은 `unchanged=800`이며, 교체 48개를 제외한 Coding 752개와
Basic 820개는 수정 전과 바이트가 같습니다. 사용자 풀이·기록 57개도 보존했습니다.
