"""
PB0630 — 최근 작업 되돌리기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
count가 0 이상이라고 가정해 최대 count개의 최근 작업을 복사본에서 pop하고, 남은 작업과 취소된 작업의 pop 순서를 반환한다.

연습 초점
---------
요청 횟수가 리스트 길이보다 큰 경우에도 빈 스택을 안전하게 처리한다.

구현할 함수
-----------
def undo_recent_actions(actions: list[str], count: int) -> tuple[list[str], list[str]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := ['open', 'edit', 'save']), undo_recent_actions(items, 2) == (['open'], ['save', 'edit']) and items == ['open', 'edit', 'save'])[-1] is True
- undo_recent_actions(['open'], 5) == ([], ['open'])
- undo_recent_actions([], 3) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0630 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def undo_recent_actions(actions: list[str], count: int) -> tuple[list[str], list[str]]:
    raise NotImplementedError("TODO: PB0630")


def self_test() -> None:
    assert ((items := ['open', 'edit', 'save']), undo_recent_actions(items, 2) == (['open'], ['save', 'edit']) and items == ['open', 'edit', 'save'])[-1] is True
    assert undo_recent_actions(['open'], 5) == ([], ['open'])
    assert undo_recent_actions([], 3) == ([], [])
