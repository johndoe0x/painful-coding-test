from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import textwrap

from generate_bank import CHAPTERS, ROOT, SEEDS, Seed


@dataclass(frozen=True)
class VariantProfile:
    slug: str
    title: str
    instruction: str
    time_cap: int


def vp(slug: str, title: str, instruction: str, time_cap: int = 240) -> VariantProfile:
    return VariantProfile(slug, title, instruction, time_cap)


PROFILES: dict[str, list[VariantProfile]] = {
    "Sorting": [
        vp("edge_dataset", "경계 데이터셋", "빈 입력, 길이 1, 중복, 음수를 모두 처리하고 입력별 결과를 설명한다.", 180),
        vp("input_immutability", "입력 불변성", "입력 리스트의 사본을 남겨 함수 호출 전후가 같은지 검증한다.", 180),
        vp("stable_ties", "안정 정렬과 동률", "동일한 정렬 키를 가진 항목의 원래 순서가 언제 유지되는지 테스트한다.", 240),
        vp("named_key", "명명된 key 함수", "정렬 기준을 별도 함수로 추출하고 기준의 의미를 설명한다.", 210),
        vp("lambda_key", "lambda key", "같은 정렬 기준을 lambda로 표현하고 명명된 함수 버전과 결과를 비교한다.", 210),
        vp("secondary_key", "두 번째 정렬 기준", "첫 번째 기준이 같을 때 결정적인 두 번째 기준을 적용한다.", 240),
        vp("reverse_contract", "정렬 방향 전환", "기본 정렬 계약과 반대 방향 결과를 보조 함수로 만들고 역관계를 검증한다.", 240),
        vp("partial_order", "부분 정렬", "전체 결과 중 앞쪽 k개만 필요한 경우의 구현 선택과 복잡도를 비교한다.", 270),
        vp("kth_element", "K번째 원소", "정렬 결과를 이용해 유효한 k번째 원소를 구하는 보조 함수를 작성한다.", 270),
        vp("merge_sorted_batches", "정렬 배치 병합", "두 개의 정렬 결과를 다시 전체 정렬하지 않고 병합하는 보조 함수를 작성한다.", 300),
        vp("nearly_sorted", "거의 정렬된 입력", "거의 정렬된 입력과 역순 입력을 테스트하고 Python 정렬 복잡도를 설명한다.", 240),
        vp("duplicate_policy", "중복 정책", "중복값을 유지하는 결과와 제거하는 결과를 각각 테스트한다.", 240),
        vp("representation_key", "표현 기반 key", "문자열은 정규화 key, 숫자는 절댓값 key처럼 자료형에 맞는 key를 추가한다.", 270),
        vp("streaming_buffer", "스트리밍 버퍼", "값을 여러 배치로 누적한 뒤 마지막에 기본 정렬 계약을 만족시키는 보조 API를 작성한다.", 300),
        vp("builtin_contract", "sort와 sorted 계약", "in-place sort의 반환값과 sorted의 원본 보존 차이를 테스트한다.", 240),
        vp("complexity_audit", "복잡도 감사", "구현의 시간·공간복잡도를 입력 크기 n으로 적고 불필요한 복사를 제거한다.", 210),
        vp("regression_bug", "정렬 회귀 버그", "reverse, key 또는 반환값을 잘못 사용하는 버그를 재현하는 테스트를 먼저 작성한다.", 240),
        vp("randomized_oracle", "무작위 oracle 비교", "작은 무작위 입력에서 표준 sorted 결과와 구현 결과를 반복 비교한다.", 300),
        vp("blind_interview", "블라인드 정렬 인터뷰", "문제 설명만 보고 구현·테스트·복잡도 설명을 제한시간 안에 완료한다.", 300),
    ],
    "Pythonic Code": [
        vp("empty_single", "빈 값과 단일 값", "빈 입력과 원소 하나 입력에서 Pythonic 표현이 예외 없이 동작하게 한다.", 180),
        vp("iterator_input", "iterator 입력", "리스트뿐 아니라 iterator를 한 번만 순회해 같은 의미의 결과를 만든다.", 240),
        vp("generator_version", "generator 버전", "동일한 처리를 lazy generator 보조 함수로 작성하고 list 결과와 비교한다.", 270),
        vp("explicit_loop", "명시적 loop", "Pythonic 구현을 명시적 loop로 다시 작성해 두 결과를 비교한다.", 210),
        vp("idiomatic_rewrite", "관용적 재작성", "인덱스 직접 관리 코드를 enumerate, zip, unpacking 등 seed의 핵심 idiom으로 바꾼다.", 210),
        vp("strict_lengths", "길이 불일치", "여러 iterable을 다룬다면 길이 불일치 정책을 명시하고 테스트한다.", 240),
        vp("start_offset", "시작 인덱스", "인덱스가 필요한 seed는 0이 아닌 시작값을 지원하는 보조 함수를 추가한다.", 240),
        vp("filter_condition", "필터 조건 결합", "원래 동작 전에 조건 필터를 적용하되 상대 순서를 보존한다.", 240),
        vp("mapping_output", "매핑 출력", "기존 결과를 key-value 매핑으로 표현하는 보조 함수를 작성한다.", 240),
        vp("any_all", "any와 all", "여러 결과의 하나 이상·모두 만족 조건을 any/all로 검증한다.", 240),
        vp("default_values", "기본값", "입력이 비었거나 짧을 때 사용할 명시적인 기본값 정책을 추가한다.", 240),
        vp("type_mixture", "혼합 자료형", "지원하는 자료형과 거부하는 자료형을 정하고 TypeError 테스트를 작성한다.", 270),
        vp("no_index_mutation", "인덱스 상태 제거", "수동 인덱스나 외부 가변 상태 없이 seed의 idiom만으로 구현한다.", 210),
        vp("nested_records", "중첩 레코드", "tuple이나 dict 레코드 안의 값을 seed의 idiom으로 추출·조합한다.", 270),
        vp("batch_pipeline", "배치 파이프라인", "여러 입력 묶음을 처리하는 파이프라인을 작성하고 결과 순서를 검증한다.", 300),
        vp("complexity_audit", "복잡도 감사", "lazy/eager 선택이 시간과 공간에 미치는 영향을 설명한다.", 210),
        vp("regression_bug", "Pythonic 회귀 버그", "unpacking 개수, zip 절단, enumerate offset 관련 버그 테스트를 작성한다.", 240),
        vp("property_checks", "성질 기반 검사", "결과 길이·순서·일대일 대응처럼 항상 참이어야 할 성질을 assert한다.", 270),
        vp("blind_interview", "블라인드 Pythonic 인터뷰", "seed의 핵심 idiom을 직접 떠올려 구현과 테스트를 제한시간 안에 끝낸다.", 300),
    ],
    "Lists": [
        vp("empty_single", "빈 리스트와 단일 원소", "빈 리스트와 길이 1 리스트의 반환 계약을 명시하고 테스트한다.", 180),
        vp("input_immutability", "입력 불변성", "입력을 수정하지 않는 버전을 구현하고 원본 보존을 assert한다.", 210),
        vp("inplace_version", "in-place 버전", "별도 보조 함수에서 같은 핵심 동작을 in-place로 수행하고 반환 계약을 정한다.", 240),
        vp("shallow_aliasing", "얕은 복사와 aliasing", "중첩 리스트 또는 공유 원소가 있을 때 얕은 복사의 영향을 테스트한다.", 270),
        vp("negative_indices", "음수 인덱스", "음수 인덱스를 허용할지 거부할지 정책을 정하고 경계를 테스트한다.", 240),
        vp("slice_bounds", "슬라이스 경계", "start·stop·step 경계를 포함한 보조 슬라이스 동작을 작성한다.", 240),
        vp("duplicate_policy", "중복 정책", "중복 유지·첫 항목만 유지 등 명시된 정책을 테스트한다.", 240),
        vp("filter_before", "사전 필터", "seed 동작 전에 predicate를 만족하는 값만 남기는 보조 함수를 작성한다.", 240),
        vp("map_after", "사후 변환", "seed 결과의 각 원소에 변환 함수를 적용하는 보조 함수를 작성한다.", 240),
        vp("chunked_input", "청크 입력", "여러 리스트 청크를 순서대로 받아 하나의 결과를 만드는 함수를 작성한다.", 270),
        vp("rotate", "회전", "결과 리스트를 k만큼 좌우 회전시키는 후처리를 추가한다.", 240),
        vp("two_pointer", "두 포인터", "가능한 경우 양끝 인덱스를 사용해 추가 리스트 생성을 줄인다.", 270),
        vp("stable_removal", "안정적 삭제", "삭제 대상이 여러 개여도 남은 원소의 상대 순서를 보존한다.", 240),
        vp("nested_lists", "중첩 리스트", "한 단계 중첩된 입력을 평탄화할지 보존할지 정책을 정해 구현한다.", 270),
        vp("batch_queries", "다중 쿼리", "같은 리스트에 여러 index 또는 value 쿼리를 처리한다.", 300),
        vp("complexity_audit", "복잡도 감사", "중간 삽입·삭제·검색 비용을 설명하고 불필요한 O(n²)을 피한다.", 210),
        vp("regression_bug", "리스트 회귀 버그", "aliasing, pop 인덱스, slice 끝점 관련 실패 테스트를 작성한다.", 240),
        vp("property_checks", "리스트 성질 검사", "길이, 원본 보존, 순서 등 항상 참인 성질을 세 개 assert한다.", 270),
        vp("blind_interview", "블라인드 리스트 인터뷰", "문제 설명만 보고 구현·경계 테스트·복잡도를 제한시간 안에 끝낸다.", 300),
    ],
    "Stacks and Queues": [
        vp("empty_underflow", "빈 구조 underflow", "pop 또는 dequeue 요청이 빈 구조에 들어올 때 정책을 명시하고 테스트한다.", 210),
        vp("peek_operation", "peek 연산", "제거하지 않고 다음 값을 확인하는 연산을 보조 API에 추가한다.", 240),
        vp("long_sequence", "긴 연산열", "100개 이상의 연산에서도 순서 계약이 유지되는지 테스트한다.", 240),
        vp("capacity_limit", "용량 제한", "최대 용량을 넘는 삽입을 거부하거나 오래된 값을 제거하는 정책을 구현한다.", 270),
        vp("lifo_fifo_proof", "LIFO·FIFO 증명", "반복값이 포함된 연산열로 LIFO 또는 FIFO 성질을 assert한다.", 210),
        vp("two_structures", "두 구조 전환", "stack 두 개로 queue 또는 queue 두 개로 stack을 구성하는 보조 구현을 작성한다.", 300),
        vp("undo_history", "Undo 기록", "연산과 undo를 처리하는 작은 명령 기록기를 작성한다.", 300),
        vp("parentheses", "괄호 상태", "stack을 사용하는 괄호 검증 보조 함수를 추가한다.", 270),
        vp("rpn", "후위 표기식", "stack을 사용하는 작은 정수 후위 표기식 평가기를 추가한다.", 300),
        vp("next_greater", "다음 큰 값", "단조 stack을 사용해 각 위치의 다음 큰 값을 구하는 보조 함수를 작성한다.", 300),
        vp("monotonic_stack", "단조 stack", "증가 또는 감소 단조성을 유지하는 push 규칙을 구현한다.", 300),
        vp("bfs_queue", "BFS queue", "작은 인접 리스트에서 deque를 사용한 BFS 방문 순서를 반환한다.", 300),
        vp("sliding_window", "슬라이딩 윈도우", "단조 deque로 고정 길이 윈도우의 최댓값을 구하는 보조 함수를 작성한다.", 300),
        vp("circular_behavior", "원형 동작", "끝과 시작이 연결되는 원형 버퍼의 인덱스 정책을 테스트한다.", 300),
        vp("streaming_api", "스트리밍 API", "연산을 하나씩 입력받아 상태와 방출값을 갱신하는 객체 없는 closure API를 작성한다.", 300),
        vp("complexity_audit", "복잡도 감사", "양끝 연산 O(1)과 list.pop(0)의 O(n) 차이를 설명한다.", 210),
        vp("regression_bug", "순서 회귀 버그", "왼쪽·오른쪽 제거 또는 push 순서를 뒤집은 버그 테스트를 작성한다.", 240),
        vp("property_checks", "자료구조 성질 검사", "연산 후 크기, 순서, 보존되는 값에 대한 성질을 assert한다.", 270),
        vp("blind_interview", "블라인드 stack·queue 인터뷰", "자료구조 선택부터 테스트·복잡도까지 제한시간 안에 완료한다.", 300),
    ],
    "2-D Lists": [
        vp("empty_shapes", "빈 격자 형태", "빈 격자, 빈 행, 1x1 격자의 계약을 각각 테스트한다.", 210),
        vp("jagged_rows", "가변 길이 행", "직사각형이 아닌 입력을 거부하거나 지원하는 명시적 정책을 구현한다.", 270),
        vp("input_immutability", "격자 불변성", "원본 격자를 변경하지 않는지 깊은 사본으로 검증한다.", 240),
        vp("row_major", "행 우선 순회", "행 우선 순회 순서를 반환하는 보조 함수를 작성한다.", 240),
        vp("column_major", "열 우선 순회", "열 우선 순회와 행 우선 순회의 차이를 테스트한다.", 240),
        vp("row_column_sums", "행·열 합", "각 행과 열의 합을 반환하는 보조 함수를 작성한다.", 270),
        vp("transpose", "전치", "직사각형 격자의 transpose를 새 격자로 반환한다.", 270),
        vp("rotate_90", "90도 회전", "정사각형 격자를 시계 방향으로 회전하는 보조 함수를 작성한다.", 300),
        vp("diagonals", "대각선", "주대각선과 부대각선 값을 반환한다.", 240),
        vp("boundary_cells", "경계 셀", "격자의 바깥 테두리 셀을 중복 없이 순서대로 반환한다.", 270),
        vp("orthogonal_neighbors", "상하좌우 이웃", "모서리·변·중앙 위치의 유효 이웃을 테스트한다.", 240),
        vp("eight_neighbors", "8방향 이웃", "대각선을 포함한 8방향 이웃 보조 함수를 작성한다.", 270),
        vp("spiral_order", "나선 순회", "직사각형 격자를 나선 순서로 읽는 보조 함수를 작성한다.", 300),
        vp("flood_fill", "Flood Fill", "작은 격자에서 BFS 또는 DFS로 연결된 같은 값을 변경한다.", 300),
        vp("prefix_matrix", "2D Prefix Sum", "직사각형 영역 합 쿼리를 위한 prefix matrix를 작성한다.", 300),
        vp("complexity_audit", "복잡도 감사", "행 R, 열 C 기준으로 시간·공간복잡도를 적는다.", 210),
        vp("regression_bug", "격자 회귀 버그", "행·열 뒤바꿈과 경계 초과를 잡는 테스트를 작성한다.", 240),
        vp("property_checks", "격자 성질 검사", "원소 수, shape, 변환 전후 관계를 assert한다.", 270),
        vp("blind_interview", "블라인드 격자 인터뷰", "순회 방향과 경계를 직접 설계해 제한시간 안에 구현한다.", 300),
    ],
    "Hashmaps and Hashsets": [
        vp("empty_single", "빈 입력과 단일 값", "빈 입력과 원소 하나에서 반환 계약을 테스트한다.", 180),
        vp("duplicate_heavy", "중복 집중", "같은 key나 값이 반복되는 입력에서 빈도·갱신 정책을 검증한다.", 210),
        vp("missing_keys", "누락 key", "존재하지 않는 key 조회에 get 또는 defaultdict 기반 정책을 적용한다.", 240),
        vp("input_immutability", "입력 불변성", "입력 mapping·set·list가 변경되지 않는지 검증한다.", 210),
        vp("insertion_order_independent", "삽입 순서 독립성", "입력 순서가 달라도 논리적 결과가 같은지 테스트한다.", 240),
        vp("case_normalization", "key 정규화", "문자열 key가 있다면 대소문자·공백을 정규화하는 보조 함수를 추가한다.", 240),
        vp("grouping", "그룹화", "계산된 key를 기준으로 여러 값을 list에 그룹화한다.", 270),
        vp("frequency_ties", "빈도 동률", "빈도가 같은 경우 결정적인 tie-break 규칙을 적용한다.", 240),
        vp("set_algebra", "집합 대수", "합집합·교집합·차집합으로 결과 관계를 검증한다.", 240),
        vp("tuple_composite_key", "복합 tuple key", "두 필드를 tuple key로 결합해 조회 또는 빈도 계산을 수행한다.", 270),
        vp("two_sum_lookup", "보수 lookup", "한 번의 순회와 hashmap으로 목표 합 쌍을 찾는 보조 함수를 작성한다.", 300),
        vp("anagram_groups", "애너그램 그룹", "정규화된 문자 빈도 또는 정렬 key로 문자열을 그룹화한다.", 300),
        vp("join_records", "해시 조인", "공통 key를 기준으로 두 레코드 목록을 결합한다.", 300),
        vp("sliding_counts", "슬라이딩 빈도", "고정 길이 윈도우가 이동할 때 Counter를 증감한다.", 300),
        vp("multi_queries", "다중 조회", "하나의 전처리 mapping으로 여러 조회를 처리한다.", 270),
        vp("complexity_audit", "복잡도 감사", "평균 O(1)과 최악 상황의 가정을 설명한다.", 210),
        vp("regression_bug", "해시 회귀 버그", "누락 key, 중복 덮어쓰기, mutable key 오류를 잡는 테스트를 작성한다.", 240),
        vp("property_checks", "해시 성질 검사", "빈도 합, key 유일성, 집합 중복 제거 성질을 assert한다.", 270),
        vp("blind_interview", "블라인드 해시 인터뷰", "적절한 dict/set 표현부터 테스트·복잡도까지 제한시간 안에 끝낸다.", 300),
    ],
    "Heaps / Priority Queues": [
        vp("empty_single", "빈 heap과 단일 값", "빈 입력·k=0·단일 원소의 계약을 테스트한다.", 180),
        vp("duplicate_priorities", "중복 우선순위", "같은 우선순위가 반복될 때 결정적인 처리 순서를 만든다.", 240),
        vp("negative_values", "음수와 부호", "음수 값과 max-heap 부호 변환이 섞여도 올바르게 처리한다.", 240),
        vp("input_immutability", "입력 불변성", "heapify 전에 입력을 복사해 원본을 보존하는지 검증한다.", 210),
        vp("heapify_vs_push", "heapify와 반복 push", "두 heap 구성 방식의 결과와 복잡도를 비교한다.", 240),
        vp("peek_contract", "peek 계약", "pop 없이 최상위 값을 확인하고 빈 heap 정책을 테스트한다.", 210),
        vp("top_k_boundaries", "Top-K 경계", "k=0, k=1, k>=n과 중복값을 모두 테스트한다.", 240),
        vp("kth_element", "K번째 원소", "heap을 사용해 k번째 작은 값 또는 큰 값을 구하는 보조 함수를 작성한다.", 270),
        vp("merge_k", "K개 정렬열 병합", "여러 정렬 리스트의 현재 원소를 heap에 넣어 병합한다.", 300),
        vp("task_scheduler", "작업 스케줄러", "우선순위와 tie-break가 있는 작업 처리 순서를 반환한다.", 300),
        vp("streaming_top_k", "스트리밍 Top-K", "값이 도착할 때 크기 k heap을 유지하고 현재 결과를 반환한다.", 300),
        vp("two_heaps", "두 heap", "작은 절반과 큰 절반을 두 heap으로 나누는 보조 구조를 작성한다.", 300),
        vp("running_median", "실시간 중앙값", "두 heap을 사용해 각 prefix의 중앙값을 계산한다.", 300),
        vp("lazy_deletion", "Lazy deletion", "삭제 예약 Counter와 heap을 결합해 지연 삭제를 구현한다.", 300),
        vp("bounded_capacity", "제한 용량 heap", "항상 최대 k개 또는 최소 k개만 남도록 heap 크기를 제한한다.", 270),
        vp("complexity_audit", "복잡도 감사", "heap 크기 k와 입력 n을 구분해 복잡도를 적는다.", 210),
        vp("regression_bug", "heap 회귀 버그", "부호 복원, tuple 순서, pop 시점 오류를 잡는 테스트를 작성한다.", 240),
        vp("property_checks", "heap 성질 검사", "부모·자식 heap 성질과 결과 정렬 관계를 assert한다.", 270),
        vp("blind_interview", "블라인드 heap 인터뷰", "heap 선택 이유·구현·테스트·복잡도를 제한시간 안에 설명한다.", 300),
    ],
    "Sorted Dicts and Sorted Sets": [
        vp("empty_single", "빈 구조와 단일 값", "빈 입력과 원소 하나의 정렬·중복 제거 계약을 테스트한다.", 180),
        vp("duplicate_policy", "중복 정책", "중복 유지 횟수와 유일 key 표현을 각각 명시한다.", 210),
        vp("bisect_insert", "bisect 삽입", "bisect_left 또는 insort로 정렬 상태를 유지하며 값을 삽입한다.", 240),
        vp("bisect_remove", "bisect 삭제", "bisect로 위치를 찾고 존재할 때만 하나를 삭제한다.", 240),
        vp("predecessor", "직전 원소", "query보다 작은 가장 큰 원소를 찾는 보조 함수를 작성한다.", 240),
        vp("successor", "직후 원소", "query보다 큰 가장 작은 원소를 찾는 보조 함수를 작성한다.", 240),
        vp("lower_upper_bound", "Lower·Upper Bound", "같은 값의 시작·끝 삽입 위치를 반환한다.", 240),
        vp("range_count", "구간 개수", "정렬 리스트와 bisect로 [low, high] 원소 개수를 계산한다.", 270),
        vp("range_values", "구간 값", "정렬 상태에서 지정 구간 값만 slice로 반환한다.", 270),
        vp("batch_queries", "다중 순서 쿼리", "한 번 정렬한 뒤 predecessor·successor 쿼리를 여러 개 처리한다.", 300),
        vp("coordinate_compression", "좌표 압축", "정렬된 유일값을 rank로 매핑한다.", 300),
        vp("interval_events", "구간 이벤트", "시작·끝 이벤트를 정렬해 활성 구간 수를 추적한다.", 300),
        vp("ordered_frequency", "정렬 빈도", "Counter 결과를 key 정렬 순서로 반환한다.", 270),
        vp("two_sorted_sets", "두 정렬 집합", "두 집합의 합·교·차집합을 정렬된 결과로 반환한다.", 270),
        vp("stream_updates", "온라인 삽입", "값을 하나씩 삽입하며 정렬 상태와 유일성 정책을 유지한다.", 300),
        vp("complexity_audit", "복잡도 감사", "bisect 검색 O(log n)과 list 삽입 O(n)을 구분해 설명한다.", 210),
        vp("regression_bug", "정렬 구조 회귀 버그", "left/right bisect 혼동과 중복 삭제 오류를 잡는 테스트를 작성한다.", 240),
        vp("property_checks", "정렬 구조 성질", "정렬성·유일성·길이 관계를 assert한다.", 270),
        vp("blind_interview", "블라인드 ordered 인터뷰", "표준 라이브러리 제약 안에서 표현을 선택하고 구현한다.", 300),
    ],
}


