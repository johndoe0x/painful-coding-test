from __future__ import annotations

import ast
from collections import Counter
from io import StringIO
import tokenize


CHECK_DESCRIPTIONS = {
    "assignment": "함수 본문에서 지역 변수 할당을 사용한다.",
    "reassignment": "같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.",
    "multiple_assignment": "tuple/list 다중 할당 또는 swap 형태를 사용한다.",
    "augassign": "+=, -=, *= 같은 복합 할당 연산자를 사용한다.",
    "comment": "함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.",
    "no_global": "global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.",
    "global_read": "문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.",
    "bool_or": "논리 연산자 or를 사용한다.",
    "bool_and": "논리 연산자 and를 사용한다.",
    "bool_not": "논리 연산자 not을 사용한다.",
    "if": "if문을 사용한다.",
    "if_else": "else 경로가 있는 if문을 사용한다.",
    "elif": "elif 경로를 사용한다.",
    "while": "while문을 사용한다.",
    "for": "for문을 사용한다.",
    "range": "range()를 사용한다.",
    "nested_loop": "반복문 안에 반복문을 중첩해 사용한다.",
    "break_or_continue": "break 또는 continue를 사용한다.",
    "comprehension": "comprehension 표현식을 사용한다.",
    "slice": "슬라이스 표현식을 사용한다.",
    "reverse_slice": "step이 -1인 역방향 슬라이스를 사용한다.",
    "f_string": "f-string을 사용한다.",
    "append_call": "list.append()를 사용한다.",
    "pop_call": "list.pop()을 사용한다.",
    "dict_items_call": "dict.items()를 사용한다.",
    "try": "try-except를 사용한다.",
    "multiple_except": "함수 안에 둘 이상의 except 블록을 사용한다.",
    "sorted_call": "sorted()를 사용한다.",
    "list_sort_call": "list.sort()를 사용한다.",
    "lambda": "lambda 표현식을 사용한다.",
    "enumerate_call": "enumerate()를 사용한다.",
    "zip_call": "zip()을 사용한다.",
    "iter_call": "iter()를 사용한다.",
    "next_call": "next()를 사용한다.",
    "yield": "yield 또는 yield from으로 generator를 만든다.",
    "tuple_unpack": "대입이나 for 문에서 tuple unpacking을 사용한다.",
    "counter_call": "collections.Counter를 사용한다.",
    "defaultdict_call": "collections.defaultdict를 사용한다.",
    "deque_call": "collections.deque를 사용한다.",
    "heapq_call": "heapq API를 사용한다.",
    "bisect_call": "bisect API를 사용한다.",
    "itertools_call": "itertools API를 사용한다.",
    "cache_decorator": "functools.cache decorator를 사용한다.",
    "lru_cache_decorator": "functools.lru_cache decorator를 사용한다.",
    "cmp_to_key_call": "functools.cmp_to_key를 사용한다.",
    "math_call": "math 모듈의 함수 또는 상수를 사용한다.",
    "itemgetter_call": "operator.itemgetter를 사용한다.",
    "re_call": "re 모듈의 정규표현식 API를 사용한다.",
    "pathlib_call": "pathlib API를 사용한다.",
    "json_call": "json API를 사용한다.",
    "csv_call": "csv API를 사용한다.",
}


SOURCE_CHECKS_BY_SEED: dict[str, tuple[str, ...]] = {
    "comments": ("comment",),
    "variable_declaration": ("assignment",),
    "reassigning_variables": ("reassignment",),
    "multiple_assignments": ("multiple_assignment",),
    "scope": ("no_global",),
    "global_vs_local": ("global_read", "no_global"),
    "shorthand_operators": ("augassign",),
    "boolean_or": ("bool_or",),
    "boolean_and": ("bool_and",),
    "boolean_negation": ("bool_not",),
    "if_statements": ("if",),
    "if_scope": ("if",),
    "if_else": ("if_else",),
    "elif_statements": ("elif",),
    "truthy_falsy": ("if",),
    "while_loops": ("while",),
    "while_counting": ("while",),
    "while_multiples": ("while",),
    "for_loops": ("for",),
    "for_loops_start": ("for", "range"),
    "for_loops_step": ("for", "range"),
    "for_loops_reverse": ("for", "range"),
    "nested_loops": ("nested_loop",),
    "control_flow": ("break_or_continue",),
    "string_looping": ("for",),
    "string_looping_shorthand": ("comprehension",),
    "string_slicing_1": ("slice",),
    "string_slicing_2": ("slice",),
    "reverse_string": ("reverse_slice",),
    "string_formatting": ("f_string",),
    "list_looping": ("for",),
    "list_append": ("append_call",),
    "list_pop": ("pop_call",),
    "dict_looping": ("for", "dict_items_call"),
    "try_except": ("try",),
    "error_catching": ("try",),
    "multiple_except": ("try", "multiple_except"),
}


