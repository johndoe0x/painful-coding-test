"""Catalog-author verification. Reference answers NEVER enter learner starters.

Literal goldens, non-public cases, exhaustive alternate oracles, and deliberately
wrong algorithms verify the 48 contracts independently of generator rendering.
"""

from collections import Counter, deque
from copy import deepcopy
from functools import lru_cache
from itertools import combinations, permutations, product
import heapq
import unittest

from python_coding.diversity_catalog import REPLACEMENTS
from python_coding.quality_catalog import TEMPLATES


def interval_schedule(intervals):
    end, result = float("-inf"), 0
    for start, stop in sorted(intervals, key=lambda pair: pair[1]):
        if start >= end:
            end, result = stop, result + 1
    return result


def closed_interval_arrows(intervals):
    point, result = float("-inf"), 0
    for start, stop in sorted(intervals, key=lambda pair: pair[1]):
        if start > point:
            point, result = stop, result + 1
    return result


def partition_labels(text):
    last = {letter: i for i, letter in enumerate(text)}
    result, start, stop = [], 0, 0
    for i, letter in enumerate(text):
        stop = max(stop, last[letter])
        if i == stop:
            result.append(i - start + 1)
            start = i + 1
    return result


def minimum_jumps(jumps):
    if len(jumps) < 2:
        return 0
    stop = farthest = count = 0
    for i in range(len(jumps) - 1):
        farthest = max(farthest, i + jumps[i])
        if i == stop:
            if farthest == stop:
                return -1
            count += 1
            stop = farthest
            if stop >= len(jumps) - 1:
                return count
    return -1


def minimum_candy(ratings):
    count = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            count[i] = count[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            count[i] = max(count[i], count[i + 1] + 1)
    return sum(count)


def rescue_boats(weights, limit):
    ordered = sorted(weights)
    left, right, count = 0, len(weights) - 1, 0
    while left <= right:
        if ordered[left] + ordered[right] <= limit:
            left += 1
        right -= 1
        count += 1
    return count


def single_unpaired(values):
    result = 0
    for value in values:
        result ^= value
    return result


def two_unpaired(values):
    combined = single_unpaired(values)
    split = combined & -combined
    first = second = 0
    for value in values:
        if value & split:
            first ^= value
        else:
            second ^= value
    return tuple(sorted((first, second)))


def reverse_fixed_bits(value, width):
    result = 0
    for _ in range(width):
        result = result * 2 + (value & 1)
        value >>= 1
    return result


def range_bitwise_and(left, right):
    shifts = 0
    while left != right:
        left >>= 1
        right >>= 1
        shifts += 1
    return left << shifts


def total_hamming_distance(values):
    result = 0
    for bit in range(16):
        ones = sum((value >> bit) & 1 for value in values)
        result += ones * (len(values) - ones)
    return result


def bit_count_table(n):
    result = [0] * (n + 1)
    for value in range(1, n + 1):
        result[value] = result[value >> 1] + (value & 1)
    return result


def linked_reverse(links, head):
    result = links[:]
    previous, current = -1, head
    while current != -1:
        following = result[current]
        result[current] = previous
        previous, current = current, following
    return previous, result


def linked_remove_nth(links, head, n):
    result = links[:]
    fast = head
    for _ in range(n):
        fast = links[fast]
    if fast == -1:
        result[head] = -1
        return links[head], result
    slow = head
    while links[fast] != -1:
        slow, fast = links[slow], links[fast]
    removed = links[slow]
    result[slow] = links[removed]
    result[removed] = -1
    return head, result


def linked_middle(links, head):
    slow = fast = head
    while fast != -1 and links[fast] != -1:
        slow, fast = links[slow], links[links[fast]]
    return slow


def linked_cycle_entry(links, head):
    slow = fast = head
    while fast != -1 and links[fast] != -1:
        slow = links[slow]
        fast = links[links[fast]]
        if slow == fast:
            slow = head
            while slow != fast:
                slow, fast = links[slow], links[fast]
            return slow
    return -1


def linked_intersection(links, left, right):
    first, second = left, right
    while first != second:
        first = right if first == -1 else links[first]
        second = left if second == -1 else links[second]
    return first


def linked_reorder(links, head):
    order, current = [], head
    while current != -1:
        order.append(current)
        current = links[current]
    alternating = []
    left, right = 0, len(order) - 1
    while left <= right:
        alternating.append(order[left])
        if left != right:
            alternating.append(order[right])
        left, right = left + 1, right - 1
    result = links[:]
    for i, node in enumerate(alternating):
        result[node] = alternating[i + 1] if i + 1 < len(alternating) else -1
    return head, result


def tree_preorder(nodes, root):
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        if node != -1:
            value, left, right = nodes[node]
            result.append(value)
            stack.extend((right, left))
    return result


def tree_levels(nodes, root):
    result, queue = [], deque([] if root == -1 else [root])
    while queue:
        row = []
        for _ in range(len(queue)):
            value, left, right = nodes[queue.popleft()]
            row.append(value)
            queue.extend(child for child in (left, right) if child != -1)
        result.append(row)
    return result


def validate_bst(nodes, root):
    def visit(node, low, high):
        if node == -1:
            return True
        value, left, right = nodes[node]
        return low < value < high and visit(left, low, value) and visit(right, value, high)
    return visit(root, float("-inf"), float("inf"))


def tree_balanced(nodes, root):
    def height(node):
        if node == -1:
            return 0
        _, left, right = nodes[node]
        first, second = height(left), height(right)
        if first < 0 or second < 0 or abs(first - second) > 1:
            return -1
        return 1 + max(first, second)
    return height(root) >= 0


def tree_diameter(nodes, root):
    result = 0
    def height(node):
        nonlocal result
        if node == -1:
            return 0
        _, left, right = nodes[node]
        first, second = height(left), height(right)
        result = max(result, first + second)
        return max(first, second) + 1
    height(root)
    return result


def tree_target_paths(nodes, root, target):
    result = []
    def visit(node, remaining, path):
        if node == -1:
            return
        value, left, right = nodes[node]
        current = path + [value]
        if left == right == -1 and value == remaining:
            result.append(current)
        visit(left, remaining - value, current)
        visit(right, remaining - value, current)
    visit(root, target, [])
    return result


def obstacle_path_count(grid):
    if not grid or not grid[0]:
        return 0
    paths = [0] * len(grid[0])
    paths[0] = 1
    for row in grid:
        for column, blocked in enumerate(row):
            if blocked:
                paths[column] = 0
            elif column:
                paths[column] += paths[column - 1]
    return paths[-1]


def edit_distance(left, right):
    previous = list(range(len(right) + 1))
    for i, first in enumerate(left, 1):
        current = [i]
        for j, second in enumerate(right, 1):
            current.append(min(previous[j] + 1, current[-1] + 1, previous[j - 1] + (first != second)))
        previous = current
    return previous[-1]


def maximal_square(grid):
    if not grid or not grid[0]:
        return 0
    previous = [0] * (len(grid[0]) + 1)
    result = 0
    for row in grid:
        current = [0]
        for j, value in enumerate(row, 1):
            current.append(1 + min(previous[j], previous[j - 1], current[-1]) if value else 0)
            result = max(result, current[-1])
        previous = current
    return result * result


def word_search(board, word):
    if not word:
        return True
    rows, columns = len(board), len(board[0]) if board else 0
    def visit(row, column, index, used):
        if not (0 <= row < rows and 0 <= column < columns) or (row, column) in used:
            return False
        if board[row][column] != word[index]:
            return False
        if index + 1 == len(word):
            return True
        used.add((row, column))
        found = any(visit(row + dr, column + dc, index + 1, used)
                    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)))
        used.remove((row, column))
        return found
    return any(visit(row, column, 0, set()) for row in range(rows) for column in range(columns))