TESTS: dict[str, list[str]] = {
    "sort_ascending": ["sort_ascending([]) == []", "sort_ascending([1]) == [1]", "sort_ascending([3, -1, 3, 0]) == [-1, 0, 3, 3]", "sort_ascending([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]"],
    "sort_descending": ["sort_descending([]) == []", "sort_descending([1]) == [1]", "sort_descending([3, -1, 3, 0]) == [3, 3, 0, -1]", "sort_descending([1, 2, 3]) == [3, 2, 1]"],
    "sort_custom": ["sort_words([]) == []", "sort_words(['b', 'a']) == ['a', 'b']", "sort_words(['bbb', 'a', 'cc', 'ab']) == ['a', 'ab', 'cc', 'bbb']", "sort_words(['aa', 'aa', 'b']) == ['b', 'aa', 'aa']"],
    "sort_lambda": ["sort_people([]) == []", "sort_people([('B', 20), ('A', 20), ('C', 18)]) == [('C', 18), ('A', 20), ('B', 20)]", "sort_people([('Z', 1)]) == [('Z', 1)]", "sort_people([('b', 2), ('a', 2)]) == [('a', 2), ('b', 2)]"],
    "sorted_copy": ["sorted_copy([]) == ([], [])", "sorted_copy([2, 1]) == ([1, 2], [2, 1])", "sorted_copy([3, 3, 1]) == ([1, 3, 3], [3, 3, 1])", "sorted_copy([-1, 2, 0]) == ([-1, 0, 2], [-1, 2, 0])"],
    "unpacking": ["swap_and_sum((0, 0)) == (0, 0, 0)", "swap_and_sum((2, 5)) == (5, 2, 7)", "swap_and_sum((-1, 3)) == (3, -1, 2)", "swap_and_sum((10, -4)) == (-4, 10, 6)"],
    "loop_unpacking": ["sum_products([]) == 0", "sum_products([(2, 3), (4, 5)]) == 26", "sum_products([(-1, 2), (3, 0)]) == -2", "sum_products([(1, 1)]) == 1"],
    "enumerate": ["indexed_labels([]) == []", "indexed_labels(['a', 'b']) == ['0:a', '1:b']", "indexed_labels(['x']) == ['0:x']", "indexed_labels(['', 'z']) == ['0:', '1:z']"],
    "zip": ["pair_columns([], []) == []", "pair_columns(['A', 'B'], [10, 20, 30]) == [('A', 10), ('B', 20)]", "pair_columns(['A'], []) == []", "pair_columns(['A'], [0]) == [('A', 0)]"],
    "inequality": ["outside_range(5, 1, 4) is True", "outside_range(1, 1, 4) is False", "outside_range(4, 1, 4) is False", "outside_range(-1, 0, 0) is True"],
    "min_max_shortcut": ["clamp(12, 0, 10) == 10", "clamp(-1, 0, 10) == 0", "clamp(5, 0, 10) == 5", "clamp(0, 0, 0) == 0"],
    "resizable_list_1": ["append_sequence([], []) == []", "append_sequence([1], [2, 3]) == [1, 2, 3]", "append_sequence([], [0]) == [0]", "append_sequence([1, 1], [1]) == [1, 1, 1]"],
    "resizable_list_2": ["insert_and_remove([1, -1, 3], 1, 2) == [1, 2, 3]", "insert_and_remove([], 0, 5) == [5]", "insert_and_remove([1, 2], 2, 3) == [1, 2, 3]", "insert_and_remove([-1, -2], 0, 0) == [0, -2]"],
    "list_concat": ["concat_lists([], []) == []", "concat_lists([1, 2], [3]) == [1, 2, 3]", "concat_lists([], [1]) == [1]", "concat_lists([1], []) == [1]"],
    "list_initialization": ["repeat_value('x', 0) == []", "repeat_value('x', 3) == ['x', 'x', 'x']", "repeat_value(0, 1) == [0]", "repeat_value(None, 2) == [None, None]"],
    "list_clone": ["clone_and_update([1, 2], 0, 9) == ([9, 2], [1, 2])", "clone_and_update([0], 0, 1) == ([1], [0])", "clone_and_update([1, 2, 3], 2, -1) == ([1, 2, -1], [1, 2, 3])", "clone_and_update(['a'], 0, 'b') == (['b'], ['a'])"],
    "list_comprehension": ["even_squares([]) == []", "even_squares([1, 2, 3, 4]) == [4, 16]", "even_squares([-2, -1, 0]) == [4, 0]", "even_squares([2, 2]) == [4, 4]"],
    "stack_push_pop": ["process_stack([]) == []", "process_stack([('push', 2), ('push', 3), ('pop', None)]) == [3]", "process_stack([('push', -1), ('pop', None)]) == [-1]", "process_stack([('push', 1), ('push', 1), ('pop', None), ('pop', None)]) == [1, 1]"],
    "queue_enqueue_dequeue": ["process_queue([]) == []", "process_queue([('enqueue', 2), ('enqueue', 3), ('dequeue', None)]) == [2]", "process_queue([('enqueue', -1), ('dequeue', None)]) == [-1]", "process_queue([('enqueue', 1), ('enqueue', 1), ('dequeue', None), ('dequeue', None)]) == [1, 1]"],
    "double_ended_queue": ["rotate_window([], 3) == []", "rotate_window([1, 2, 3], 1) == [3, 1, 2]", "rotate_window([1, 2, 3], -1) == [2, 3, 1]", "rotate_window([1], 100) == [1]"],
    "multi_dimensional_list": ["matrix_shape([]) == (0, 0)", "matrix_shape([[]]) == (1, 0)", "matrix_shape([[1, 2], [3, 4]]) == (2, 2)", "matrix_shape([[1]]) == (1, 1)"],
    "grid_neighbors": ["orthogonal_neighbors([[1]], 0, 0) == []", "orthogonal_neighbors([[1, 2], [3, 4]], 0, 0) == [3, 2]", "orthogonal_neighbors([[1, 2], [3, 4]], 1, 1) == [2, 3]", "orthogonal_neighbors([[1, 2, 3]], 0, 1) == [1, 3]"],
    "nested_list_comprehension": ["make_grid(0, 3) == []", "make_grid(2, 0) == [[], []]", "make_grid(2, 3) == [[0, 1, 2], [1, 2, 3]]", "make_grid(1, 1) == [[0]]"],
    "hash_map_basics": ["index_by_key([]) == {}", "index_by_key([('a', 1), ('a', 2)]) == {'a': 2}", "index_by_key([('x', -1)]) == {'x': -1}", "index_by_key([('a', 1), ('b', 2)]) == {'a': 1, 'b': 2}"],
    "default_dict": ["group_words([]) == {}", "group_words(['ant', 'apple', 'bee']) == {'a': ['ant', 'apple'], 'b': ['bee']}", "group_words(['x']) == {'x': ['x']}", "group_words(['aa', 'ab']) == {'a': ['aa', 'ab']}"],
    "counter": ["most_common_value([]) is None", "most_common_value(['b', 'a', 'b']) == ('b', 2)", "most_common_value(['b', 'a']) == ('a', 1)", "most_common_value(['x']) == ('x', 1)"],
    "dict_comprehension": ["square_map([]) == {}", "square_map([2, 3]) == {2: 4, 3: 9}", "square_map([-2, 0]) == {-2: 4, 0: 0}", "square_map([2, 2]) == {2: 4}"],
    "dict_items": ["filter_mapping({}, 2) == {}", "filter_mapping({'a': 1, 'b': 3}, 2) == {'b': 3}", "filter_mapping({'a': 2}, 2) == {'a': 2}", "filter_mapping({'a': -1}, 0) == {}"],
    "hash_set_basics": ["has_duplicate([]) is False", "has_duplicate([1, 2, 1]) is True", "has_duplicate([1, 2, 3]) is False", "has_duplicate([-1, -1]) is True"],
    "set_comprehension": ["unique_lengths([]) == set()", "unique_lengths(['a', 'bb', 'cc']) == {1, 2}", "unique_lengths(['']) == {0}", "unique_lengths(['abc', 'x']) == {1, 3}"],
    "tuple_keys": ["count_coordinates([]) == {}", "count_coordinates([(0, 0), (0, 0), (1, 2)]) == {(0, 0): 2, (1, 2): 1}", "count_coordinates([(-1, 2)]) == {(-1, 2): 1}", "count_coordinates([(1, 1), (2, 2)]) == {(1, 1): 1, (2, 2): 1}"],
    "heap_push": ["running_minimum([]) == []", "running_minimum([3, 1, 2]) == [3, 1, 1]", "running_minimum([-1, -2]) == [-1, -2]", "running_minimum([2, 2]) == [2, 2]"],
    "heap_pop": ["pop_sorted([]) == []", "pop_sorted([3, 1, 2]) == [1, 2, 3]", "pop_sorted([2, 2, -1]) == [-1, 2, 2]", "pop_sorted([1]) == [1]"],
    "heapify": ["smallest_after_heapify([]) is None", "smallest_after_heapify([4, 2, 3]) == 2", "smallest_after_heapify([-1, -3]) == -3", "smallest_after_heapify([5]) == 5"],
    "max_heap": ["top_k_largest([], 2) == []", "top_k_largest([3, 1, 5, 2], 2) == [5, 3]", "top_k_largest([2, 2, 1], 5) == [2, 2, 1]", "top_k_largest([1, 2], 0) == []"],
    "custom_heap": ["schedule_tasks([]) == []", "schedule_tasks([(2, 'b'), (1, 'c'), (1, 'a')]) == ['a', 'c', 'b']", "schedule_tasks([(0, 'x')]) == ['x']", "schedule_tasks([(-1, 'b'), (-1, 'a')]) == ['a', 'b']"],
    "heap_nsmallest": ["n_smallest([], 2) == []", "n_smallest([4, 1, 3, 2], 2) == [1, 2]", "n_smallest([2, 2, 1], 5) == [1, 2, 2]", "n_smallest([1, 2], 0) == []"],
    "heap_nlargest": ["n_largest([], 2) == []", "n_largest([4, 1, 3, 2], 2) == [4, 3]", "n_largest([2, 2, 1], 5) == [2, 2, 1]", "n_largest([1, 2], 0) == []"],
    "sorted_dict_basics": ["sorted_items({}) == []", "sorted_items({'b': 2, 'a': 1}) == [('a', 1), ('b', 2)]", "sorted_items({'x': -1}) == [('x', -1)]", "sorted_items({'aa': 2, 'a': 1}) == [('a', 1), ('aa', 2)]"],
    "sorted_set_basics": ["sorted_unique([]) == []", "sorted_unique([3, 1, 3, 2]) == [1, 2, 3]", "sorted_unique([-1, -1, 0]) == [-1, 0]", "sorted_unique([2, 1]) == [1, 2]"],
}