def checks_for_seed(seed_slug: str) -> tuple[str, ...]:
    return SOURCE_CHECKS_BY_SEED.get(seed_slug, ())


def _assigned_names(node: ast.AST) -> list[str]:
    return [
        child.id
        for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Store)
    ]


def _module_names(module: ast.Module) -> set[str]:
    names: set[str] = set()
    for statement in module.body:
        if isinstance(statement, (ast.Assign, ast.AnnAssign)):
            names.update(_assigned_names(statement))
    return names


def _primary_function(module: ast.Module, function_name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in module.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one function named {function_name}, found {len(matches)}")
    return matches[0]


def _import_aliases(module: ast.Module) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for statement in module.body:
        if isinstance(statement, ast.Import):
            for alias in statement.names:
                aliases[alias.asname or alias.name] = alias.name
        elif isinstance(statement, ast.ImportFrom) and statement.module:
            for alias in statement.names:
                aliases[alias.asname or alias.name] = (
                    f"{statement.module}.{alias.name}"
                )
    return aliases


def _qualified_name(node: ast.AST, aliases: dict[str, str]) -> str:
    if isinstance(node, ast.Name):
        return aliases.get(node.id, node.id)
    if isinstance(node, ast.Attribute):
        prefix = _qualified_name(node.value, aliases)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _has_comment(source: str, function: ast.FunctionDef) -> bool:
    lines = source.splitlines(keepends=True)
    segment = "".join(lines[function.lineno - 1 : function.end_lineno])
    try:
        tokens = tokenize.generate_tokens(StringIO(segment).readline)
        return any(token.type == tokenize.COMMENT for token in tokens)
    except tokenize.TokenError:
        return False


def failed_source_checks(
    source: str,
    function_name: str,
    check_names: tuple[str, ...],
) -> list[str]:
    unknown = set(check_names) - CHECK_DESCRIPTIONS.keys()
    if unknown:
        raise ValueError(f"unknown source checks: {sorted(unknown)}")
    module = ast.parse(source)
    function = _primary_function(module, function_name)
    descendants = list(ast.walk(function))
    module_names = _module_names(module)
    import_aliases = _import_aliases(module)
    assignments = [
        node
        for node in descendants
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign))
    ]
    assigned_counts = Counter(
        name
        for assignment in assignments
        for name in _assigned_names(assignment)
    )

    def has_call(attribute: str) -> bool:
        return any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == attribute
            for node in descendants
        )

    call_names = {
        _qualified_name(node.func, import_aliases)
        for node in descendants
        if isinstance(node, ast.Call)
    }

    def calls_api(prefix: str) -> bool:
        return any(
            name == prefix or name.startswith(f"{prefix}.")
            for name in call_names
        )

    def nested_loop() -> bool:
        for loop in descendants:
            if not isinstance(loop, (ast.For, ast.While)):
                continue
            for child in ast.walk(loop):
                if child is not loop and isinstance(child, (ast.For, ast.While)):
                    return True
        return False

    results = {
        "assignment": bool(assignments),
        "reassignment": any(isinstance(node, ast.AugAssign) for node in descendants)
        or any(count >= 2 for count in assigned_counts.values()),
        "multiple_assignment": any(
            isinstance(node, ast.Assign)
            and (
                len(node.targets) > 1
                or any(
                    isinstance(target, (ast.Tuple, ast.List)) and len(target.elts) >= 2
                    for target in node.targets
                )
            )
            for node in descendants
        ),
        "augassign": any(isinstance(node, ast.AugAssign) for node in descendants),
        "comment": _has_comment(source, function),
        "no_global": not any(
            isinstance(node, (ast.Global, ast.Nonlocal)) for node in descendants
        ),
        "global_read": any(
            isinstance(node, ast.Name)
            and isinstance(node.ctx, ast.Load)
            and node.id in module_names
            for node in descendants
        ),
        "bool_or": any(
            isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or)
            for node in descendants
        ),
        "bool_and": any(
            isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And)
            for node in descendants
        ),
        "bool_not": any(
            isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not)
            for node in descendants
        ),
        "if": any(isinstance(node, ast.If) for node in descendants),
        "if_else": any(
            isinstance(node, ast.If) and bool(node.orelse) for node in descendants
        ),
        "elif": any(
            isinstance(node, ast.If)
            and len(node.orelse) == 1
            and isinstance(node.orelse[0], ast.If)
            for node in descendants
        ),
        "while": any(isinstance(node, ast.While) for node in descendants),
        "for": any(isinstance(node, ast.For) for node in descendants),
        "range": any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "range"
            for node in descendants
        ),
        "nested_loop": nested_loop(),
        "break_or_continue": any(
            isinstance(node, (ast.Break, ast.Continue)) for node in descendants
        ),
        "comprehension": any(
            isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp))
            for node in descendants
        ),
        "slice": any(
            isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice)
            for node in descendants
        ),
        "reverse_slice": any(
            isinstance(node, ast.Subscript)
            and isinstance(node.slice, ast.Slice)
            and isinstance(node.slice.step, ast.UnaryOp)
            and isinstance(node.slice.step.op, ast.USub)
            and isinstance(node.slice.step.operand, ast.Constant)
            and node.slice.step.operand.value == 1
            for node in descendants
        ),
        "f_string": any(isinstance(node, ast.JoinedStr) for node in descendants),
        "append_call": has_call("append"),
        "pop_call": has_call("pop"),
        "dict_items_call": has_call("items"),
        "try": any(isinstance(node, ast.Try) for node in descendants),
        "multiple_except": sum(
            len(node.handlers) for node in descendants if isinstance(node, ast.Try)
        )
        >= 2,
        "sorted_call": "sorted" in call_names,
        "list_sort_call": has_call("sort"),
        "lambda": any(isinstance(node, ast.Lambda) for node in descendants),
        "enumerate_call": "enumerate" in call_names,
        "zip_call": "zip" in call_names,
        "iter_call": "iter" in call_names,
        "next_call": "next" in call_names,
        "yield": any(
            isinstance(node, (ast.Yield, ast.YieldFrom)) for node in descendants
        ),
        "tuple_unpack": any(
            isinstance(node, (ast.Tuple, ast.List))
            and isinstance(node.ctx, ast.Store)
            and len(node.elts) >= 2
            for node in descendants
        ),
        "counter_call": "collections.Counter" in call_names,
        "defaultdict_call": "collections.defaultdict" in call_names,
        "deque_call": "collections.deque" in call_names,
        "heapq_call": calls_api("heapq"),
        "bisect_call": calls_api("bisect"),
        "itertools_call": calls_api("itertools"),
        "cache_decorator": any(
            _qualified_name(
                decorator.func if isinstance(decorator, ast.Call) else decorator,
                import_aliases,
            )
            == "functools.cache"
            for candidate in descendants
            if isinstance(candidate, (ast.FunctionDef, ast.AsyncFunctionDef))
            for decorator in candidate.decorator_list
        ),
        "lru_cache_decorator": any(
            _qualified_name(
                decorator.func if isinstance(decorator, ast.Call) else decorator,
                import_aliases,
            )
            == "functools.lru_cache"
            for candidate in descendants
            if isinstance(candidate, (ast.FunctionDef, ast.AsyncFunctionDef))
            for decorator in candidate.decorator_list
        ),
        "cmp_to_key_call": "functools.cmp_to_key" in call_names,
        "math_call": calls_api("math")
        or any(
            _qualified_name(node, import_aliases).startswith("math.")
            for node in descendants
            if isinstance(node, ast.Attribute)
        ),
        "itemgetter_call": "operator.itemgetter" in call_names,
        "re_call": calls_api("re"),
        "pathlib_call": calls_api("pathlib"),
        "json_call": calls_api("json"),
        "csv_call": calls_api("csv"),
    }
    return [name for name in check_names if not results[name]]
