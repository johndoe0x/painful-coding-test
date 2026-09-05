"""
PB0816 — slice step 오류 구분

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 06 / 10
Time cap: 150 seconds
Source checks: try, multiple_except

문제
----
먼저 step_text를 int로 변환한다. 이 변환의 ValueError는 invalid_step이다. 변환 후 values[::step]을 실행하며 step이 0이라 발생한 ValueError는 zero_step으로 구분한다.

연습 초점
---------
변환 단계와 슬라이싱 단계를 별도 try-except로 나눠 같은 ValueError의 원인을 구분

구현할 함수
-----------
def exc_slice_with_step_status(values: list[int], step_text: str) -> tuple[str, list[int]]:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_slice_with_step_status([1, 2, 3], '2') == ('ok', [1, 3])
- exc_slice_with_step_status([1, 2], 'x') == ('invalid_step', [])
- exc_slice_with_step_status([1, 2], ' 00 ') == ('zero_step', [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0816 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_slice_with_step_status(values: list[int], step_text: str) -> tuple[str, list[int]]:
    raise NotImplementedError("TODO: PB0816")


def self_test() -> None:
    assert exc_slice_with_step_status([1, 2, 3], '2') == ('ok', [1, 3])
    assert exc_slice_with_step_status([1, 2], 'x') == ('invalid_step', [])
    assert exc_slice_with_step_status([1, 2], ' 00 ') == ('zero_step', [])
