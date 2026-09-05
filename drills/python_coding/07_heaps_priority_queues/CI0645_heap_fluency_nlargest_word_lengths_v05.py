"""
CI0645 — nlargest와 문자열 길이

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 05 / 20
Time cap: 150 seconds
Source checks: heapq_call

문제
----
heapq.nlargest(count, words, key=len)로 긴 단어부터 반환하세요. 0<=count<=1000이며 동률은 입력 순서이고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
key 값과 원소 자체의 비교

구현할 함수
-----------
def heap_fluency_nlargest_word_lengths(words: list[str], count: int) -> list[str]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_fluency_nlargest_word_lengths(['bb', 'aa', 'c', 'ddd'], 3) == ['ddd', 'bb', 'aa']
- heap_fluency_nlargest_word_lengths([], 3) == []
- ((_practice_1_0 := ['', 'x']), (_practice_1_1 := 8), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_nlargest_word_lengths(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['x', '']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0645 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_fluency_nlargest_word_lengths(words: list[str], count: int) -> list[str]:
    raise NotImplementedError("TODO: CI0645")


def self_test() -> None:
    assert heap_fluency_nlargest_word_lengths(['bb', 'aa', 'c', 'ddd'], 3) == ['ddd', 'bb', 'aa']
    assert heap_fluency_nlargest_word_lengths([], 3) == []
    assert ((_practice_1_0 := ['', 'x']), (_practice_1_1 := 8), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_nlargest_word_lengths(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['x', '']
