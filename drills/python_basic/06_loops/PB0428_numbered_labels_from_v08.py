"""
PB0428 — 지정 번호부터 라벨

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
for와 range(start_number, start_number+len(labels))를 사용해 '<번호>:<라벨>' 문자열을 반환한다.

연습 초점
---------
range 시작값을 외부 번호에 맞추기

구현할 함수
-----------
def numbered_labels_from(labels: list[str], start_number: int) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- numbered_labels_from(['a', 'b'], 5) == ['5:a', '6:b']
- numbered_labels_from([], 3) == []
- numbered_labels_from(['x'], -1) == ['-1:x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0428 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def numbered_labels_from(labels: list[str], start_number: int) -> list[str]:
    raise NotImplementedError("TODO: PB0428")


def self_test() -> None:
    assert numbered_labels_from(['a', 'b'], 5) == ['5:a', '6:b']
    assert numbered_labels_from([], 3) == []
    assert numbered_labels_from(['x'], -1) == ['-1:x']
