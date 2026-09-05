"""
PB0627 — 스택을 모두 꺼낸 순서

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
values를 변경하지 않고 복사본이 빌 때까지 pop한 값들을 순서대로 반환한다.

연습 초점
---------
후입선출 순서를 반복되는 pop 결과로 관찰한다.

구현할 함수
-----------
def unwind_stack(values: list[str]) -> list[str]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := ['a', 'b', 'c']), unwind_stack(items) == ['c', 'b', 'a'] and items == ['a', 'b', 'c'])[-1] is True
- unwind_stack(['x']) == ['x']
- unwind_stack([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0627 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unwind_stack(values: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0627")


def self_test() -> None:
    assert ((items := ['a', 'b', 'c']), unwind_stack(items) == ['c', 'b', 'a'] and items == ['a', 'b', 'c'])[-1] is True
    assert unwind_stack(['x']) == ['x']
    assert unwind_stack([]) == []
