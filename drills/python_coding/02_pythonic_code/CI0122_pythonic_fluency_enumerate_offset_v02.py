"""
CI0122 — enumerate 시작 번호

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 02 / 20
Time cap: 150 seconds
Source checks: enumerate_call

문제
----
enumerate(values, start=start)로 '번호:값' 문자열을 반환하세요. 빈 문자열과 음수 start도 그대로 처리하며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
enumerate start 인수

구현할 함수
-----------
def pythonic_fluency_enumerate_offset(values: list[str], start: int) -> list[str]:

필수 구현 방식
--------------
- enumerate()를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_fluency_enumerate_offset(['a', 'b'], 3) == ['3:a', '4:b']
- pythonic_fluency_enumerate_offset([], 9) == []
- ((_practice_1_0 := ['', 'x']), (_practice_1_1 := (-1)), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := pythonic_fluency_enumerate_offset(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['-1:', '0:x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0122 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_fluency_enumerate_offset(values: list[str], start: int) -> list[str]:
    raise NotImplementedError("TODO: CI0122")


def self_test() -> None:
    assert pythonic_fluency_enumerate_offset(['a', 'b'], 3) == ['3:a', '4:b']
    assert pythonic_fluency_enumerate_offset([], 9) == []
    assert ((_practice_1_0 := ['', 'x']), (_practice_1_1 := (-1)), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := pythonic_fluency_enumerate_offset(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['-1:', '0:x']
