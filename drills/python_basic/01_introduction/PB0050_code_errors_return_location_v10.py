"""
PB0050 — 반복문 안의 이른 return 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 첫 원소를 처리한 직후 return해 나머지를 검사하지 않습니다. 반복을 끝낸 뒤 모든 짝수를 입력 순서대로 반환하세요.

연습 초점
---------
return을 반복문 밖에 두어 전체 입력 처리

구현할 함수
-----------
def collect_even_numbers(numbers: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- collect_even_numbers([1, 2, 4, 5]) == [2, 4]
- collect_even_numbers([]) == []
- collect_even_numbers([3]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0050 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def collect_even_numbers(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
        return result
    return result


def self_test() -> None:
    assert collect_even_numbers([1, 2, 4, 5]) == [2, 4]
    assert collect_even_numbers([]) == []
    assert collect_even_numbers([3]) == []