def n_queens(n):
    result = []
    def visit(path, columns, descending, ascending):
        row = len(path)
        if row == n:
            result.append(tuple(path))
            return
        for column in range(n):
            if column not in columns and row - column not in descending and row + column not in ascending:
                visit(path + [column], columns | {column}, descending | {row - column}, ascending | {row + column})
    visit([], set(), set(), set())
    return result


def longest_increasing_grid_path(grid):
    if not grid or not grid[0]:
        return 0
    rows, columns = len(grid), len(grid[0])
    @lru_cache(None)
    def visit(row, column):
        best = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, column + dc
            if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] > grid[row][column]:
                best = max(best, 1 + visit(nr, nc))
        return best
    return max(visit(row, column) for row in range(rows) for column in range(columns))


def trie_prefix_counts(words, prefixes):
    root = {"#": 0}
    for word in words:
        node = root
        node["#"] += 1
        for letter in word:
            node = node.setdefault(letter, {"#": 0})
            node["#"] += 1
    result = []
    for prefix in prefixes:
        node = root
        for letter in prefix:
            node = node.get(letter, {})
        result.append(node.get("#", 0))
    return result


def shortest_unique_prefixes(words):
    counts = Counter(word[:length] for word in words for length in range(1, len(word) + 1))
    return [next((word[:length] for length in range(1, len(word) + 1) if counts[word[:length]] == 1), None)
            for word in words]


def trie_wildcard_matches(words, pattern):
    root = {}
    for word in words:
        node = root
        for letter in word:
            node = node.setdefault(letter, {})
        node["#"] = word
    result = []
    def visit(node, i):
        if i == len(pattern):
            if "#" in node:
                result.append(node["#"])
            return
        if pattern[i] == ".":
            for letter, child in node.items():
                if letter != "#":
                    visit(child, i + 1)
        elif pattern[i] in node:
            visit(node[pattern[i]], i + 1)
    visit(root, 0)
    return sorted(result)


def graph_bipartite(n, edges):
    graph = [[] for _ in range(n)]
    for left, right in edges:
        graph[left].append(right)
        graph[right].append(left)
    colors = {}
    for root in range(n):
        if root in colors:
            continue
        colors[root] = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in colors:
                    colors[neighbor] = colors[node] ^ 1
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
    return True


def connectivity_queries(n, edges, queries):
    parent = list(range(n))
    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    for left, right in edges:
        parent[find(left)] = find(right)
    return [find(left) == find(right) for left, right in queries]


def graph_bfs_distances(n, edges, source):
    graph = [[] for _ in range(n)]
    for left, right in edges:
        graph[left].append(right)
    result = [-1] * n
    result[source] = 0
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if result[neighbor] == -1:
                result[neighbor] = result[node] + 1
                queue.append(neighbor)
    return result


def dijkstra_distances(n, edges, source):
    graph = [[] for _ in range(n)]
    for left, right, weight in edges:
        graph[left].append((right, weight))
    distances = [float("inf")] * n
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph[node]:
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    return [None if distance == float("inf") else distance for distance in distances]


def lexicographic_toposort(n, edges):
    graph = [set() for _ in range(n)]
    degree = [0] * n
    for left, right in edges:
        if right not in graph[left]:
            graph[left].add(right)
            degree[right] += 1
    ready = [node for node in range(n) if not degree[node]]
    heapq.heapify(ready)
    result = []
    while ready:
        node = heapq.heappop(ready)
        result.append(node)
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if not degree[neighbor]:
                heapq.heappush(ready, neighbor)
    return result if len(result) == n else None


def bounded_flight_cost(n, flights, source, target, stops):
    distance = [float("inf")] * n
    distance[source] = 0
    for _ in range(stops + 1):
        following = distance[:]
        for left, right, cost in flights:
            following[right] = min(following[right], distance[left] + cost)
        distance = following
    return -1 if distance[target] == float("inf") else distance[target]


def minimum_spanning_tree(n, edges):
    if n < 2:
        return 0
    parent = list(range(n))
    def find(node):
        if node != parent[node]:
            parent[node] = find(parent[node])
        return parent[node]
    result, count = 0, 0
    for left, right, weight in sorted(edges, key=lambda edge: edge[2]):
        left, right = find(left), find(right)
        if left != right:
            parent[left] = right
            result += weight
            count += 1
    return result if count == n - 1 else None