def source_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def has_unfinished_raise(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as error:
        if source.startswith('        """') and 'raise NotImplementedError("TODO: CI' in source:
            return True
        raise RuntimeError(f"사용자 파일에 문법 오류가 있어 보존합니다: {path}: {error}") from error
    for node in ast.walk(tree):
        if not isinstance(node, ast.Raise):
            continue
        exception = node.exc
        if isinstance(exception, ast.Name) and exception.id == "NotImplementedError":
            return True
        if isinstance(exception, ast.Call) and isinstance(exception.func, ast.Name):
            if exception.func.id == "NotImplementedError":
                return True
    return False


def selected_tests(seed: Seed, variant_number: int) -> list[str]:
    tests = TESTS[seed.slug]
    offset = (variant_number - 2) % len(tests)
    return [tests[(offset + index) % len(tests)] for index in range(3)]


def render_variant(seed: Seed, seed_number: int, variant_number: int, problem_id: int) -> str:
    profile = PROFILES[seed.chapter][variant_number - 2]
    tests = selected_tests(seed, variant_number)
    assertions = "\n".join(f"    assert {expression}" for expression in tests)
    tests_as_text = "\n".join(f"- {expression}" for expression in tests)
    docstring = f'''"""
CI{problem_id:04d} — {seed.title} / {profile.title}

Chapter: {seed.chapter}
Seed: {seed_number:02d} / 40
Variant: {variant_number:02d} / 20
Time cap: {profile.time_cap} seconds

기본 베이스
-----------
{seed.task}

변형 시나리오
-------------
{profile.instruction}

공개 예시
---------
{tests[0]}

전용 테스트
---------
{tests_as_text}

완료 조건
---------
1. 기본 함수의 공개 계약을 유지한다.
2. 변형 시나리오에 필요한 보조 함수·테스트를 직접 추가한다.
3. 아래 self_test()의 세 assert를 모두 통과한다.
4. 시간·공간복잡도를 마지막 주석에 적는다.
5. 답안을 보며 타이핑한 코드는 완료로 세지 않는다.
6. 마지막에는 NotImplementedError를 제거한다.
"""'''
    starter = f"{seed.signature}\n    raise NotImplementedError(\"TODO: CI{problem_id:04d}\")"
    self_test = f"def self_test() -> None:\n{assertions}"
    return f"{docstring}\n\n{starter}\n\n\n{self_test}\n"


def problem_id(seed_number: int, variant_number: int) -> int:
    return (seed_number - 1) * 20 + variant_number


def legacy_main() -> None:
    if len(SEEDS) != 40 or len(TESTS) != 40:
        raise RuntimeError("40 seed와 40 test set이 필요합니다.")
    for chapter, profiles in PROFILES.items():
        if len(profiles) != 19:
            raise RuntimeError(f"{chapter}: expected 19 profiles, found {len(profiles)}")

    baseline_files = sorted(ROOT.rglob("CI*_v01_*.py"))
    if len(baseline_files) != 40:
        raise RuntimeError(f"expected 40 v01 baselines, found {len(baseline_files)}")
    baseline_hashes = {path.relative_to(ROOT).as_posix(): source_hash(path) for path in baseline_files}

    generated = 0
    preserved = 0
    index_lines = [
        "# Python Coding Interview 800 Problem Index",
        "",
        "40개 seed × 20개 변형 = 800개 문제입니다. v01은 원본 baseline이고 v02~v20은 챕터별 시나리오와 전용 테스트를 가집니다.",
        "",
    ]

    for seed_number, seed in enumerate(SEEDS, start=1):
        index_lines.extend([f"## {seed.chapter} — {seed.title}", ""])
        baseline_id = problem_id(seed_number, 1)
        baseline_matches = sorted(ROOT.rglob(f"CI{baseline_id:04d}_*_v01_*.py"))
        if len(baseline_matches) != 1:
            raise RuntimeError(f"CI{baseline_id:04d}: baseline file count={len(baseline_matches)}")
        baseline_path = baseline_matches[0]
        index_lines.append(
            f"- [CI{baseline_id:04d} — {seed.title} / 기본 구현]({baseline_path.relative_to(ROOT).as_posix()})"
        )

        for variant_number in range(2, 21):
            current_id = problem_id(seed_number, variant_number)
            existing = sorted(ROOT.rglob(f"CI{current_id:04d}_*.py"))
            if len(existing) != 1:
                raise RuntimeError(f"CI{current_id:04d}: existing file count={len(existing)}")
            existing_path = existing[0]
            profile = PROFILES[seed.chapter][variant_number - 2]
            if not has_unfinished_raise(existing_path):
                preserved += 1
                output_path = existing_path
            else:
                output_path = existing_path.parent / (
                    f"CI{current_id:04d}_{seed.slug}_v{variant_number:02d}_{profile.slug}.py"
                )
                if output_path != existing_path:
                    existing_path.unlink()
                output_path.write_text(
                    render_variant(seed, seed_number, variant_number, current_id),
                    encoding="utf-8",
                )
                generated += 1
            index_lines.append(
                f"- [CI{current_id:04d} — {seed.title} / {profile.title}]({output_path.relative_to(ROOT).as_posix()})"
            )
        index_lines.append("")

    after_hashes = {path.relative_to(ROOT).as_posix(): source_hash(path) for path in baseline_files}
    if baseline_hashes != after_hashes:
        raise RuntimeError("v01 baseline hash changed")

    all_problems = sorted(ROOT.rglob("CI*.py"))
    if len(all_problems) != 800:
        raise RuntimeError(f"expected 800 problems, found {len(all_problems)}")

    (ROOT / "INDEX.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    report = [
        "# Variant Regeneration Report",
        "",
        f"- v01 preserved: {len(baseline_files)}",
        f"- v02-v20 regenerated: {generated}",
        f"- completed variants preserved: {preserved}",
        f"- total problems: {len(all_problems)}",
        "",
        "## Frozen v01 SHA-256",
        "",
    ]
    report.extend(f"- `{digest}` `{path}`" for path, digest in sorted(baseline_hashes.items()))
    (ROOT / "REGENERATION_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"v01_preserved={len(baseline_files)}")
    print(f"variants_regenerated={generated}")
    print(f"completed_variants_preserved={preserved}")
    print(f"total={len(all_problems)}")


def main() -> None:
    from quality_regenerate import main as quality_main

    quality_main()


if __name__ == "__main__":
    main()