def minimum_effort_grid(heights):
    if not heights or not heights[0]:
        return 0
    rows, columns = len(heights), len(heights[0])
    distance = {(0, 0): 0}
    queue = [(0, 0, 0)]
    while queue:
        effort, row, column = heapq.heappop(queue)
        if effort != distance[row, column]:
            continue
        if (row, column) == (rows - 1, columns - 1):
            return effort
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, column + dc
            if 0 <= nr < rows and 0 <= nc < columns:
                candidate = max(effort, abs(heights[row][column] - heights[nr][nc]))
                if candidate < distance.get((nr, nc), float("inf")):
                    distance[nr, nc] = candidate
                    heapq.heappush(queue, (candidate, nr, nc))


def single_cpu_order(tasks):
    arriving = sorted((start, duration, index) for index, (start, duration) in enumerate(tasks))
    queue, result = [], []
    time = index = 0
    while index < len(tasks) or queue:
        if not queue:
            time = max(time, arriving[index][0])
        while index < len(tasks) and arriving[index][0] <= time:
            _, duration, original = arriving[index]
            heapq.heappush(queue, (duration, original))
            index += 1
        duration, original = heapq.heappop(queue)
        time += duration
        result.append(original)
    return result


def weighted_interval_profit(jobs):
    from bisect import bisect_right
    ordered = sorted(jobs, key=lambda job: job[1])
    ends, best = [], [0]
    for start, stop, profit in ordered:
        best.append(max(best[-1], profit + best[bisect_right(ends, start)]))
        ends.append(stop)
    return best[-1]


def minimum_coins(coins, amount):
    best = [0] + [amount + 1] * amount
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin <= subtotal:
                best[subtotal] = min(best[subtotal], best[subtotal - coin] + 1)
    return best[-1] if best[-1] <= amount else -1


def coin_combination_count(coins, amount):
    counts = [1] + [0] * amount
    for coin in sorted(set(coins)):
        for subtotal in range(coin, amount + 1):
            counts[subtotal] += counts[subtotal - coin]
    return counts[-1]


def equal_subset_partition(values):
    total = sum(values)
    if total % 2:
        return False
    reachable = {0}
    for value in values:
        reachable |= {subtotal + value for subtotal in reachable}
    return total // 2 in reachable


def unique_permutations(values):
    counts = Counter(values)
    result = []
    def visit(path):
        if len(path) == len(values):
            result.append(tuple(path))
            return
        for value in sorted(counts):
            if counts[value]:
                counts[value] -= 1
                visit(path + [value])
                counts[value] += 1
    visit([])
    return result


def single_use_combination_sum(values, target):
    ordered, result = sorted(values), []
    def visit(start, remaining, path):
        if remaining == 0:
            result.append(tuple(path))
            return
        for i in range(start, len(ordered)):
            if i > start and ordered[i] == ordered[i - 1]:
                continue
            if ordered[i] > remaining:
                break
            visit(i + 1, remaining - ordered[i], path + [ordered[i]])
    visit(0, target, [])
    return result


REFERENCES = {number: globals()[template.slug] for number, template in REPLACEMENTS.items()}


# Hand-calculated independent cases, not produced by the references above.
EXTRA_CASES = {
    22: [(([(0, 4), (1, 2), (2, 3), (3, 5)],), 3)],
    23: [(([(1, 4), (2, 5), (3, 6), (7, 9)],), 2)],
    24: [(('eccbbbbdec',), [10])],
    25: [(([1, 2, 0, 1, 0],), 3)],
    26: [(([1, 3, 2, 2, 1],), 7)],
    27: [(([2, 3, 4, 5], 7), 2)],
    122: [(([0, -7, 0, 9, 9],), -7)],
    123: [(([-5, -2, 1, 1, 9, 9],), (-5, -2))],
    124: [((1, 32), 2147483648)],
    125: [((26, 30), 24)],
    126: [(([1, 1, 2, 2],), 8)],
    127: [((10,), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])],
    242: [(([3, 1, -1, 2], 0), (2, [-1, 1, 3, 0]))],
    243: [(([3, 1, -1, 2], 0, 1), (0, [3, 1, -1, -1]))],
    244: [(([3, 1, -1, 2], 0), 3)],
    245: [(([3, 1, 3, 2], 0), 3)],
    246: [(([3, 4, -1, 2, 3], 0, 1), 3)],
    247: [(([1, 2, 3, 4, -1], 0), (0, [4, 3, -1, 2, 1]))],
    362: [(([(9, -1, -1), (4, -1, 2), (5, 0, -1)], 1), [4, 5, 9])],
    363: [(([(9, -1, -1), (4, -1, 2), (5, 0, -1)], 1), [[4], [5], [9]])],
    364: [(([(10, 1, -1), (5, -1, 2), (12, -1, -1)], 0), False)],
    365: [(([(0, 1, 4), (1, 2, -1), (2, 3, -1), (3, -1, -1), (4, -1, 5), (5, -1, -1)], 0), False)],
    366: [(([(0, 1, -1), (1, 2, -1), (2, 3, -1), (3, -1, -1)], 0), 3)],
    367: [(([(1, 1, 2), (-1, -1, -1), (0, 3, -1), (-1, -1, -1)], 0, 0), [[1, -1], [1, 0, -1]])],
    422: [(([[0, 0, 0], [0, 0, 0]],), 3)],
    423: [(('intention', 'execution'), 5)],
    424: [(([[1, 1, 1], [1, 1, 1], [1, 1, 1]],), 9)],
    425: [(([['a', 'b', 'c'], ['d', 'e', 'f']], 'abed'), True)],
    426: [((5,), [(0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), (2, 0, 3, 1, 4), (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2), (4, 2, 0, 3, 1)])],
    427: [(([[-3, -2, -1], [-4, 1, 0]],), 6)],
    482: [((['aa', 'aa', 'ab', ''], ['a', '', 'aa', 'b']), [3, 4, 2, 0])],
    483: [((['zebra', 'dog', 'duck', 'dove'],), ['z', 'dog', 'du', 'dov'])],
    484: [((['a', 'b', 'aa', '', 'b'], '.'), ['a', 'b'])],
    485: [((6, [(0, 1), (2, 3), (3, 4), (4, 5), (5, 2)]), True)],
    486: [((4, [(2, 3), (1, 2), (0, 1)], [(0, 3), (3, 0), (2, 2)]), [True, True, True])],
    487: [((4, [(3, 2), (2, 1), (1, 3)], 3), [-1, 2, 1, 0])],
    642: [((4, [(3, 1, 2), (1, 0, 4), (3, 0, 9)], 3), [6, 2, None, 0])],
    643: [((4, [(3, 0), (3, 1)]), [2, 3, 0, 1])],
    644: [((5, [(0, 1, 1), (1, 2, 1), (0, 2, 5), (2, 3, 1), (3, 4, 1)], 0, 4, 2), 7)],
    645: [((4, [(0, 1, -2), (1, 2, -1), (0, 2, 1), (2, 3, 5), (1, 3, 6), (3, 3, -99)]), 2)],
    646: [(([[1, 2, 3], [3, 8, 4], [5, 3, 5]],), 1)],
    647: [(([(10, 2), (0, 8), (1, 1), (8, 1)],), [1, 2, 3, 0])],
    782: [(([(0, 5, 10), (0, 2, 6), (2, 5, 6), (5, 7, -1)],), 12)],
    783: [(([3, 7], 12), 4)],
    784: [(([2, 3, 5], 10), 4)],
    785: [(([2, 2, 3, 5],), False)],
    786: [(([2, 1, 2],), [(1, 2, 2), (2, 1, 2), (2, 2, 1)])],
    787: [(([1, 1, 1, 2, 2], 4), [(1, 1, 2), (2, 2)])],
}


def _path(links, head):
    result = []
    while head != -1:
        result.append(head)
        head = links[head]
    return result


def _start_sorted_schedule(intervals):
    result, stop = 0, float("-inf")
    for left, right in sorted(intervals):
        if left >= stop:
            stop, result = right, result + 1
    return result


def _jump_full_distance(jumps):
    node = count = 0
    while node < len(jumps) - 1:
        if not jumps[node]:
            return -1
        node += jumps[node]
        count += 1
    return count


def _one_sided_candy(ratings):
    result, previous = 0, 1
    for i, value in enumerate(ratings):
        previous = previous + 1 if i and value > ratings[i - 1] else 1
        result += previous
    return result


def _floyd_collision(links, head):
    slow = fast = head
    while fast != -1 and links[fast] != -1:
        slow, fast = links[slow], links[links[fast]]
        if slow == fast:
            return slow
    return -1


def _height(nodes, root):
    return 0 if root == -1 else 1 + max(_height(nodes, nodes[root][1]), _height(nodes, nodes[root][2]))


def _inorder(nodes, root):
    if root == -1:
        return []
    value, left, right = nodes[root]
    return _inorder(nodes, left) + [value] + _inorder(nodes, right)


def _local_bst(nodes, root):
    if root == -1:
        return True
    value, left, right = nodes[root]
    return (left == -1 or nodes[left][0] < value) and (right == -1 or nodes[right][0] > value) and _local_bst(nodes, left) and _local_bst(nodes, right)


def _prefix_sum_paths(nodes, root, target):
    result = []
    def visit(node, path):
        if node == -1:
            return
        value, left, right = nodes[node]
        path = path + [value]
        if sum(path) == target:
            result.append(path)
        visit(left, path)
        visit(right, path)
    visit(root, [])
    return result


def _bipartite_only_zero(n, edges):
    reachable = set(_reachable(n, edges, 0)) if n else set()
    return graph_bipartite(n, [(a, b) for a, b in edges if a in reachable and b in reachable])


def _reachable(n, edges, start):
    visited, queue = {start}, [start]
    for node in queue:
        for left, right in edges:
            if node in (left, right):
                neighbor = right if node == left else left
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return visited


def _fifo_toposort(n, edges):
    degree = [0] * n
    for _, right in set(edges):
        degree[right] += 1
    queue = [i for i in range(n) if degree[i] == 0]
    for node in queue:
        for left, right in sorted(set(edges)):
            if left == node:
                degree[right] -= 1
                if degree[right] == 0:
                    queue.append(right)
    return queue if len(queue) == n else None


def _inplace_flight_relaxation(n, flights, source, target, stops):
    distance = [float("inf")] * n
    distance[source] = 0
    for _ in range(stops + 1):
        for left, right, cost in flights:
            distance[right] = min(distance[right], distance[left] + cost)
    return -1 if distance[target] == float("inf") else distance[target]


def _sum_effort_grid(heights):
    if not heights or not heights[0]:
        return 0
    rows, columns = len(heights), len(heights[0])
    edges = []
    for row in range(rows):
        for column in range(columns):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    edges.append((row * columns + column, nr * columns + nc, abs(heights[row][column] - heights[nr][nc])))
    return dijkstra_distances(rows * columns, edges, 0)[-1]


def _greedy_profit(jobs):
    result, stop = 0, float("-inf")
    for start, end, profit in sorted(jobs, key=lambda job: job[1]):
        if start >= stop and profit > 0:
            stop, result = end, result + profit
    return result


def _greedy_coins(coins, amount):
    result = 0
    for coin in sorted(set(coins), reverse=True):
        result += amount // coin
        amount %= coin
    return result if not amount else -1


def _ordered_coin_sequences(coins, amount):
    counts = [1] + [0] * amount
    for subtotal in range(1, amount + 1):
        counts[subtotal] = sum(counts[subtotal - coin] for coin in set(coins) if coin <= subtotal)
    return counts[-1]


def _unbounded_partition(values):
    if sum(values) % 2:
        return False
    return minimum_coins([value for value in values if value], sum(values) // 2) >= 0


def _unlimited_combinations(values, target):
    values = sorted(set(values))
    result = []
    def visit(start, remaining, path):
        if remaining == 0:
            result.append(tuple(path))
            return
        for i in range(start, len(values)):
            if values[i] <= remaining:
                visit(i, remaining - values[i], path + [values[i]])
    visit(0, target, [])
    return result


# Each incorrect algorithm has an explicit semantic misconception, not arbitrary
# output corruption. Every one must be rejected by public or extra literal cases.
WRONG_ALGORITHMS = {
    22: ("earliest start instead of earliest finish", _start_sorted_schedule),
    23: ("half-open nonoverlap instead of closed coverage", interval_schedule),
    24: ("each distinct character is a separate partition", lambda text: [text.count(ch) for ch in dict.fromkeys(text)]),
    25: ("always jump the entire available distance", _jump_full_distance),
    26: ("only satisfy left-neighbor ratings", _one_sided_candy),
    27: ("unlimited passengers per boat", lambda weights, limit: (sum(weights) + limit - 1) // limit),
    122: ("discard signs before XOR", lambda values: single_unpaired([abs(value) for value in values])),
    123: ("distinct values rather than single occurrences", lambda values: tuple(sorted(set(values))[:2])),
    124: ("ignore the fixed-width leading zeros", lambda value, width: int(bin(value)[2:][::-1], 2)),
    125: ("AND only the endpoints", lambda left, right: left & right),
    126: ("count ones without pairwise zero frequencies", lambda values: sum(value.bit_count() for value in values)),
    127: ("exclude n from the table", lambda n: [value.bit_count() for value in range(n)]),
    242: ("reverse storage instead of pointers", lambda links, head: (head, links[::-1])),
    243: ("count from beginning instead of end", lambda links, head, n: linked_remove_nth(links, head, len(_path(links, head)) - n + 1)),
    244: ("choose the earlier even-length middle", lambda links, head: _path(links, head)[(len(_path(links, head)) - 1) // 2] if head != -1 else -1),
    245: ("return Floyd meeting point rather than entry", _floyd_collision),
    246: ("smallest shared index rather than first shared node", lambda links, left, right: min(set(_path(links, left)) & set(_path(links, right)), default=-1)),
    247: ("reverse whole chain instead of interleaving", linked_reverse),
    362: ("inorder rather than preorder", _inorder),
    363: ("forget per-level grouping", lambda nodes, root: [tree_preorder(nodes, root)] if root != -1 else []),
    364: ("validate only immediate children", _local_bst),
    365: ("validate balance only at root", lambda nodes, root: root == -1 or abs(_height(nodes, nodes[root][1]) - _height(nodes, nodes[root][2])) <= 1),
    366: ("height instead of arbitrary-node diameter", lambda nodes, root: max(0, _height(nodes, root) - 1)),
    367: ("accept matching non-leaf prefixes", _prefix_sum_paths),
    422: ("ignore interior obstacles", lambda grid: obstacle_path_count([[0 for _ in row] for row in grid])),
    423: ("positional mismatches without shifts", lambda left, right: abs(len(left) - len(right)) + sum(a != b for a, b in zip(left, right))),
    424: ("all one cells form a square", lambda grid: sum(map(sum, grid))),
    425: ("character supply without adjacency", lambda board, word: not (Counter(word) - Counter(ch for row in board for ch in row))),
    426: ("columns distinct but diagonals ignored", lambda n: list(permutations(range(n)))),
    427: ("distinct values without adjacency", lambda grid: len({value for row in grid for value in row})),
    482: ("deduplicate input words", lambda words, prefixes: trie_prefix_counts(list(set(words)), prefixes)),
    483: ("word ending always makes a unique prefix", lambda words: [prefix if prefix is not None else word or None for word, prefix in zip(words, shortest_unique_prefixes(words))]),
    484: ("dot can match any number of characters", lambda words, pattern: sorted({word for word in words if __import__('fnmatch').fnmatchcase(word, pattern.replace('.', '*'))})),
    485: ("ignore disconnected components", _bipartite_only_zero),
    486: ("direct edges instead of transitive reachability", lambda n, edges, queries: [a == b or (a, b) in edges or (b, a) in edges for a, b in queries]),
    487: ("treat directed edges as undirected", lambda n, edges, source: graph_bfs_distances(n, edges + [(b, a) for a, b in edges], source)),
    642: ("BFS ignores weights", lambda n, edges, source: [None if d < 0 else d for d in graph_bfs_distances(n, [(a, b) for a, b, _ in edges], source)]),
    643: ("FIFO availability violates lexicographic order", _fifo_toposort),
    644: ("in-place relaxation consumes extra edges", _inplace_flight_relaxation),
    645: ("take lightest n-1 edges without cycle checks", lambda n, edges: sum(sorted(w for _, _, w in edges)[:max(0, n - 1)]) if len(edges) >= n - 1 else None),
    646: ("minimize sum instead of maximum edge", _sum_effort_grid),
    647: ("globally shortest duration ignores arrivals", lambda tasks: sorted(range(len(tasks)), key=lambda i: (tasks[i][1], i))),
    782: ("unweighted earliest-finish greedy", _greedy_profit),
    783: ("greedily consume largest coin", _greedy_coins),
    784: ("count ordered sequences instead of combinations", _ordered_coin_sequences),
    785: ("reuse a single index repeatedly", _unbounded_partition),
    786: ("retain duplicate index permutations", lambda values: sorted(permutations(values))),
    787: ("reuse candidate indices without limit", _unlimited_combinations),
}


class DiversityCatalogTests(unittest.TestCase):
    def test_exactly_48_distinct_replacement_contracts(self):
        starts = (22, 122, 242, 362, 422, 482, 642, 782)
        self.assertEqual(set(REPLACEMENTS), {start + offset for start in starts for offset in range(6)})
        self.assertEqual(len({template.slug for template in REPLACEMENTS.values()}), 48)
        self.assertEqual(set(EXTRA_CASES), set(REPLACEMENTS))
        existing = {template.slug for templates in TEMPLATES.values() for template in templates}
        for number, template in REPLACEMENTS.items():
            self.assertNotIn(template.slug, existing)
            self.assertNotEqual((number - 1) % 20, 0)
            self.assertEqual(len(template.tests), 3)
            self.assertTrue(300 <= template.time_cap <= 1200)
            self.assertEqual(template.source_checks, ())

    def test_all_public_literal_goldens(self):
        for number, template in REPLACEMENTS.items():
            for expression in template.tests:
                with self.subTest(number=number, expression=expression):
                    self.assertTrue(eval(expression, {"__FN__": REFERENCES[number]}))

    def test_all_extra_literal_goldens_and_input_preservation(self):
        for number, cases in EXTRA_CASES.items():
            for args, expected in cases:
                with self.subTest(number=number, args=args):
                    before = deepcopy(args)
                    self.assertEqual(REFERENCES[number](*args), expected)
                    self.assertEqual(args, before)

    def test_public_suites_reject_input_mutation_for_every_mutable_contract(self):
        checked = set()
        for number, cases in EXTRA_CASES.items():
            if not any(isinstance(arg, list) for arg in cases[0][0]):
                continue
            reference = REFERENCES[number]
            def mutating(*args):
                result = reference(*args)
                for arg in args:
                    if isinstance(arg, list) and arg:
                        if isinstance(arg[0], list):
                            arg[0].append("changed")
                        else:
                            arg.reverse()
                            arg.append("changed")
                        break
                return result
            self.assertTrue(any(not eval(test, {"__FN__": mutating}) for test in REPLACEMENTS[number].tests), number)
            checked.add(number)
        self.assertEqual(len(checked), 42)

    def test_every_contract_rejects_a_semantic_wrong_algorithm(self):
        self.assertEqual(set(WRONG_ALGORITHMS), set(REPLACEMENTS))
        for number, (mistake, wrong) in WRONG_ALGORITHMS.items():
            with self.subTest(number=number, mistake=mistake):
                rejected = any(not eval(test, {"__FN__": wrong}) for test in REPLACEMENTS[number].tests)
                rejected |= any(wrong(*deepcopy(args)) != expected for args, expected in EXTRA_CASES[number])
                self.assertTrue(rejected, mistake)

    def test_exhaustive_greedy_contracts_against_search(self):
        pool = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        for flags in product((0, 1), repeat=len(pool)):
            intervals = [item for item, flag in zip(pool, flags) if flag]
            compatible = lambda chosen: all(b <= c or d <= a for (a, b), (c, d) in combinations(chosen, 2))
            expected = max((len(chosen) for size in range(len(intervals) + 1)
                            for chosen in combinations(intervals, size) if compatible(chosen)), default=0)
            self.assertEqual(interval_schedule(intervals), expected)
            expected_arrows = next(size for size in range(5)
                                   if any(all(any(a <= p <= b for p in points) for a, b in intervals)
                                          for points in combinations(range(4), size)))
            self.assertEqual(closed_interval_arrows(intervals), expected_arrows)
        for size in range(6):
            for letters in product('ab', repeat=size):
                text = ''.join(letters)
                partitions = []
                for cuts in product((0, 1), repeat=max(0, size - 1)):
                    boundaries = [0] + [i + 1 for i, cut in enumerate(cuts) if cut] + [size]
                    chunks = [text[a:b] for a, b in zip(boundaries, boundaries[1:])] if text else []
                    if all(not set(a) & set(b) for a, b in combinations(chunks, 2)):
                        partitions.append([len(chunk) for chunk in chunks])
                result = partition_labels(text)
                self.assertEqual(sum(result), len(text))
                self.assertEqual(len(result), max(map(len, partitions)))
            for jumps in product(range(3), repeat=size):
                distances = [None] * size
                if size:
                    distances[0] = 0
                for i in range(size):
                    if distances[i] is not None:
                        for j in range(i + 1, min(size, i + jumps[i] + 1)):
                            distances[j] = min(distances[j] if distances[j] is not None else size, distances[i] + 1)
                expected = 0 if size < 2 else -1 if distances[-1] is None else distances[-1]
                self.assertEqual(minimum_jumps(list(jumps)), expected)
        for size in range(4):
            for ratings in product(range(3), repeat=size):
                assignments = product(range(1, size + 1), repeat=size)
                expected = min((sum(candies) for candies in assignments
                                if all(ratings[i] <= ratings[j] or candies[i] > candies[j]
                                       for i in range(size) for j in (i - 1, i + 1) if 0 <= j < size)), default=0)
                self.assertEqual(minimum_candy(list(ratings)), expected)
        @lru_cache(None)
        def boats_search(weights, limit):
            if not weights:
                return 0
            best = 1 + boats_search(weights[1:], limit)
            for i in range(1, len(weights)):
                if weights[0] + weights[i] <= limit:
                    best = min(best, 1 + boats_search(weights[1:i] + weights[i + 1:], limit))
            return best
        for weights in product(range(1, 5), repeat=5):
            self.assertEqual(rescue_boats(list(weights), 4), boats_search(weights, 4))

    def test_exhaustive_bit_contracts_and_invariants(self):
        for width in range(9):
            for value in range(1 << width):
                reversed_value = reverse_fixed_bits(value, width)
                expected = int(format(value, f'0{width}b')[::-1], 2) if width else 0
                self.assertEqual(reversed_value, expected)
                self.assertEqual(reverse_fixed_bits(reversed_value, width), value)
        for left in range(32):
            result = left
            for right in range(left, 32):
                result &= right
                self.assertEqual(range_bitwise_and(left, right), result)
        for size in range(5):
            for values in product(range(4), repeat=size):
                expected = sum(bin(a ^ b).count('1') for a, b in combinations(values, 2))
                self.assertEqual(total_hamming_distance(values), expected)
        self.assertEqual(bit_count_table(10000), [bin(i).count('1') for i in range(10001)])
        for first, second in permutations(range(-3, 4), 2):
            duplicates = [value for value in range(-3, 4) if value not in (first, second)]
            self.assertEqual(single_unpaired(duplicates + [first] + duplicates[::-1]), first)
            self.assertEqual(two_unpaired(duplicates + [first, second] + duplicates[::-1]), tuple(sorted((first, second))))

    def test_exhaustive_linked_node_identity_and_invariants(self):
        for size in range(1, 6):
            for order in permutations(range(size)):
                links = [-1] * size + [size]  # Unreachable self-cycle must survive.
                for left, right in zip(order, order[1:]):
                    links[left] = right
                head, reversed_links = linked_reverse(links, order[0])
                self.assertEqual(_path(reversed_links, head), list(reversed(order)))
                self.assertEqual(reversed_links[-1], size)
                self.assertEqual(linked_reverse(reversed_links, head), (order[0], links))
                self.assertEqual(linked_middle(links, order[0]), order[size // 2])
                self.assertEqual(linked_cycle_entry(links, order[0]), -1)
                for nth in range(1, size + 1):
                    new_head, new_links = linked_remove_nth(links, order[0], nth)
                    self.assertEqual(_path(new_links, new_head), list(order[:size - nth] + order[size - nth + 1:]))
                    self.assertEqual(new_links[order[size - nth]], -1)
                    self.assertEqual(new_links[-1], size)
                    cyclic = links[:]
                    cyclic[order[-1]] = order[nth - 1]
                    self.assertEqual(linked_cycle_entry(cyclic, order[0]), order[nth - 1])
                for first in range(size):
                    for second in range(size):
                        self.assertEqual(linked_intersection(links, order[first], order[second]), order[max(first, second)])
                alternating = [order[i // 2] if i % 2 == 0 else order[-1 - i // 2] for i in range(size)]
                new_head, new_links = linked_reorder(links, order[0])
                self.assertEqual(_path(new_links, new_head), alternating)
                self.assertEqual(new_links[-1], size)

    def test_tree_shapes_against_traversal_and_graph_oracles(self):
        @lru_cache(None)
        def shapes(size):
            if not size:
                return (None,)
            return tuple((left, right) for left_size in range(size)
                         for left in shapes(left_size) for right in shapes(size - 1 - left_size))
        for size in range(6):
            for shape in shapes(size):
                nodes = []
                def build(tree):
                    if tree is None:
                        return -1
                    index = len(nodes)
                    nodes.append(None)
                    left, right = build(tree[0]), build(tree[1])
                    nodes[index] = ((index * 3) % 7 - 3, left, right)
                    return index
                root = build(shape)
                self.assertEqual(tree_preorder(nodes, root), [node[0] for node in nodes])
                frontier, levels, paths = ([] if root == -1 else [(root, [])]), [], []
                while frontier:
                    levels.append([nodes[index][0] for index, _ in frontier])
                    following = []
                    for index, prefix in frontier:
                        value, left, right = nodes[index]
                        if left == right == -1:
                            paths.append(prefix + [value])
                        following.extend((child, prefix + [value]) for child in (left, right) if child != -1)
                    frontier = following
                self.assertEqual(tree_levels(nodes, root), levels)
                inorder = _inorder(nodes, root)
                self.assertEqual(validate_bst(nodes, root), all(a < b for a, b in zip(inorder, inorder[1:])))
                balanced = all(abs(_height(nodes, left) - _height(nodes, right)) <= 1 for _, left, right in nodes)
                self.assertEqual(tree_balanced(nodes, root), balanced)
                edges = [(i, child) for i, (_, left, right) in enumerate(nodes) for child in (left, right) if child != -1]
                diameter = 0
                for start in range(size):
                    queue, seen = [(start, 0)], {start}
                    for node, distance in queue:
                        diameter = max(diameter, distance)
                        for left, right in edges:
                            if node in (left, right):
                                child = right if left == node else left
                                if child not in seen:
                                    seen.add(child)
                                    queue.append((child, distance + 1))
                self.assertEqual(tree_diameter(nodes, root), diameter)
                for target in range(-5, 6):
                    self.assertEqual(sorted(tree_target_paths(nodes, root, target)), sorted(path for path in paths if sum(path) == target))

    def test_grid_backtracking_and_dp_against_small_searches(self):
        for flat in product((0, 1), repeat=6):
            grid = [list(flat[:3]), list(flat[3:])]
            def count(row, column):
                if row >= 2 or column >= 3 or grid[row][column]:
                    return 0
                if (row, column) == (1, 2):
                    return 1
                return count(row + 1, column) + count(row, column + 1)
            self.assertEqual(obstacle_path_count(grid), count(0, 0))
            squares = [side * side for side in range(1, 3) for row in range(3 - side) for column in range(4 - side)
                       if all(grid[r][c] for r in range(row, row + side) for c in range(column, column + side))]
            self.assertEqual(maximal_square(grid), max(squares, default=0))
        paths = [path for length in range(1, 5) for path in permutations(range(4), length)
                 if all(abs(a // 2 - b // 2) + abs(a % 2 - b % 2) == 1 for a, b in zip(path, path[1:]))]
        for flat in product(range(3), repeat=4):
            grid = [list(flat[:2]), list(flat[2:])]
            longest = max(len(path) for path in paths if all(flat[a] < flat[b] for a, b in zip(path, path[1:])))
            self.assertEqual(longest_increasing_grid_path(grid), longest)
        for flat in product('ab', repeat=4):
            board = [list(flat[:2]), list(flat[2:])]
            possible = {''.join(flat[i] for i in path) for path in paths} | {''}
            for length in range(5):
                for letters in product('ab', repeat=length):
                    word = ''.join(letters)
                    self.assertEqual(word_search(board, word), word in possible)
        for n in range(7):
            expected = [cols for cols in permutations(range(n))
                        if len({r - c for r, c in enumerate(cols)}) == n and len({r + c for r, c in enumerate(cols)}) == n]
            self.assertEqual(n_queens(n), expected)
        words = ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb']
        for left in words:
            distance, queue = {left: 0}, [left]
            for word in queue:
                candidates = {word[:i] + word[i + 1:] for i in range(len(word))}
                candidates |= {word[:i] + letter + word[i + 1:] for i in range(len(word)) for letter in 'ab'}
                if len(word) < 2:
                    candidates |= {word[:i] + letter + word[i:] for i in range(len(word) + 1) for letter in 'ab'}
                for candidate in candidates:
                    if candidate not in distance:
                        distance[candidate] = distance[word] + 1
                        queue.append(candidate)
            for right in words:
                self.assertEqual(edit_distance(left, right), distance[right])

    def test_trie_contracts_against_string_predicates(self):
        vocabulary = ['', 'a', 'b', 'aa', 'ab']
        patterns = [''] + [''.join(chars) for size in (1, 2) for chars in product('ab.', repeat=size)]
        for size in range(4):
            for words in product(vocabulary, repeat=size):
                expected = [sum(word.startswith(prefix) for word in words) for prefix in vocabulary]
                self.assertEqual(trie_prefix_counts(words, vocabulary), expected)
                prefixes = []
                for i, word in enumerate(words):
                    prefixes.append(next((word[:end] for end in range(1, len(word) + 1)
                                          if all(not other.startswith(word[:end]) for j, other in enumerate(words) if j != i)), None))
                self.assertEqual(shortest_unique_prefixes(words), prefixes)
                for pattern in patterns:
                    expected = sorted({word for word in words if len(word) == len(pattern)
                                       and all(p == '.' or p == ch for p, ch in zip(pattern, word))})
                    self.assertEqual(trie_wildcard_matches(words, pattern), expected)

    def test_small_graphs_against_colors_permutations_and_floyd(self):
        candidates = [(a, b) for a in range(3) for b in range(3) if a != b]
        for flags in product((0, 1), repeat=len(candidates)):
            edges = [edge for edge, present in zip(candidates, flags) if present]
            colorable = any(all(colors[a] != colors[b] for a, b in edges) for colors in product((0, 1), repeat=3))
            self.assertEqual(graph_bipartite(3, edges), colorable)
            queries = list(product(range(3), repeat=2))
            expected = [b in _reachable(3, edges, a) for a, b in queries]
            self.assertEqual(connectivity_queries(3, edges, queries), expected)
            valid_orders = [order for order in permutations(range(3)) if all(order.index(a) < order.index(b) for a, b in edges)]
            self.assertEqual(lexicographic_toposort(3, edges), list(min(valid_orders)) if valid_orders else None)
            weighted = [(a, b, (a + 2 * b) % 4) for a, b in edges]
            for use_weights in (False, True):
                distances = [[0 if a == b else float('inf') for b in range(3)] for a in range(3)]
                for a, b, weight in weighted:
                    distances[a][b] = min(distances[a][b], weight if use_weights else 1)
                for middle in range(3):
                    for left in range(3):
                        for right in range(3):
                            distances[left][right] = min(distances[left][right], distances[left][middle] + distances[middle][right])
                for source in range(3):
                    expected = [(None if use_weights else -1) if d == float('inf') else d for d in distances[source]]
                    actual = dijkstra_distances(3, weighted, source) if use_weights else graph_bfs_distances(3, edges, source)
                    self.assertEqual(actual, expected)
            for source, target in queries:
                for stops in range(3):
                    totals = [0] if source == target else []
                    def walks(node, budget, cost):
                        if not budget:
                            return
                        for left, right, weight in weighted:
                            if left == node:
                                if right == target:
                                    totals.append(cost + weight)
                                walks(right, budget - 1, cost + weight)
                    walks(source, stops + 1, 0)
                    self.assertEqual(bounded_flight_cost(3, weighted, source, target, stops), min(totals, default=-1))

    def test_weighted_graph_and_scheduler_alternate_oracles(self):
        candidates = [(a, b, a - b + 2) for a, b in combinations(range(4), 2)]
        for flags in product((0, 1), repeat=len(candidates)):
            edges = [edge for edge, flag in zip(candidates, flags) if flag]
            costs = [sum(weight for _, _, weight in chosen) for chosen in combinations(edges, 3)
                     if len(_reachable(4, [(a, b) for a, b, _ in chosen], 0)) == 4]
            self.assertEqual(minimum_spanning_tree(4, edges), min(costs) if costs else None)
        for flat in product(range(3), repeat=4):
            grid = [list(flat[:2]), list(flat[2:])]
            adjacent = [(0, 1), (0, 2), (1, 3), (2, 3)]
            expected = next(limit for limit in range(3) if 3 in _reachable(4, [(a, b) for a, b in adjacent if abs(flat[a] - flat[b]) <= limit], 0))
            self.assertEqual(minimum_effort_grid(grid), expected)
        task_options = [(start, duration) for start in range(3) for duration in (1, 2)]
        for tasks in product(task_options, repeat=3):
            remaining, order, time = set(range(3)), [], 0
            while remaining:
                available = [i for i in remaining if tasks[i][0] <= time]
                if not available:
                    time += 1
                    continue
                chosen = min(available, key=lambda i: (tasks[i][1], i))
                order.append(chosen)
                remaining.remove(chosen)
                time += tasks[chosen][1]
            self.assertEqual(single_cpu_order(tasks), order)

    def test_ordered_dp_and_backtracking_against_enumeration(self):
        options = [(0, 1, -1), (0, 2, 5), (1, 2, 3), (2, 3, 4), (1, 3, 8)]
        for flags in product((0, 1), repeat=len(options)):
            jobs = [job for job, flag in zip(options, flags) if flag]
            profits = [sum(job[2] for job in chosen) for count in range(len(jobs) + 1) for chosen in combinations(jobs, count)
                       if all(b <= c or d <= a for (a, b, _), (c, d, _) in combinations(chosen, 2))]
            self.assertEqual(weighted_interval_profit(jobs), max(profits))
        for coin_flags in product((0, 1), repeat=5):
            coins = [i + 1 for i, flag in enumerate(coin_flags) if flag]
            for amount in range(13):
                vectors = [counts for counts in product(*(range(amount // coin + 1) for coin in coins))
                           if sum(count * coin for count, coin in zip(counts, coins)) == amount]
                self.assertEqual(minimum_coins(coins, amount), min(map(sum, vectors), default=-1))
                self.assertEqual(coin_combination_count(coins, amount), len(vectors))
        for size in range(6):
            for values in product(range(3), repeat=size):
                subsets = [subset for count in range(size + 1) for subset in combinations(values, count)]
                expected = any(2 * sum(subset) == sum(values) for subset in subsets)
                self.assertEqual(equal_subset_partition(values), expected)
                self.assertEqual(unique_permutations(values), sorted(set(permutations(values))))
                positive = [value + 1 for value in values]
                for target in range(7):
                    expected = sorted({tuple(sorted(subset)) for count in range(size + 1) for subset in combinations(positive, count) if sum(subset) == target})
                    actual = single_use_combination_sum(positive, target)
                    self.assertEqual(actual, expected)
                    self.assertTrue(all(sum(item) == target and Counter(item) <= Counter(positive) for item in actual))


if __name__ == "__main__":
    unittest.main()
